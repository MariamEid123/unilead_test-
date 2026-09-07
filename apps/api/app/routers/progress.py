import logging

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..auth.dependencies import get_current_user
from ..db import get_db
from ..db.models import User
from ..schemas.progress import CourseProgressResponse, LectureProgressUpdate, ProgressResponse
from ..services import progress_service

router = APIRouter(prefix="/api/progress", tags=["progress"])
_log = logging.getLogger("Areta.progress")


@router.get("", response_model=ProgressResponse)
def get_progress(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> dict:
    _log.debug("progress requested by user=%s", current_user.id)
    result = progress_service.get_progress_summary(db, current_user.id)
    db.commit()
    return result


@router.get("/{course_id}", response_model=CourseProgressResponse)
def get_course_progress(course_id: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> dict:
    try:
        result = progress_service.get_course_progress(db, current_user.id, course_id)
        db.commit()
        return result
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unknown course.") from None


@router.api_route("/lectures/{lecture_id}", methods=["POST", "PATCH"], response_model=CourseProgressResponse)
def update_lecture_progress(
    lecture_id: str,
    update: LectureProgressUpdate = LectureProgressUpdate(),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict:
    try:
        result = progress_service.update_lecture_progress(db, current_user.id, lecture_id, update.completed)
        db.commit()
        return result
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unknown lecture.") from None
