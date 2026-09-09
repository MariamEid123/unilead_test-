"""Sprint 5G — Student Model + adaptive endpoints.

One read-only surface exposing the deterministic layers built in Sprint 5:

  - ``GET /api/student-model/me``           → the requesting student's model
  - ``GET /api/student-model/me/adaptive``  → their prioritized next steps
  - ``GET /api/student-model/me/path/{code}``→ the path to a target competency
  - ``GET /api/student-model/me/readiness`` → transfer/build readiness gate

...plus instructor-scoped equivalents that follow the Sprint 4F policy:

  - ``GET /api/student-model/instructors/{student_id}/...``
    404 when the student does not exist; 403 when the student exists but is
    outside the instructor's sections (denied reads land in the audit trail
    with ``outcome=DENIED``).

Students reach only their own record (``get_current_student``); instructors
can only view students inside the sections they teach.
"""

from __future__ import annotations

import logging

from fastapi import APIRouter, Depends, HTTPException, Path, Request, status
from sqlalchemy.orm import Session

from ..auth.dependencies import get_current_instructor, get_current_student
from ..db import crud, get_db, models
from ..schemas.student_model import (
    LearningPathResponse,
    NextStep,
    StudentModelResponse,
    TransferReadinessResponse,
)
from ..services import (
    adaptive_engine,
    evidence_narrative,
    instructor_service,
    learning_path,
    student_model,
    transfer_readiness,
)

router = APIRouter(prefix="/api/student-model", tags=["student-model"])
_log = logging.getLogger("arete.student_model_router")


# --- shared helpers ----------------------------------------------------------


def _build_model(db: Session, student_id: str) -> dict:
    try:
        return student_model.build_student_model(db, student_id=student_id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


def _build_model_with_narrative(db: Session, student_id: str) -> dict:
    """Student Model + the Sprint 8A Evidence Narrative (evidence_records only)."""
    model = _build_model(db, student_id)
    model["evidence_narrative"] = evidence_narrative.build_evidence_narrative(
        db, student_model=model
    )
    return model


def _student_exists(db: Session, student_id: str) -> bool:
    return crud.get_student_by_id(db, student_id) is not None


def _denied_audit(db: Session, current_user: models.User, ip: str, target_id: str) -> None:
    crud.add_audit_log(
        db,
        actor_user_id=current_user.id,
        actor_role=current_user.role or "instructor",
        action="instructor_view",
        target_type="student",
        target_id=target_id,
        detail="student model denied: student not in an instructor's section",
        ip_address=ip,
        outcome="DENIED",
        university_id=current_user.university_id,
    )
    db.commit()


def _instructor_scoped_student(
    db: Session,
    current_user: models.User,
    ip: str,
    student_id: str,
) -> dict:
    """Resolve + enforce instructor section scope for a target student.

    Sprint 4F: 404 for a missing student; 403 (with a DENIED audit row) when
    the student exists but is out of the instructor's sections.
    """
    if not _student_exists(db, student_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No student found with the given ID.",
        )
    if not instructor_service.is_student_in_scope(db, current_user.id, student_id):
        _denied_audit(db, current_user, ip, student_id)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Student not in an instructor's section.",
        )
    return _build_model(db, student_id)


# --- student (self) ---------------------------------------------------------


@router.get("/me", response_model=StudentModelResponse)
def my_student_model(
    student: models.Student = Depends(get_current_student),
    db: Session = Depends(get_db),
) -> dict:
    """The requesting student's derived model + evidence narrative."""
    return _build_model_with_narrative(db, student.student_id)


@router.get("/me/adaptive", response_model=list[NextStep])
def my_next_steps(
    student: models.Student = Depends(get_current_student),
    db: Session = Depends(get_db),
) -> list[dict]:
    """Prioritized next steps for the requesting student."""
    model = _build_model(db, student.student_id)
    return adaptive_engine.recommend_next_steps(db, model)


@router.get("/me/path/{competency_code}", response_model=LearningPathResponse)
def my_path_to(
    competency_code: str = Path(..., max_length=64, pattern=r"^[a-z0-9-]+$"),
    student: models.Student = Depends(get_current_student),
    db: Session = Depends(get_db),
) -> dict:
    """The ordered path to a target competency for the requesting student."""
    model = _build_model(db, student.student_id)
    try:
        return learning_path.build_learning_path(
            db, student_model=model, target_competency_code=competency_code
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get("/me/readiness", response_model=TransferReadinessResponse)
def my_readiness(
    student: models.Student = Depends(get_current_student),
    db: Session = Depends(get_db),
) -> dict:
    """Transfer/build readiness gate for the requesting student."""
    model = _build_model(db, student.student_id)
    return transfer_readiness.compute_transfer_readiness(model)


# --- instructor (section-scoped) --------------------------------------------


@router.get("/instructors/{student_id}/model", response_model=StudentModelResponse)
def instructor_student_model(
    student_id: str = Path(..., max_length=64, pattern=r"^[a-zA-Z0-9_-]+$"),
    request: Request = None,  # type: ignore[assignment]
    current_user: models.User = Depends(get_current_instructor),
    db: Session = Depends(get_db),
) -> dict:
    """An instructor views one of their students' models + evidence narrative."""
    ip = request.client.host if request.client else "unknown"
    model = _instructor_scoped_student(db, current_user, ip, student_id)
    model["evidence_narrative"] = evidence_narrative.build_evidence_narrative(
        db, student_model=model
    )
    return model


@router.get("/instructors/{student_id}/adaptive", response_model=list[NextStep])
def instructor_student_steps(
    student_id: str = Path(..., max_length=64, pattern=r"^[a-zA-Z0-9_-]+$"),
    request: Request = None,  # type: ignore[assignment]
    current_user: models.User = Depends(get_current_instructor),
    db: Session = Depends(get_db),
) -> list[dict]:
    """An instructor views one of their students' prioritized steps."""
    ip = request.client.host if request.client else "unknown"
    model = _instructor_scoped_student(db, current_user, ip, student_id)
    return adaptive_engine.recommend_next_steps(db, model)


@router.get("/instructors/{student_id}/readiness", response_model=TransferReadinessResponse)
def instructor_student_readiness(
    student_id: str = Path(..., max_length=64, pattern=r"^[a-zA-Z0-9_-]+$"),
    request: Request = None,  # type: ignore[assignment]
    current_user: models.User = Depends(get_current_instructor),
    db: Session = Depends(get_db),
) -> dict:
    """An instructor checks one of their students' transfer readiness."""
    ip = request.client.host if request.client else "unknown"
    model = _instructor_scoped_student(db, current_user, ip, student_id)
    return transfer_readiness.compute_transfer_readiness(model)
