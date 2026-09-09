"""PID simulation service — the deterministic robotics proof pipeline (Sprint 7).

The run is *evidence*: the same single evidence stream the assessment
pipeline uses, never a side-channel. Flow enforced here (matching the
``submit_retry`` decision pipeline, no shortcuts):

    deterministic telemetry (task preset + gains)   [7A/7B/7C contract]
        -> AssessmentAttempt #N (competency's MASTERY assessment)   [7E]
        -> AttemptItemResult per rubric criterion (mastery verdicts)
        -> durable SimulationRun row (task + gains + telemetry)     [7D]
        -> EvidenceRecord (source_type="simulation")
        -> Mastery Engine ``resolve_and_record`` (never written here)
        -> open remediation plan on FAIL / complete plans on PASS

Library AI Education engines are deterministic *infra*; Compass owns
evidence, attempts, mastery, and plans. The in-memory library student model
is intentionally NOT fed from here — the DB pipeline is the single source.
"""

from __future__ import annotations

import json
import logging
from datetime import UTC, datetime

from fastapi import HTTPException

from ..db import SessionLocal, crud, models
from ..schemas.simulation import SimulationResult
from . import mastery_engine, student_state
from .remediation_flow import ensure_plan_for_failed_evidence
from .simulation_contract import get_task, simulate_gains

_log = logging.getLogger("arete.simulation")

_METRIC_KEYS = ("overshoot", "settling_time", "rise_time", "steady_state_error", "stable")
"""Rubric metric keys persisted in evidence.metric_json — must match the DB rubric."""


def _misconception_name(metrics: dict) -> str | None:
    """Map the run's metrics to a PID misconception tag (FAIL only)."""
    try:
        from ai_education.reasoning.misconceptions import diagnose_misconception
        from ai_education.robotics.telemetry import StepResponseTelemetry

        telemetry = StepResponseTelemetry(
            overshoot_pct=metrics["overshoot"],
            settling_time_sec=metrics["settling_time"],
            rise_time_sec=metrics["rise_time"],
            steady_state_error=metrics["steady_state_error"],
            is_stable=metrics["stable"],
        )
        m = diagnose_misconception(telemetry)
        return m.name if m and m.name != "NONE" else None
    except Exception:  # pragma: no cover — defensive
        _log.debug("Could not diagnose misconception", exc_info=True)
        return None


def run_simulation(request_data, student_id: str) -> dict:
    """Run one deterministic PID simulation and route its evidence through the
    standard attempt -> rubric -> evidence -> mastery -> plan pipeline.

    Raises HTTPException 404 for unknown task/competency, 409 when the
    competency has no mastery instrument (same contract as retries).
    """
    try:
        task = get_task(request_data.task_id)
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Unknown task_id {request_data.task_id!r}."
        ) from None

    metrics = simulate_gains(
        task.task_id, kp=request_data.kp, ki=request_data.ki, kd=request_data.kd
    )

    db = SessionLocal()
    try:
        outcome = _record_evidence(
            db,
            student_id=student_id,
            task=task,
            kp=request_data.kp,
            ki=request_data.ki,
            kd=request_data.kd,
            metrics=metrics,
        )
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

    # Timeline event uses its own committed session — never inside the
    # evidence transaction (sqlite single-writer).
    student_state.append_evidence_event(
        student_id=student_id,
        event_type="simulation_run",
        title=f"Simulation run #{outcome['attempt_number']}",
        detail=(
            f"Kp={request_data.kp:.2f} Ki={request_data.ki:.2f} Kd={request_data.kd:.2f} → "
            f"overshoot {metrics['overshoot']:.1f}% / "
            f"settling {metrics['settling_time']:.2f}s / "
            f"SSE {metrics['steady_state_error']:.4f}. "
            f"{'Met requirements.' if outcome['passed'] else 'Failed requirements.'}"
        ),
        result="PASS" if outcome["passed"] else "FAIL",
        competency_id=task.competency_code,
    )

    misconception = _misconception_name(metrics)
    return SimulationResult(
        stable=metrics["stable"],
        overshoot=round(metrics["overshoot"], 3),
        settling_time=round(metrics["settling_time"], 3),
        rise_time=round(metrics["rise_time"], 3),
        steady_state_error=round(metrics["steady_state_error"], 4),
        kp=request_data.kp,
        ki=request_data.ki,
        kd=request_data.kd,
        requirements_met=outcome["passed"],
        result="PASS" if outcome["passed"] else "FAIL",
        attempt=outcome["attempt_number"],
        competency_id=outcome["competency_code"],
        misconception=misconception,
        attempt_id=outcome["attempt_id"],
        evidence_id=outcome["evidence_id"],
        remediation_plan_id=outcome["remediation_plan_id"],
        mastery_level=outcome["level"],
    ).model_dump()


