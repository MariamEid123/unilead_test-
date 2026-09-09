"""Sprint 4E — Remediation + Retry flow.

The immutable evidence pipeline:

    Failed Evidence
          ↓
    identify failed criteria / misconception
          ↓
    RemediationPlan (linked to the triggering EvidenceRecord)
          ↓
    Student completes remediation  ->  plan.status = completed
          ↓
    Retry Assessment  ->  a NEW AssessmentAttempt (never mutates #1)
          ↓
    new EvidenceRecord (old evidence is never touched)
          ↓
    Mastery Engine   (evaluate_evidence() -> resolve_and_record())

Two rules are sacred here:

  - REMEDIATION IS NOT MASTERY: creating/completing a plan never changes a
    skill level. Only the Mastery Engine does that, from evidence.
  - RETRY IS NOT RESET: a retry is a fresh attempt appended on top of the
    history. Failed attempts and old evidence are preserved forever.

All mastery writes happen exclusively through
``mastery_engine.resolve_and_record`` — nobody in this module sets a level
directly.
"""

from __future__ import annotations

import json
import logging
from datetime import UTC, datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..db import crud, models
from . import mastery_engine

_log = logging.getLogger("arete.remediation_flow")

_REMEDIATION_SUPPORTED_SOURCES = ("simulation", "assessment", "instructor")


# --- Plan generation --------------------------------------------------------


def _misconception_hint(evidence: models.EvidenceRecord) -> str | None:
    """Best-effort misconception tag from context (never blocks the plan)."""
    try:
        ctx = json.loads(evidence.context_json or "{}")
    except (TypeError, ValueError):
        return None
    return ctx.get("misconception") or ctx.get("misconception_tag")


def create_plan_for_evidence(
    db: Session,
    *,
    evidence: models.EvidenceRecord,
    reason_codes: list[str] | None = None,
    recommended_action: str = "REVIEW_CONCEPT_AND_RETRY",
    conceptual_focus: str | None = None,
    guided_question: str | None = None,
    remediation_steps: list[str] | None = None,
) -> models.RemediationPlan:
    """Create a remediation plan *tied to the evidence that revealed the problem*.

    The plan is linked to the evidence row (``evidence_id``) so every plan
    can be audited — "why did this student get this plan?" -> the evidence
    that triggered it and the criteria that failed.
    """
    if evidence.source_type not in _REMEDIATION_SUPPORTED_SOURCES:
        _log.debug("source %s does not trigger remediation", evidence.source_type)
        return None

    comp = evidence.competency
    comp_code = comp.code if comp is not None else "pid-tuning"

    # Build human-readable reason codes from the actual failed criteria.
    verdicts = json.loads(evidence.metric_json or "{}")
    if reason_codes is None:
        try:
            _verdicts = _evaluate_for_codes(db, evidence)
            reason_codes = [v for v in _verdicts if not v["passed"]]
            reason_codes = [f"{v['metric']} {v['operator']} {v['threshold']}" for v in reason_codes]
        except Exception:  # pragma: no cover — defensive
            reason_codes = _criteria_from_metrics(verdicts)

    steps = remediation_steps or [
        "Review the controller tuning concepts behind the failed criterion.",
        "Re-check the plant response vs the target thresholds.",
        "Run the retry with an adjusted parameter set.",
    ]

    plan = crud.save_remediation_plan(
        db,
        student_id=evidence.student_id,
        competency_id=comp_code,
        detected_misconception=_misconception_hint(evidence),
        recommended_action=recommended_action,
        conceptual_focus=conceptual_focus or f"Rethink {comp_code}",
        guided_question=guided_question or "What changed in your tuning and why?",
        consecutive_failures=0,
        total_attempts=0,
        summary_text="; ".join(reason_codes),
        remediation_steps=steps,
        evidence_id=evidence.id,
        reason_codes_json=json.dumps(reason_codes),
        status="open",
    )
    _log.info(
        "remediation plan %s created for student=%s evidence=%s comp=%s",
        plan.id,
        evidence.student_id,
        evidence.id,
        comp_code,
    )
    return plan


