"""Progress service — returns the live competency + progress state for one
student.

Each call opens a short DB session and reads the current student's
competency snapshots. The Mastery engine runs *inside* the simulation /
transfer flows — when a competency is promoted to MASTERED, this service
just reads the resulting status from the DB.
"""

from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy.orm import Session

from ..db.models import CourseProgress, LectureProgress
from . import student_state
from .course_catalog import COURSES, find_lecture, get_course


def _utcnow() -> datetime:
    return datetime.now(UTC).replace(tzinfo=None)


def _get_or_create_course_progress(db: Session, user_id: int, course_id: str) -> CourseProgress:
    course = get_course(course_id)
    if course is None:
        raise KeyError(course_id)
    record = (
        db.query(CourseProgress)
        .filter_by(user_id=user_id, course_id=course_id)
        .one_or_none()
    )
    if record is None:
        record = CourseProgress(
            user_id=user_id, course_id=course_id, total_lectures=len(course["lectures"])
        )
        db.add(record)
        db.flush()
    return record


def _serialize(record: CourseProgress) -> dict:
    course = COURSES[record.course_id]
    return {
        "course_id": record.course_id,
        "course_title": course["title"],
        "progress_percentage": record.progress_percentage,
        "completed_lectures": record.completed_lectures_count,
        "total_lectures": record.total_lectures,
        "completed_quizzes": record.completed_quizzes_count,
        "total_quizzes": record.total_quizzes,
        "completed_assignments": record.completed_assignments_count,
        "total_assignments": record.total_assignments,
        "simulation_status": record.simulation_status,
        "review_status": record.review_status,
        "last_lecture": record.last_lecture_id,
        "last_accessed_at": record.last_accessed_at,
    }


def get_course_progress(db: Session, user_id: int, course_id: str) -> dict:
    return _serialize(_get_or_create_course_progress(db, user_id, course_id))


def get_progress_summary(db: Session, user_id: int) -> dict:
    records = [_get_or_create_course_progress(db, user_id, course_id) for course_id in COURSES]
    latest = max(
        (r for r in records if r.last_accessed_at is not None),
        key=lambda r: r.last_accessed_at,
        default=None,
    )
    total_lectures = sum(record.total_lectures for record in records)
    completed = sum(record.completed_lectures_count for record in records)
    return {
        "overall_progress": round((completed / total_lectures) * 100) if total_lectures else 0,
        "courses": [_serialize(record) for record in records],
        "last_active_course": latest.course_id if latest else None,
        "last_lecture": latest.last_lecture_id if latest else None,
    }


def update_lecture_progress(db: Session, user_id: int, lecture_id: str, completed: bool) -> dict:
    found = find_lecture(lecture_id)
    if found is None:
        raise KeyError(lecture_id)
    course_id, course = found
    lecture = (
        db.query(LectureProgress).filter_by(user_id=user_id, lecture_id=lecture_id).one_or_none()
    )
    now = _utcnow()
    if lecture is None:
        lecture = LectureProgress(user_id=user_id, course_id=course_id, lecture_id=lecture_id)
        db.add(lecture)
    lecture.completed = completed
    lecture.completed_at = now if completed else None
    db.flush()
    record = _get_or_create_course_progress(db, user_id, course_id)
    completed_count = (
        db.query(LectureProgress)
        .filter_by(user_id=user_id, course_id=course_id, completed=True)
        .count()
    )
    record.total_lectures = len(course["lectures"])
    record.completed_lectures_count = completed_count
    record.progress_percentage = round((completed_count / record.total_lectures) * 100)
    record.last_lecture_id = lecture_id
    record.last_accessed_at = now
    db.flush()
    return _serialize(record)


def get_full_competencies(student_id: str) -> list[dict]:
    """Compatibility read used by the existing protected competencies route.

    Competencies remain part of the legacy learning flow; course progress is
    intentionally stored independently in ``CourseProgress``.
    """
    return student_state.get_competencies(student_id)
