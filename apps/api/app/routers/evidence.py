"""Evidence router — read-only views of a student's evidence timeline.

The ``student_id`` is taken from the JWT (``get_current_student``) for the
student-facing route, and from the URL for the instructor-facing route.
"""

import logging

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from ..auth.dependencies import get_current_instructor, get_current_student
from ..db import crud, get_db
from ..db.models import Student, User
from ..schemas.instructor import EvidenceEvent
from ..services import evidence_service, instructor_service

router = APIRouter(prefix="/api/evidence", tags=["evidence"])
_log = logging.getLogger("arete.evidence")


@router.get("/me/timeline", response_model=list[EvidenceEvent])
def get_my_timeline(current_student: Student = Depends(get_current_student)) -> list[dict]:
    """Return the current student's evidence timeline, newest-first."""
    _log.debug("evidence timeline requested by student=%s", current_student.student_id)
    return evidence_service.get_timeline(current_student.student_id)


@router.get("/{student_id}/timeline", response_model=list[EvidenceEvent])
def get_student_timeline(
    student_id: str,
    request: Request = None,  # type: ignore[assignment]
    current_user: User = Depends(get_current_instructor),
    db: Session = Depends(get_db),
) -> list[dict]:
    """Instructor view: return a student's evidence timeline by student_id —
    gated to students enrolled in a section the instructor teaches.

    Response policy (Sprint 4F): 404 for a student that does not exist; 403
    when the student exists but is outside the instructor's sections. Denied
    reads are written to the audit trail with outcome=DENIED.
    """
    ip = request.client.host if request.client else "unknown"
    student = crud.get_student_by_id(db, student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No student found with the given ID."
        )
    if not instructor_service.is_student_in_scope(db, current_user.id, student_id):
        crud.add_audit_log(
            db,
            actor_user_id=current_user.id,
            actor_role=current_user.role or "instructor",
            action="instructor_view",
            target_type="student",
            target_id=student_id,
            detail="evidence timeline denied: student not in an instructor's section",
            ip_address=ip,
            outcome="DENIED",
            university_id=current_user.university_id,
        )
        db.commit()
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Student not in an instructor's section.",
        )
    crud.add_audit_log(
        db,
        actor_user_id=current_user.id,
        actor_role=current_user.role or "instructor",
        action="instructor_view",
        target_type="student",
        target_id=student_id,
        detail="evidence timeline view",
        ip_address=ip,
        outcome="OK",
        university_id=current_user.university_id,
    )
    db.commit()
    _log.info(
        "evidence timeline requested by instructor=%d for student=%s", current_user.id, student_id
    )
    return evidence_service.get_timeline(student_id)
