"""Idempotent curriculum importer.

Turns a structured bundle (``curriculum.content``) into rows: course →
module → lesson → content/resource/competency/practice-item. Safe to call on
every boot: every step is get-or-create keyed on the bundle's stable single
keys, so re-imports update in place without duplicating.

Also importable from the CLI to drop in new lessons without touching code
(see ``apps/api/scripts/import_curriculum.py``).
"""

from __future__ import annotations

import json
import logging
from typing import Any

from sqlalchemy.orm import Session

from app.db import crud, models

_log = logging.getLogger("arete.curriculum.seed")


def ensure_faculty_department(db: Session, *, university_id: int, bundle: dict) -> Any:
    """Get-or-create the faculty + department named by a bundle."""
    dep_code = bundle["department_code"]
    dep_name = bundle["department_name"]
    fac_code = bundle["faculty_code"]
    fac_name = bundle["faculty_name"]

    faculty = (
        db.query(models.Faculty)
        .filter(
            models.Faculty.university_id == university_id,
            models.Faculty.code == fac_code,
        )
        .first()
    )
    if faculty is None:
        faculty = crud.create_faculty(
            db, university_id=university_id, code=fac_code, name=fac_name
        )

    department = (
        db.query(models.Department)
        .filter(
            models.Department.faculty_id == faculty.id,
            models.Department.code == dep_code,
        )
        .first()
    )
    if department is None:
        department = crud.create_department(
            db, faculty_id=faculty.id, code=dep_code, name=dep_name
        )
    return department


def _find_course(db: Session, department_id: int, code: str) -> models.Course | None:
    return (
        db.query(models.Course)
        .filter(models.Course.department_id == department_id, models.Course.code == code)
        .first()
    )


def _upsert_lesson_content(db: Session, lesson_id: int, spec: dict, *, offset: int) -> None:
    sort_order = int(spec.get("sort_order", offset))
    row = (
        db.query(models.LessonContent)
        .filter(
            models.LessonContent.lesson_id == lesson_id,
            models.LessonContent.sort_order == sort_order,
        )
        .first()
    )
    payload = {
        "section_type": spec["section_type"],
        "title": spec.get("title"),
        "body": spec.get("body", ""),
        "metadata_json": json.dumps(spec.get("metadata") or {}),
    }
    if row is None:
        row = models.LessonContent(lesson_id=lesson_id, sort_order=sort_order, **payload)
        db.add(row)
    else:
        for key, value in payload.items():
            setattr(row, key, value)


