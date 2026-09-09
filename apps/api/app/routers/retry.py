"""Retry + remediation router (Sprint 4E).

Rules enforced:

  - RETRY IS NOT RESET: ``POST /api/retry/{competency_code}`` creates a NEW
    AssessmentAttempt and a NEW EvidenceRecord. Old attempts and old evidence
    are never modified, and repeated retries only append to history.
  - Everyone (student retry AND instructor review) passes through the Mastery
    Engine via ``remediation_flow.submit_retry`` — no endpoint writes a level
    directly.
  - Student routes are self-scoped to the JWT student; instructor routes are
    gated by ``instructor_service.is_student_in_scope`` so an instructor can
    never read remediation/evidence for a student outside their sections.
"""

from __future__ import annotations

import json
import logging

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..auth.dependencies import get_current_instructor, get_current_student
from ..db import crud, get_db
from ..db.models import Student, User
from ..schemas.retry import RetryRequest, RetryResponse, RetryReviewRequest
from ..services import instructor_service, remediation_flow

router = APIRouter(prefix="/api/retry", tags=["retry"])
_log = logging.getLogger("arete.retry")


@router.post("/{competency_code}", response_model=RetryResponse)
def submit_retry(
    competency_code: str,
    payload: RetryRequest,
    current_student: Student = Depends(get_current_student),
    db: Session = Depends(get_db),
) -> dict:
    """Submit one retry for the current student. Self-scoped: the student
    can only create attempts for themselves.

    The response carries the new ``attempt_id`` + ``evidence_id`` and the
    resolved mastery ``level`` (decided by the Mastery Engine, not here).
    When the retry doesn't achieve mastery, an open remediation plan is
    created and its id is returned.
    """
    _log.info("retry submit student=%s comp=%s", current_student.student_id, competency_code)
    result = remediation_flow.submit_retry(
        db,
        student_id=current_student.student_id,
        competency_code=competency_code,
        metrics=payload.metric_dict(),
        source_type="assessment",
    )
    db.commit()
    return result


@router.get("/me/plans")
def my_plans(
    current_student: Student = Depends(get_current_student),
    db: Session = Depends(get_db),
) -> list[dict]:
    """The current student's remediation plans, newest first."""
    plans = crud.get_remediation_plans_for_student(db, student_id=current_student.student_id)
    return [_plan_summary(p) for p in plans]


@router.post("/me/plans/{plan_id}/complete")
def complete_my_plan(
    plan_id: int,
    current_student: Student = Depends(get_current_student),
    db: Session = Depends(get_db),
) -> dict:
    """Mark the student's own open remediation plan as completed.

    Completion is NOT mastery — the level is only ever decided by the next
    evidence submission flowing through the Mastery Engine.
    """
    plan = remediation_flow.complete_plan(
        db, student_id=current_student.student_id, plan_id=plan_id
    )
    if plan is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plan not found.")
    db.commit()
    return _plan_summary(plan)


@router.post("/students/{student_id}/review")
def instructor_review_retry(
    student_id: str,
    payload: RetryReviewRequest,
    current_user: User = Depends(get_current_instructor),
    db: Session = Depends(get_db),
) -> dict:
    """Instructor submits a retry assessment for a scoped student.

    Gated by section scope (test #8). Also passes through the Mastery Engine
    — an instructor can never write ``DEMONSTRATED`` directly.
    """
    if not instructor_service.is_student_in_scope(db, current_user.id, student_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Student not in an instructor's section.",
        )
    result = remediation_flow.submit_retry(
        db,
        student_id=student_id,
        competency_code=payload.competency_code,
        metrics=payload.metric_dict(),
        source_type="instructor",
    )
    db.commit()
    return result


@router.get("/students/{student_id}/plans")
def student_plans(
    student_id: str,
    current_user: User = Depends(get_current_instructor),
    db: Session = Depends(get_db),
) -> list[dict]:
    """Instructor view: remediation plans for one scoped student."""
    if not instructor_service.is_student_in_scope(db, current_user.id, student_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Student not in an instructor's section.",
        )
    plans = crud.get_remediation_plans_for_student(
        db, student_id=student_id, include_completed=True
    )
    return [_plan_summary(p) for p in plans]


@router.get("/plans/{plan_id}/trace")
def plan_trace(
    plan_id: int,
    current_user: User = Depends(get_current_instructor),
    db: Session = Depends(get_db),
) -> dict:
    """Full traceability for one plan: triggering evidence, failed criteria,
    recommended action, lifecycle. Evidence must belong to a scoped student."""
    trace = remediation_flow.plan_traceability(db, plan_id=plan_id)
    if not instructor_service.is_student_in_scope(db, current_user.id, trace["student_id"]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Student not in an instructor's section.",
        )
    return trace


def _plan_summary(plan) -> dict:
    try:
        reason_codes = json.loads(plan.reason_codes_json or "[]")
    except (TypeError, ValueError):
        reason_codes = []
    return {
        "id": plan.id,
        "student_id": plan.student_id,
        "competency_id": plan.competency_id,
        "evidence_id": plan.evidence_id,
        "reason_codes": reason_codes,
        "recommended_action": plan.recommended_action,
        "status": plan.status,
        "created_at": plan.created_at.isoformat() if plan.created_at else None,
        "completed_at": plan.completed_at.isoformat() if plan.completed_at else None,
    }
