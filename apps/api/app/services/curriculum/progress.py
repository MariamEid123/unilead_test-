"""Curriculum progress recording + per-course progress summaries.

Distinct from the legacy Mastery engine (``services.progress_service`` /
``student_state``): this module tracks *real curriculum artefacts* — which
lessons of a course have been completed and how the practice items went —
and feeds them into the existing evidence timeline + competency snapshots
(``student_state``) so the two views stay consistent.

Building blocks:

* ``LessonProgress`` — one row per (student, lesson) that has been marked
  complete (unique on student_id + lesson_code; recording twice is a no-op).
* ``PracticeResult`` — the latest outcome per (student, practice item);
  upserted on every grade so the last attempt wins.
* ``EvidenceEvent`` rows (event_type ``lesson_completed`` / ``practice_grade``)
  keep the evidence timeline driven by real activity.
"""

from __future__ import annotations

from sqlalchemy.orm import Session, joinedload

from app.db import models
from app.services import student_state

# How much a completed lesson advances a taught competency / overall progress.
_COMPETENCY_BUMP_PER_LESSON = 10
_OVERALL_BUMP_PER_LESSON = 2


# --- Progress summary -------------------------------------------------------


def get_course_progress_summary(db: Session, student_id: str) -> dict:
    """Build the per-course progress shape the frontend ``ProgressResponse``
    contract expects.

    ``courses`` includes every catalog course that has at least one lesson;
    counts are real (lessons completed via LessonProgress, quizzes answered
    correctly via PracticeResult).
    """
    completed_lessons = {
        row.lesson_code
        for row in db.query(models.LessonProgress)
        .filter(models.LessonProgress.student_id == student_id)
        .all()
    }
    correct_items = {
        row.item_id
        for row in db.query(models.PracticeResult)
        .filter(models.PracticeResult.student_id == student_id, models.PracticeResult.correct.is_(True))
        .all()
    }

    courses: list[dict] = []
    last_active: tuple[str, str] | None = None
    for course in (
        db.query(models.Course)
        .options(
            joinedload(models.Course.modules)
            .joinedload(models.Module.lessons)
            .joinedload(models.Lesson.practice_items)
        )
        .order_by(models.Course.id)
        .all()
    ):
        lessons = [lesson for mod in course.modules for lesson in mod.lessons]
        if not lessons:
            continue
        course_completed = [l for l in lessons if l.code in completed_lessons]
        quiz_items = [item for lesson in lessons for item in lesson.practice_items if item.is_active]
        quiz_done = [item for item in quiz_items if item.id in correct_items]
        total_lectures = len(lessons)
        completed_lectures = len(course_completed)
        progress_percentage = round(completed_lectures / total_lectures * 100) if total_lectures else None
        courses.append(
            {
                "course_id": course.code,
                "course_title": course.title,
                "progress_percentage": progress_percentage,
                "completed_lectures": completed_lectures,
                "total_lectures": total_lectures,
                "completed_quizzes": len(quiz_done),
                "total_quizzes": len(quiz_items),
                "completed_assignments": None,
                "total_assignments": None,
                "completed_lessons": sorted(l.code for l in course_completed),
            }
        )

    latest = (
        db.query(models.LessonProgress)
        .filter(models.LessonProgress.student_id == student_id)
        .order_by(models.LessonProgress.completed_at.desc(), models.LessonProgress.id.desc())
        .first()
    )
    if latest is not None:
        last_active = (latest.course_code, latest.lesson_code)

    return {
        "courses": courses,
        "last_active_course": last_active[0] if last_active else None,
        "last_lecture": last_active[1] if last_active else None,
    }


# --- Recording ---------------------------------------------------------------


def mark_lesson_complete(db: Session, student_id: str, lesson: models.Lesson) -> None:
    """Record a completed lesson: upsert LessonProgress, append an evidence
    event, and bump the linked competencies + overall progress."""
    course = lesson.module.course if lesson.module is not None else None
    course_code = course.code if course is not None else ""
    course_title = course.title if course is not None else ""

    existing = (
        db.query(models.LessonProgress)
        .filter(
            models.LessonProgress.student_id == student_id,
            models.LessonProgress.lesson_code == lesson.code,
        )
        .first()
    )
    if existing is None:
        db.add(
            models.LessonProgress(
                student_id=student_id,
                course_code=course_code,
                course_title=course_title,
                lesson_code=lesson.code,
                lesson_title=lesson.title,
            )
        )
    # Commit our session before student_state opens its own connections
    # (SQLite holds one writer at a time).
    db.commit()

    primary = _primary_competency(lesson)
    student_state.append_evidence_event(
        student_id,
        event_type="lesson_completed",
        title=f"Lesson complete: {lesson.title}",
        detail=f"{course_code} — {course_title}".strip(" —") or lesson.code,
        result="PASS",
        competency_id=primary,
    )

    for code in _linked_competency_codes(lesson):
        student_state.bump_competency_progress(code, _COMPETENCY_BUMP_PER_LESSON, student_id)
    student_state.bump_overall_progress(_OVERALL_BUMP_PER_LESSON, student_id)


def record_practice_result(
    db: Session,
    student_id: str,
    lesson: models.Lesson,
    item: models.PracticeItem,
    *,
    correct: bool,
) -> None:
    """Upsert the latest practice outcome and emit an evidence event + bump."""
    row = (
        db.query(models.PracticeResult)
        .filter(
            models.PracticeResult.student_id == student_id,
            models.PracticeResult.item_id == item.id,
        )
        .first()
    )
    course = lesson.module.course if lesson.module is not None else None
    course_code = course.code if course is not None else ""
    if row is None:
        db.add(
            models.PracticeResult(
                student_id=student_id,
                course_code=course_code,
                lesson_code=lesson.code,
                item_id=item.id,
                correct=correct,
            )
        )
    else:
        row.correct = correct
    # Commit before student_state opens its own connections.
    db.commit()

    competency_code = None
    if item.competency_id is not None:
        comp = db.get(models.Competency, item.competency_id)
        competency_code = comp.code if comp is not None else None
    student_state.append_evidence_event(
        student_id,
        event_type="practice_grade",
        title=("Correct" if correct else "Needs review") + f": {lesson.code} practice",
        detail=f"{lesson.title} — item {item.id}",
        result="PASS" if correct else "FAIL",
        competency_id=competency_code,
    )
    if correct and competency_code is not None:
        student_state.bump_competency_progress(competency_code, 5, student_id)


# --- Helpers -----------------------------------------------------------------


def _linked_competency_codes(lesson: models.Lesson) -> list[str]:
    codes: list[str] = []
    for link in lesson.competencies:
        if link.competency is not None:
            codes.append(link.competency.code)
    return codes


def _primary_competency(lesson: models.Lesson) -> str | None:
    codes = _linked_competency_codes(lesson)
    if not codes:
        return None
    # Prefer a 'teaches' link over 'reinforces'/'assesses', else the first.
    for link in lesson.competencies:
        if link.role == "teaches" and link.competency is not None:
            return link.competency.code
    return codes[0]