def import_bundle(db: Session, *, university_id: int, bundle: dict) -> dict:
    """Import one course bundle idempotently. Returns created-course info."""
    course_spec = bundle["course"]
    department = ensure_faculty_department(db, university_id=university_id, bundle=course_spec)

    course = _find_course(db, department.id, course_spec["code"])
    if course is None:
        course = crud.create_course(
            db,
            department_id=department.id,
            code=course_spec["code"],
            title=course_spec["title"],
            credits=course_spec.get("credits", 3),
        )
    else:
        course.title = course_spec["title"]
        course.credits = course_spec.get("credits", course.credits)
    course.description = course_spec.get("description", course.description)

    # --- module -----------------------------------------------------------
    module_spec = course_spec["module"]
    module = (
        db.query(models.Module)
        .filter(models.Module.course_id == course.id, models.Module.code == module_spec["code"])
        .first()
    )
    if module is None:
        module = models.Module(
            course_id=course.id,
            code=module_spec["code"],
            title=module_spec["title"],
            description=module_spec.get("description", ""),
            sort_order=module_spec.get("sort_order", 0),
        )
        db.add(module)
        db.flush()
    else:
        module.title = module_spec["title"]
        module.description = module_spec.get("description", "")

    # --- lesson -----------------------------------------------------------
    lesson_spec = course_spec["lesson"]
    lesson = (
        db.query(models.Lesson)
        .filter(models.Lesson.module_id == module.id, models.Lesson.code == lesson_spec["code"])
        .first()
    )
    if lesson is None:
        lesson = models.Lesson(
            module_id=module.id,
            code=lesson_spec["code"],
            title=lesson_spec["title"],
            description=lesson_spec.get("description", ""),
            estimated_minutes=lesson_spec.get("estimated_minutes"),
            difficulty=lesson_spec.get("difficulty", "beginner"),
            objectives_json=json.dumps(lesson_spec.get("objectives", [])),
            prerequisites_json=json.dumps(lesson_spec.get("prerequisites", [])),
            sort_order=lesson_spec.get("sort_order", 0),
        )
        db.add(lesson)
        db.flush()
    else:
        lesson.title = lesson_spec["title"]
        lesson.description = lesson_spec.get("description", "")
        lesson.objectives_json = json.dumps(lesson_spec.get("objectives", []))
        lesson.prerequisites_json = json.dumps(lesson_spec.get("prerequisites", []))
    lesson_id = lesson.id

    # --- competencies (course-level graph) --------------------------------
    comp_by_code: dict[str, models.Competency] = {}
    for i, comp_spec in enumerate(course_spec.get("competencies", [])):
        comp = crud.ensure_competency(
            db,
            course_id=course.id,
            code=comp_spec["code"],
            title=comp_spec["title"],
            description=comp_spec.get("description", ""),
            taxonomy_level=comp_spec.get("taxonomy_level"),
            sort_order=comp_spec.get("sort_order", i),
        )
        comp_by_code[comp_spec["code"]] = comp

    for pre_code, post_code in course_spec.get("competency_prerequisites", []):
        pre = comp_by_code.get(pre_code)
        post = comp_by_code.get(post_code)
        if pre is None or post is None:
            continue
        crud.ensure_competency_prerequisite(
            db,
            course_id=course.id,
            pre_competency_id=pre.id,
            post_competency_id=post.id,
        )

    # --- lesson <-> competency links --------------------------------------
    for link in course_spec.get("lesson_competencies", []):
        comp = comp_by_code.get(link["code"])
        if comp is None:
            continue
        existing = (
            db.query(models.LessonCompetency)
            .filter(
                models.LessonCompetency.lesson_id == lesson_id,
                models.LessonCompetency.competency_id == comp.id,
            )
            .first()
        )
        if existing is None:
            db.add(
                models.LessonCompetency(
                    lesson_id=lesson_id,
                    competency_id=comp.id,
                    role=link.get("role", "teaches"),
                )
            )

    # --- content blocks (teaching + summary) ------------------------------
    teaching = course_spec.get("lesson_contents", [])
    summary = course_spec.get("summary_contents", [])
    ordered = list(teaching) + [
        {**s, "sort_order": len(teaching) + i} for i, s in enumerate(summary)
    ]
    for i, spec in enumerate(ordered):
        _upsert_lesson_content(db, lesson_id, spec, offset=i)

    # --- resources ---------------------------------------------------------
    for i, res_spec in enumerate(course_spec.get("resources", [])):
        row = (
            db.query(models.LessonResource)
            .filter(
                models.LessonResource.lesson_id == lesson_id,
                models.LessonResource.title == res_spec["title"],
            )
            .first()
        )
        payload = {
            "resource_type": res_spec.get("resource_type", "LINK"),
            "description": res_spec.get("description", ""),
            "external_url": res_spec.get("external_url"),
            "duration_seconds": res_spec.get("duration_seconds"),
            "metadata_json": json.dumps(res_spec.get("metadata") or {}),
            "sort_order": res_spec.get("sort_order", i),
        }
        if row is None:
            db.add(models.LessonResource(lesson_id=lesson_id, title=res_spec["title"], **payload))
        else:
            for key, value in payload.items():
                setattr(row, key, value)

    # --- practice items -----------------------------------------------------
    for i, item_spec in enumerate(course_spec.get("practice_items", [])):
        row = (
            db.query(models.PracticeItem)
            .filter(models.PracticeItem.lesson_id == lesson_id)
            .filter(models.PracticeItem.prompt == item_spec["prompt"])
            .first()
        )
        comp = comp_by_code.get(item_spec.get("competency_code"))
        payload = {
            "competency_id": comp.id if comp else None,
            "level": item_spec.get("level", "UNDERSTAND"),
            "options_json": json.dumps(item_spec.get("options", [])),
            "answer_json": json.dumps(
                {"correct_index": item_spec["correct_index"]}
            ),
            "explanation": item_spec.get("explanation", ""),
            "skill": item_spec.get("skill"),
            "difficulty": item_spec.get("difficulty", 1),
            "sort_order": item_spec.get("sort_order", i),
        }
        if row is None:
            db.add(models.PracticeItem(lesson_id=lesson_id, prompt=item_spec["prompt"], **payload))
        else:
            for key, value in payload.items():
                setattr(row, key, value)

    db.commit()
    return {
        "course_code": course.code,
        "course_id": course.id,
        "module_code": module.code,
        "lesson_code": lesson.code,
        "lesson_id": lesson_id,
    }


def ensure_curriculum_for_university(db: Session, university_id: int) -> list[dict]:
    """Import every registered bundle for a university's default org."""
    from .content import BUNDLES

    imported = []
    for bundle in BUNDLES:
        result = import_bundle(db, university_id=university_id, bundle=bundle)
        imported.append(result)
        _log.info(
            "curriculum imported %s / %s / %s",
            result["course_code"],
            result["module_code"],
            result["lesson_code"],
        )
    return imported
