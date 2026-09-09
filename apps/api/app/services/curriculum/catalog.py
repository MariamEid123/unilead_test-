"""Curriculum catalog — read-only DB queries behind the /api/curriculum API.

Kept out of the router so tests and future adaptive routes can reuse the
same serialisers. No writes happen here: imports go through
``services/curriculum/seed.py``.
"""

from __future__ import annotations

import json
from typing import Any

from sqlalchemy.orm import Session, joinedload

from app.db import models

# Content blocks a lesson's lecture view includes (summary blocks are only
# served by the /summary view).
_LECTURE_TYPES = {
    "TEXT",
    "FORMULA",
    "EXAMPLE",
    "KEY_POINT",
    "WARNING",
    "TABLE",
    "IMAGE",
    "VIDEO",
    "DIFFICULT_CONCEPT",
}


def _bm(data: str) -> dict[str, Any]:
    try:
        parsed = json.loads(data)
        return parsed if isinstance(parsed, dict) else {}
    except (TypeError, ValueError):
        return {}


def _ls(data: str) -> list[str]:
    try:
        parsed = json.loads(data)
        return parsed if isinstance(parsed, list) else []
    except (TypeError, ValueError):
        return []


def _lesson_card(lesson: models.Lesson) -> dict[str, Any]:
    return {
        "code": lesson.code,
        "title": lesson.title,
        "description": lesson.description,
        "difficulty": lesson.difficulty,
        "estimated_minutes": lesson.estimated_minutes,
        "sort_order": lesson.sort_order,
        "section_count": len(lesson.contents),
        "video_count": sum(1 for r in lesson.resources if r.resource_type == "VIDEO"),
        "practice_count": len(lesson.practice_items),
    }


def get_course(db: Session, code: str) -> models.Course | None:
    """Load a course by code with its module → lesson tree."""
    return (
        db.query(models.Course)
        .options(
            joinedload(models.Course.modules)
            .joinedload(models.Module.lessons)
            .joinedload(models.Lesson.contents),
            joinedload(models.Course.modules)
            .joinedload(models.Module.lessons)
            .joinedload(models.Lesson.resources),
            joinedload(models.Course.modules)
            .joinedload(models.Module.lessons)
            .joinedload(models.Lesson.practice_items),
        )
        .filter(models.Course.code == code)
        .first()
    )


def list_courses(db: Session) -> list[dict[str, Any]]:
    courses = db.query(models.Course).order_by(models.Course.id).all()
    rows: list[dict[str, Any]] = []
    for course in courses:
        lesson_count = sum(len(m.lessons) for m in course.modules)
        rows.append(
            {
                "id": course.id,
                "code": course.code,
                "title": course.title,
                "description": course.description,
                "credits": course.credits,
                "module_count": len(course.modules),
                "lesson_count": lesson_count,
            }
        )
    return rows


def get_course_detail(db: Session, code: str) -> dict[str, Any] | None:
    course = get_course(db, code)
    if course is None:
        return None
    return {
        "id": course.id,
        "code": course.code,
        "title": course.title,
        "description": course.description,
        "credits": course.credits,
        "modules": [
            {
                "code": m.code,
                "title": m.title,
                "description": m.description,
                "sort_order": m.sort_order,
                "lessons": [_lesson_card(lesson) for lesson in m.lessons],
            }
            for m in course.modules
        ],
    }


def get_lesson(db: Session, code: str) -> models.Lesson | None:
    return (
        db.query(models.Lesson)
        .options(
            joinedload(models.Lesson.contents),
            joinedload(models.Lesson.resources),
            joinedload(models.Lesson.practice_items),
            joinedload(models.Lesson.competencies),
        )
        .filter(models.Lesson.code == code)
        .first()
    )


