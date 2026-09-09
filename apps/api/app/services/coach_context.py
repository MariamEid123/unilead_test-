"""Sprint 6A/6D — Coach Context Contract and read-only tool access.

The AI Coach sees the world ONLY through these read-only tools. Every tool
returns facts derived from the deterministic Sprint 5 services (student
model, adaptive engine, learning path, remediation, transfer readiness),
so nothing the coach says can originate from a model that drifted from the
evidence.

Rules:

  - No fact in ``CoachContext`` may come from the LLM.
  - The tool layer exposes NO mutation — the coaching layer can never write
    evidence, mastery, or remediation state. State changes happen only
    through the deliberately user-invoked flows (retry / assessment).
  - ``build_coach_context`` is deterministic given the same DB state.
"""

from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy.orm import Session

from app.db import crud

from . import adaptive_engine, learning_path
from . import student_model as student_model_service
from .transfer_readiness import compute_transfer_readiness

CONTEXT_VERSION = "1"
DEMONSTRATED = "DEMONSTRATED"


def _public_profile(profile: dict) -> dict:
    """The slice of a competency profile the coach is allowed to see."""
    return {
        "competency_code": profile["competency_code"],
        "competency_title": profile["competency_title"],
        "mastery_level": profile["mastery_level"],
        "confidence": profile["confidence"],
        "evidence_count": profile["evidence_count"],
        "weak_criteria": list(profile.get("weak_criteria") or []),
        "misconceptions": list(profile.get("misconceptions") or []),
        "remediation_open_count": profile.get("remediation_open_count", 0),
        "open_plan_id": profile.get("open_plan_id"),
    }


# --- Read-only tools (6D) ---------------------------------------------------


def tool_student_model(db: Session, *, student_id: str) -> dict:
    """The full derived Student Model — the single source of learner truth."""
    return student_model_service.build_student_model(db, student_id=student_id)


def tool_adaptive_focus(db: Session, *, student_model: dict) -> dict | None:
    """The deterministic focus step (``steps[0]``), or None for a done course."""
    steps = adaptive_engine.recommend_next_steps(db, student_model=student_model)
    return adaptive_engine.focus_step(steps)


def tool_learning_path(db: Session, *, student_model: dict, target_competency_code: str) -> dict:
    """The deterministic learning path to one competency."""
    return learning_path.build_learning_path(
        db, student_model=student_model, target_competency_code=target_competency_code
    )


def tool_remediation(db: Session, *, student_model: dict) -> dict:
    """Open remediation plans for the student, plus their catalog resources."""
    open_plans: list[dict] = []
    competencies = student_model.get("competencies", {})
    for profile in competencies.values():
        open_plan_id = profile.get("open_plan_id")
        if open_plan_id is None:
            continue
        plan = crud.get_remediation_plan(db, plan_id=int(open_plan_id))
        resources: list[str] = []
        if plan is not None:
            rows = crud.get_active_remediation_resources(db, competency_code=plan.competency_id)
            resources = [r.resource_code for r in rows]
        open_plans.append(
            {
                "plan_id": open_plan_id,
                "competency_code": profile["competency_code"],
                "resource_codes": resources,
            }
        )
    return {"open_plans": open_plans, "open_count": len(open_plans)}


def tool_transfer(db: Session, *, student_model: dict) -> dict:
    """Transfer readiness gate (DEMONSTRATED and confidence >= 0.60)."""
    return compute_transfer_readiness(student_model)


def tool_recent_evidence(db: Session, *, student_id: str, limit: int = 3) -> list[dict]:
    """The newest evidence-timeline events, facts only."""
    events = crud.list_evidence_events(db, student_id, newest_first=True)[:limit]
    return [
        {
            "event_type": e.event_type,
            "title": e.title,
            "detail": (e.detail or "")[:240],
            "result": e.result,
            "competency_id": e.competency_id,
            "timestamp": e.timestamp.isoformat() if e.timestamp else None,
        }
        for e in events
    ]


def tool_simulation_runs(
    db: Session, *, student_id: str, competency_code: str | None = None, limit: int = 3
) -> list[dict]:
    """The student's recent deterministic PID simulation runs (facts only).

    Each run is the proof lineage (task + gains + telemetry) behind a
    ``simulation`` evidence record. Read-only — the coach can reason about
    a failed run's metrics but can never amend it.
    """
    runs = crud.list_simulation_runs(db, student_id, competency_id=competency_code)[:limit]
    return [
        {
            "run_id": r.id,
            "task_id": r.task_id,
            "competency_code": r.competency_id,
            "attempt": r.attempt,
            "kp": r.kp,
            "ki": r.ki,
            "kd": r.kd,
            "stable": r.stable,
            "overshoot_pct": r.overshoot,
            "settling_time_sec": r.settling_time,
            "rise_time_sec": r.rise_time,
            "steady_state_error": r.steady_state_error,
            "requirements_met": r.requirements_met,
            "result": r.result,
            "misconception": r.misconception,
            "created_at": r.created_at.isoformat() if r.created_at else None,
        }
        for r in runs
    ]


def build_coach_context(
    db: Session,
    *,
    student_id: str,
    intent_code: str,
    intent_mode: str,
    target_competency_code: str | None = None,
) -> dict:
    """Assemble the deterministic CoachContext for one turn.

    ``target_competency_code`` defaults to the adaptive focus competency, or
    to ``pid-tuning`` when nothing is actionable yet (nothing to focus on).
    """
    student_model = tool_student_model(db, student_id=student_id)
    focus = tool_adaptive_focus(db, student_model=student_model)
    target = target_competency_code or (focus or {}).get("competency_code") or "pid-tuning"

    try:
        path = tool_learning_path(db, student_model=student_model, target_competency_code=target)
    except ValueError:
        # Target outside this course — never let the context builder crash
        # the turn; fall back to a path with the target only.
        path = {
            "course_code": student_model.get("course_code"),
            "target": target,
            "status": "not_started",
            "total_steps": 0,
            "blockers": [],
            "path": [],
            "earliest_next_step": None,
        }

    competencies = student_model.get("competencies", {})
    ordered_profiles = sorted(
        (_public_profile(p) for p in competencies.values()),
        key=lambda p: p["competency_code"],
    )
    sim_runs = tool_simulation_runs(db, student_id=student_id, limit=3)
    total_runs = len(crud.list_simulation_runs(db, student_id))
    latest = sim_runs[0] if sim_runs else None

    return {
        "version": CONTEXT_VERSION,
        "student_id": student_id,
        "course": {
            "code": student_model.get("course_code"),
            "title": student_model.get("course_title"),
        },
        "intent": {"code": intent_code, "mode": intent_mode},
        "focus": focus,
        "competencies": ordered_profiles,
        "learning_path": path,
        "remediation": tool_remediation(db, student_model=student_model),
        "evidence": {
            "recent_events": tool_recent_evidence(db, student_id=student_id),
            "attempted_count": student_model.get("attempted_count", 0),
            "demonstrated_count": student_model.get("demonstrated_count", 0),
            "overall_confidence": student_model.get("overall_confidence", 0.0),
        },
        "simulation": {
            "total_runs": total_runs,
            "latest_result": latest["result"] if latest else None,
            "latest_run": latest,
        },
        "transfer": tool_transfer(db, student_model=student_model),
        "generated_at": datetime.now(UTC).isoformat(),
    }