def _evaluate_for_codes(db: Session, evidence: models.EvidenceRecord) -> list[dict]:
    """Re-evaluate the evidence against its competency's MASTERY rubric."""
    rubric = _mastery_rubric(db, evidence.competency_id)
    if not rubric:
        return []
    from .mastery_engine import _metrics_from_evidence, evaluate_criterion

    metrics = _metrics_from_evidence(evidence)
    return [evaluate_criterion(c, metrics) for c in rubric]


def _criteria_from_metrics(metrics: dict) -> list[str]:
    """Fallback human-readable code (no rubric present)."""
    return [f"{k} -> {v}" for k, v in metrics.items()]


def _mastery_rubric(db: Session, competency_id: int) -> list:
    assessment = None
    for a in crud.get_assessments_for_competency(db, competency_id=competency_id):
        if a.kind == "MASTERY":
            assessment = a
            break
    if assessment is None:
        return []
    return crud.get_rubric(db, assessment_id=assessment.id)


def ensure_plan_for_failed_evidence(
    db: Session,
    *,
    student_id: str,
    competency: models.Competency,
    evidence: models.EvidenceRecord,
    reason_codes: list[str] | None = None,
) -> models.RemediationPlan | None:
    """Create an open remediation plan when a failing piece of evidence
    shows a non-mastered state. No-op when a plan already exists for the
    exact evidence row, or the evidence is not from a supported source."""
    existing = crud.get_remediation_plan_for_evidence(db, evidence_id=evidence.id)
    if existing is not None:
        if existing.status == "open":
            return existing
        # A completed plan on the same evidence stays completed; a fresh
        # retry produces a *new* evidence row -> new plan.
        return existing

    # Only failing (non-mastering) evidence generates remediation. If the
    # evidence already demonstrates mastery there is nothing to remediate.
    latest = crud.get_latest_mastery(db, student_id=student_id, competency_id=competency.id)
    if latest is not None and latest.level == "DEMONSTRATED":
        return None

    return create_plan_for_evidence(db, evidence=evidence, reason_codes=reason_codes)


# --- Retry flow -------------------------------------------------------------


def submit_retry(
    db: Session,
    *,
    student_id: str,
    competency_code: str,
    metrics: dict,
    context: dict | None = None,
    source_type: str = "assessment",
    reason_codes: list[str] | None = None,
) -> dict:
    """Run one retry submission through the *full* assessment pipeline.

    Pipeline enforced here (in this exact order — no shortcuts):

        1. NEW AssessmentAttempt (attempt #N+1) for the competency's
           MASTERY assessment — the previous attempt is untouched.
        2. Per-criterion verdicts recorded as AttemptItemResult rows.
        3. A NEW EvidenceRecord is appended (old evidence unchanged).
        4. Mastery Engine: ``resolve_and_record`` decides the level.
           NOTHING here ever writes a level itself.

    Returns a dict describing the attempt, the evidence, and the resolved
    mastery view. Raises HTTPException 404 when the competency is unknown.
    """
    course = (
        db.query(models.Course)
        .filter(models.Course.code == "MEC271")
        .order_by(models.Course.id)
        .first()
    )
    if course is None:
        raise HTTPException(status_code=404, detail="MEC271 course not seeded.")
    competency = crud.get_competency_by_code(db, course_id=course.id, code=competency_code)
    if competency is None:
        raise HTTPException(
            status_code=404,
            detail=f"Competency {competency_code!r} not found.",
        )

    assessment = _assessment_for(db, competency.id)
    if assessment is None:
        raise HTTPException(
            status_code=409,
            detail=f"No MASTERY assessment defined for {competency_code!r}.",
        )

    rubric = crud.get_rubric(db, assessment_id=assessment.id)
    if not rubric:
        raise HTTPException(
            status_code=409,
            detail=f"No rubric defined for {competency_code!r}.",
        )

    # 1) New attempt (number = previous + 1).
    attempt = crud.create_attempt_open(db, assessment_id=assessment.id, student_id=student_id)

    # 2) Evaluate each rubric criterion -> AttemptItemResult rows.
    verdicts: list[dict] = []
    passed_count = 0
    for criterion in rubric:
        verdict = mastery_engine.evaluate_criterion(criterion, metrics)
        verdicts.append(verdict)
        item = models.AttemptItemResult(
            attempt_id=attempt.id,
            task_code=criterion.metric_field,
            metric_field=criterion.metric_field,
            actual=verdict["actual"],
            passed=verdict["passed"],
            misconception_tag=None,
        )
        db.add(item)
        if verdict["passed"]:
            passed_count += 1

    attempt.status = "SUBMITTED"
    attempt.submitted_at = datetime.now(UTC)
    attempt.score = passed_count
    attempt.passed = passed_count == len(rubric) and len(rubric) > 0
    attempt.results_json = json.dumps(verdicts)
    attempt.resolution_json = json.dumps({"passed_count": passed_count, "total": len(rubric)})
    db.flush()

    # 3) New evidence record.
    evidence = crud.add_evidence(
        db,
        student_id=student_id,
        competency_id=competency.id,
        source_type=source_type,
        source_ref_id=attempt.id,
        metric_json=json.dumps(metrics),
        context_json=json.dumps(context or {}),
    )
    db.flush()

    # 4) Mastery Engine decides the level (never write it ourselves).
    mastery = mastery_engine.resolve_and_record(db, student_id=student_id, competency=competency)
    db.flush()

    # If the retry did NOT achieve mastery, ensure an open remediation plan
    # exists for the evidence that revealed the failure.
    level = mastery.level if mastery is not None else "NOT_DEMONSTRATED"
    if level != "DEMONSTRATED":
        reason_codes = reason_codes or [v["metric"] for v in verdicts if not v["passed"]]
        plan = ensure_plan_for_failed_evidence(
            db,
            student_id=student_id,
            competency=competency,
            evidence=evidence,
            reason_codes=reason_codes,
        )
        plan_id = plan.id if plan is not None else None
    else:
        # Achieving mastery completes the open plans for this competency.
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
        "passed": attempt.passed,
        "passed_count": passed_count,
        "total": len(rubric),
        "level": level,
        "reason_codes": reason_codes or [],
        "remediation_plan_id": plan_id,
    }


