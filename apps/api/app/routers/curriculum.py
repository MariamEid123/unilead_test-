"""Curriculum catalog API.

Read-only views over the imported curriculum: course/module/lesson tree,
lecture sections, summary, video resources and practice items (with
server-side grading that never ships answers in the list view).

Endpoints require any verified user (student, instructor or admin): the
catalog is the university-wide curriculum, not scoped to a student record,
and practice grading here is a stateless self-check (it writes no learning
events — those go through the learning loop services).
"""

from __future__ import annotations

import logging

from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel

from ..auth.dependencies import get_current_student, get_current_user
from ..db import SessionLocal, crud
from ..db.models import User
from ..schemas.curriculum import (
    ContentSection,
    CourseDetail,
    CourseLessonMaterials,
    CourseListItem,
    LessonDetail,
    PracticeGradeResult,
    PracticeItemView,
    VideoResource,
)
from ..schemas.progress import ProgressResponse
from ..services.curriculum import catalog
from ..services.curriculum.progress import mark_lesson_complete, record_practice_result
from ..services import progress_service

router = APIRouter(prefix="/api/curriculum", tags=["curriculum"])
_log = logging.getLogger("arete.curriculum")

_LESSON_CODE_PATTERN = r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$"
_COURSE_CODE_PATTERN = r"^[A-Z0-9][A-Z0-9-]{0,15}$"


def _with_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/courses", response_model=list[CourseListItem])
def list_courses(_: User = Depends(get_current_user), db=Depends(_with_db)):
    return catalog.list_courses(db)


@router.get("/courses/{code}", response_model=CourseDetail)
def get_course(
    code: str = Path(..., pattern=_COURSE_CODE_PATTERN),
    _: User = Depends(get_current_user),
    db=Depends(_with_db),
) -> CourseDetail:
    detail = catalog.get_course_detail(db, code)
    if detail is None:
        raise HTTPException(status_code=404, detail=f"Course '{code}' not found.")
    return detail


@router.get("/courses/{code}/materials", response_model=list[CourseLessonMaterials])
def get_course_materials(
    code: str = Path(..., pattern=_COURSE_CODE_PATTERN),
    _: User = Depends(get_current_user),
    db=Depends(_with_db),
) -> list[CourseLessonMaterials]:
    """Data-driven course materials (videos + links) grouped by lesson.

    Lecturers add materials by editing the course bundle; the frontend
    Materials tab renders whatever this endpoint returns.
    """
    materials = catalog.get_course_materials(db, code)
    if materials is None:
        raise HTTPException(status_code=404, detail=f"Course '{code}' not found.")
    return materials


@router.get("/lessons/{code}", response_model=LessonDetail)
def get_lesson(
    code: str = Path(..., pattern=_LESSON_CODE_PATTERN),
    _: User = Depends(get_current_user),
    db=Depends(_with_db),
) -> LessonDetail:
    detail = catalog.get_lesson_detail(db, code)
    if detail is None:
        raise HTTPException(status_code=404, detail=f"Lesson '{code}' not found.")
    return detail


@router.get("/lessons/{code}/lecture", response_model=list[ContentSection])
def get_lecture(
    code: str = Path(..., pattern=_LESSON_CODE_PATTERN),
    _: User = Depends(get_current_user),
    db=Depends(_with_db),
) -> list[ContentSection]:
    sections = catalog.get_lecture_sections(db, code)
    if sections is None:
        raise HTTPException(status_code=404, detail=f"Lesson '{code}' not found.")
    return sections


@router.get("/lessons/{code}/summary", response_model=list[ContentSection])
def get_summary(
    code: str = Path(..., pattern=_LESSON_CODE_PATTERN),
    _: User = Depends(get_current_user),
    db=Depends(_with_db),
) -> list[ContentSection]:
    sections = catalog.get_summary_sections(db, code)
    if sections is None:
        raise HTTPException(status_code=404, detail=f"Lesson '{code}' not found.")
    return sections


@router.get("/lessons/{code}/videos", response_model=list[VideoResource])
def get_videos(
    code: str = Path(..., pattern=_LESSON_CODE_PATTERN),
    _: User = Depends(get_current_user),
    db=Depends(_with_db),
) -> list[VideoResource]:
    videos = catalog.get_videos(db, code)
    if videos is None:
        raise HTTPException(status_code=404, detail=f"Lesson '{code}' not found.")
    return videos


@router.get("/lessons/{code}/practice", response_model=list[PracticeItemView])
def get_practice(
    code: str = Path(..., pattern=_LESSON_CODE_PATTERN),
    _: User = Depends(get_current_user),
    db=Depends(_with_db),
) -> list[PracticeItemView]:
    items = catalog.list_practice_items(db, code)
    if items is None:
        raise HTTPException(status_code=404, detail=f"Lesson '{code}' not found.")
    return items


class _GradeRequest(BaseModel):
    item_id: int
    selected_index: int


@router.post("/lessons/{code}/practice/grade", response_model=PracticeGradeResult)
def grade_practice(
    payload: _GradeRequest,
    code: str = Path(..., pattern=_LESSON_CODE_PATTERN),
    current_user: User = Depends(get_current_user),
    db=Depends(_with_db),
) -> PracticeGradeResult:
    try:
        result = catalog.grade_practice_item(
            db, code, item_id=payload.item_id, selected_index=payload.selected_index
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    if result is None:
        raise HTTPException(status_code=404, detail=f"Lesson '{code}' or item not found.")

    # A *student* caller feeds the result into the evidence pipeline (the
    # self-check itself stays stateless — instructors/admins browsing the
    # catalog never write to a learner's timeline).
    students = crud.get_students_by_user_id(db, current_user.id)
    if current_user.role == "student" and students:
        lesson = catalog.get_lesson(db, code)
        item = next((i for i in lesson.practice_items if i.id == payload.item_id), None) if lesson else None
        if lesson is not None and item is not None:
            record_practice_result(
                db,
                students[0].student_id,
                lesson,
                item,
                correct=result["correct"],
            )
    return result


@router.post("/lessons/{code}/complete", response_model=ProgressResponse)
def complete_lesson(
    code: str = Path(..., pattern=_LESSON_CODE_PATTERN),
    current_student=Depends(get_current_student),
    db=Depends(_with_db),
) -> dict:
    """Mark a lesson complete for the current student.

    Records a LessonProgress row + evidence event and bumps the linked
    competency / overall progress, then returns the fresh progress summary so
    the frontend can update in one round trip.
    """
    lesson = catalog.get_lesson(db, code)
    if lesson is None:
        raise HTTPException(status_code=404, detail=f"Lesson '{code}' not found.")
    mark_lesson_complete(db, current_student.student_id, lesson)
    return progress_service.get_progress_summary(current_student.student_id)