def _record_evidence(
    db,
    *,
    student_id: str,
    task,
    kp: float,
    ki: float,
    kd: float,
    metrics: dict,
) -> dict:
    """Run the unified evidence pipeline for a simulation outcome."""
    course = (
        db.query(models.Course)
        .filter(models.Course.code == "MEC271")
        .order_by(models.Course.id)
        .first()
    )
    if course is None:
        raise HTTPException(status_code=404, detail="MEC271 course not seeded.")
    competency = crud.get_competency_by_code(db, course_id=course.id, code=task.competency_code)
    if competency is None:
        raise HTTPException(
            status_code=404,
            detail=f"Competency {task.competency_code!r} not found.",
        )

    assessment = None
    for a in crud.get_assessments_for_competency(db, competency_id=competency.id):
        if a.kind == "MASTERY":
            assessment = a
            break
    if assessment is None:
        raise HTTPException(
            status_code=409,
            detail=f"No MASTERY assessment defined for {task.competency_code!r}.",
        )
    rubric = crud.get_rubric(db, assessment_id=assessment.id)
    if not rubric:
        raise HTTPException(
            status_code=409,
            detail=f"No rubric defined for {task.competency_code!r}.",
        )

    # 1) New attempt for the competency's MASTERY assessment.
    attempt = crud.create_attempt_open(db, assessment_id=assessment.id, student_id=student_id)

    # 2) Per-criterion verdicts via the Mastery Engine.
    verdicts: list[dict] = []
    passed_count = 0
    for criterion in rubric:
        verdict = mastery_engine.evaluate_criterion(criterion, metrics)
        verdicts.append(verdict)
        db.add(
            models.AttemptItemResult(
                attempt_id=attempt.id,
                task_code=criterion.metric_field,
                metric_field=criterion.metric_field,
                actual=verdict["actual"],
                passed=verdict["passed"],
                misconception_tag=None,
            )
        )
        if verdict["passed"]:
            passed_count += 1

    attempt.status = "SUBMITTED"
    attempt.submitted_at = datetime.now(UTC)
    attempt.score = passed_count
    attempt.passed = passed_count == len(rubric) and len(rubric) > 0
    attempt.results_json = json.dumps(verdicts)
    attempt.resolution_json = json.dumps({"passed_count": passed_count, "total": len(rubric)})
    db.flush()

    # 3) Durable SimulationRun lineage row (task + gains + telemetry).
    run = crud.save_simulation_run(
        db,
        student_id=student_id,
        competency_id=task.competency_code,
        task_id=task.task_id,
        attempt=attempt.attempt_number,
        kp=kp,
        ki=ki,
        kd=kd,
        stable=metrics["stable"],
        overshoot=metrics["overshoot"],
        settling_time=metrics["settling_time"],
        rise_time=metrics["rise_time"],
        steady_state_error=metrics["steady_state_error"],
        requirements_met=attempt.passed,
        result="PASS" if attempt.passed else "FAIL",
        misconception=_misconception_name(metrics),
    )

    # 4) EvidenceRecord pointing at the run — the authoritative proof lineage.
    evidence = crud.add_evidence(
        db,
        student_id=student_id,
        competency_id=competency.id,
        source_type="simulation",
        source_ref_id=run.id,
        metric_json=json.dumps({k: metrics[k] for k in _METRIC_KEYS}),
        context_json=json.dumps(
            {
                "task_id": task.task_id,
                "kp": kp,
                "ki": ki,
                "kd": kd,
                "setpoint": task.setpoint,
                "simulation_run_id": run.id,
                "misconception": _misconception_name(metrics),
            }
        ),
    )
    db.flush()

    # 5) Mastery Engine decides the level (never write it ourselves).
    mastery = mastery_engine.resolve_and_record(db, student_id=student_id, competency=competency)
    db.flush()
    level = mastery.level if mastery is not None else "NOT_DEMONSTRATED"

    # 6) Open a plan on FAIL; complete open plans once mastery is shown.
    if level != "DEMONSTRATED":
        reason_codes = [v["metric"] for v in verdicts if not v["passed"]]
        plan = ensure_plan_for_failed_evidence(
            db,
            student_id=student_id,
            competency=competency,
            evidence=evidence,
            reason_codes=reason_codes or None,
        )
        plan_id = plan.id if plan is not None else None
    else:
        for open_plan in crud.get_open_remediation_plans(
            db, student_id=student_id, competency_id=competency.code
        ):
            crud.complete_remediation_plan(db, plan_id=open_plan.id)
        plan_id = None

    db.flush()

    return {
        "attempt_number": attempt.attempt_number,
        "attempt_id": attempt.id,
        "evidence_id": evidence.id,
        "simulation_run_id": run.id,
        "passed": attempt.passed,
        "passed_count": passed_count,
        "total": len(rubric),
        "level": level,
        "competency_code": task.competency_code,
        "remediation_plan_id": plan_id,
    }