def _assessment_for(db: Session, competency_id: int) -> models.Assessment | None:
    for a in crud.get_assessments_for_competency(db, competency_id=competency_id):
        if a.kind == "MASTERY":
            return a
    return None


# --- Completion -------------------------------------------------------------


def complete_plan(db: Session, *, student_id: str, plan_id: int) -> models.RemediationPlan | None:
    """Mark a plan as completed (the student finished the remediation work).

    This NEVER changes mastery — completion of remediation is not mastery.
    Only the Mastery Engine can promote a competency.
    """
    plan = crud.get_remediation_plan(db, plan_id=plan_id)
    if plan is None:
        raise HTTPException(status_code=404, detail="Remediation plan not found.")
    if plan.student_id != student_id:
        raise HTTPException(status_code=403, detail="Cannot complete another student's plan.")
    if plan.status != "open":
        return plan
    return crud.complete_remediation_plan(db, plan_id=plan_id)


# --- Read views -------------------------------------------------------------


def plan_traceability(db: Session, *, plan_id: int) -> dict:
    """Full auditable trail for one remediation plan:

    - Which evidence triggered it (evidence_id, metrics, criteria verdicts)
    - Which criteria failed  (reason_codes)
    - Plan lifecycle        (status, completed_at)
    """
    plan = crud.get_remediation_plan(db, plan_id=plan_id)
    if plan is None:
        raise HTTPException(status_code=404, detail="Remediation plan not found.")

    evidence = None
    if plan.evidence_id is not None:
        evidence = (
            db.query(models.EvidenceRecord)
            .filter(models.EvidenceRecord.id == plan.evidence_id)
            .first()
        )

    return {
        "plan_id": plan.id,
        "student_id": plan.student_id,
        "competency_id": plan.competency_id,
        "evidence_id": plan.evidence_id,
        "evidence_metrics": json.loads(evidence.metric_json) if evidence else None,
        "reason_codes": json.loads(plan.reason_codes_json or "[]"),
        "recommended_action": plan.recommended_action,
        "conceptual_focus": plan.conceptual_focus,
        "guided_question": plan.guided_question,
        "status": plan.status,
        "created_at": plan.created_at.isoformat() if plan.created_at else None,
        "completed_at": plan.completed_at.isoformat() if plan.completed_at else None,
    }