def get_lesson_detail(db: Session, code: str) -> dict[str, Any] | None:
    lesson = get_lesson(db, code)
    if lesson is None:
        return None
    module = lesson.module
    course = module.course if module is not None else None
    links: list[dict[str, Any]] = []
    for link in lesson.competencies:
        comp = link.competency
        if comp is None:
            continue
        links.append({"code": comp.code, "title": comp.title, "role": link.role})
    links.sort(key=lambda c: c["code"])
    return {
        "code": lesson.code,
        "title": lesson.title,
        "description": lesson.description,
        "difficulty": lesson.difficulty,
        "estimated_minutes": lesson.estimated_minutes,
        "objectives": _ls(lesson.objectives_json),
        "prerequisites": _ls(lesson.prerequisites_json),
        "course_code": course.code if course is not None else "",
        "course_title": course.title if course is not None else "",
        "module_code": module.code if module is not None else "",
        "module_title": module.title if module is not None else "",
        "competencies": links,
        "section_count": len(lesson.contents),
        "video_count": sum(1 for r in lesson.resources if r.resource_type == "VIDEO"),
        "practice_count": len(lesson.practice_items),
    }


def _section(block: models.LessonContent) -> dict[str, Any]:
    return {
        "section_type": block.section_type,
        "title": block.title,
        "body": block.body,
        "sort_order": block.sort_order,
        "metadata": _bm(block.metadata_json),
    }


def get_lecture_sections(db: Session, code: str) -> list[dict[str, Any]] | None:
    lesson = get_lesson(db, code)
    if lesson is None:
        return None
    return [
        _section(b)
        for b in lesson.contents
        if b.section_type in _LECTURE_TYPES and b.section_type != "SUMMARY"
    ]


def get_summary_sections(db: Session, code: str) -> list[dict[str, Any]] | None:
    lesson = get_lesson(db, code)
    if lesson is None:
        return None
    return [
        _section(b)
        for b in lesson.contents
        if b.section_type in ("SUMMARY", "KEY_POINT")
    ]


def get_videos(db: Session, code: str) -> list[dict[str, Any]] | None:
    lesson = get_lesson(db, code)
    if lesson is None:
        return None
    return [
        {
            "title": r.title,
            "description": r.description,
            "external_url": r.external_url,
            "duration_seconds": r.duration_seconds,
            "sort_order": r.sort_order,
            "metadata": _bm(r.metadata_json),
        }
        for r in lesson.resources
        if r.resource_type == "VIDEO"
    ]


def get_course_materials(db: Session, code: str) -> list[dict[str, Any]] | None:
    """Every resource of a course's lessons, flat and grouped by lesson.

    Backs the course ''Materials'' tab: data-driven (a lecturer adds materials
    by editing the course bundle in ``services/curriculum/content_it.py``), never
    hard-coded in the frontend. Returns None when the course doesn't exist.
    """
    course = get_course(db, code)
    if course is None:
        return None
    materials: list[dict[str, Any]] = []
    for module in course.modules:
        for lesson in module.lessons:
            resources = [
                {
                    "title": r.title,
                    "description": r.description,
                    "external_url": r.external_url,
                    "duration_seconds": r.duration_seconds,
                    "sort_order": r.sort_order,
                    "metadata": _bm(r.metadata_json),
                }
                for r in lesson.resources
            ]
            if not resources:
                continue
            materials.append(
                {
                    "lesson_code": lesson.code,
                    "lesson_title": lesson.title,
                    "module_code": module.code,
                    "module_title": module.title,
                    "resources": resources,
                }
            )
    return materials


def list_practice_items(db: Session, code: str) -> list[dict[str, Any]] | None:
    lesson = get_lesson(db, code)
    if lesson is None:
        return None
    rows: list[dict[str, Any]] = []
    for item in lesson.practice_items:
        if not item.is_active:
            continue
        rows.append(
            {
                "id": item.id,
                "level": item.level,
                "prompt": item.prompt,
                "options": _ls(item.options_json),
                "skill": item.skill,
                "difficulty": item.difficulty,
                "sort_order": item.sort_order,
            }
        )
    return rows


def grade_practice_item(
    db: Session, code: str, *, item_id: int, selected_index: int
) -> dict[str, Any] | None:
    lesson = get_lesson(db, code)
    if lesson is None:
        return None
    item = next((i for i in lesson.practice_items if i.id == item_id and i.is_active), None)
    if item is None:
        return None
    options = _ls(item.options_json)
    if not options or not (0 <= selected_index < len(options)):
        raise ValueError("selected_index out of range")
    correct_index = int(json.loads(item.answer_json).get("correct_index", -1))
    return {
        "item_id": item.id,
        "correct": selected_index == correct_index,
        "correct_index": correct_index,
        "explanation": item.explanation,
    }
