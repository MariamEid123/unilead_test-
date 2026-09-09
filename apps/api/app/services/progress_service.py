"""Progress service — returns the live competency + progress state for one
student.

Each call opens a short DB session and reads the current student's
competency snapshots. The Mastery engine runs *inside* the simulation /
transfer flows — when a competency is promoted to MASTERED, this service
just reads the resulting status from the DB.

The ``courses`` breakdown measures the student against the *real* imported
curriculum (how many lessons of each course really completed, how many
practice items answered correctly) — see ``services.curriculum.progress``.
"""

from __future__ import annotations

from ..db import SessionLocal
from . import student_state
from .curriculum import progress as curriculum_progress
from .mock_data import COURSE_CODE, COURSE_TITLE


def get_progress_summary(student_id: str) -> dict:
    competencies = student_state.get_competencies(student_id)
    active = student_state.get_active_competency(student_id)

    # Keep legacy section headings (MEC271 days) only if the student's record
    # still carries them; otherwise fall back to the seeded physics course.
    code = COURSE_CODE
    title = COURSE_TITLE
    db = SessionLocal()
    try:
        course_progress = curriculum_progress.get_course_progress_summary(db, student_id)
    finally:
        db.close()

    return {
        "overall_progress": student_state.get_overall_progress(student_id),
        "competencies": [{"name": c["name"], "status": c["status"]} for c in competencies],
        "recommended_next_activity": f"{active['name']} Practice",
        "course_code": code,
        "course_title": title,
        "courses": course_progress["courses"],
        "last_active_course": course_progress["last_active_course"],
        "last_lecture": course_progress["last_lecture"],
    }


def get_full_competencies(student_id: str) -> list[dict]:
    return student_state.get_competencies(student_id)