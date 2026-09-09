"""Sprint 5D — the learning path.

A deterministic walk over the course's prerequisite graph, paramed by a
Student Model. Given a target competency, the path lists every competency
that must come first (transitive prerequisites) followed by the target, in
study order. Each step is labelled with the student's current level,
confidence, and whether it is ``locked`` (a prerequisite has not been
demonstrated yet).

Used by the adaptive controller to turn "advance" into a concrete next step.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from sqlalchemy.orm import Session

from ..db import models

if TYPE_CHECKING:
    pass

_log = logging.getLogger("arete.learning_path")

DEMONSTRATED = "DEMONSTRATED"


def _course_id_by_code(db: Session, course_code: str) -> int | None:
    course = (
        db.query(models.Course)
        .filter(models.Course.code == course_code)
        .order_by(models.Course.id)
        .first()
    )
    return course.id if course is not None else None


def build_learning_path(
    db: Session,
    *,
    student_model: dict,
    target_competency_code: str,
) -> dict:
    """The ordered path to ``target_competency_code`` for this student.

    Deterministic: prerequisites always precede their dependents, ties break
    on competency code. Never reads per-student state beyond the Student
    Model passed in (the graph edges come from the DB, the levels/confidence
    come from the model).
    """
    competencies = student_model.get("competencies", {})
    if target_competency_code not in competencies:
        raise ValueError(f"target competency {target_competency_code!r} not in course")

    course_id = _course_id_by_code(db, student_model.get("course_code", ""))
    prereq_by_post: dict[str, set[str]] = {}
    if course_id is not None:
        edges = (
            db.query(models.CompetencyPrerequisite)
            .filter(models.CompetencyPrerequisite.course_id == course_id)
            .all()
        )
        id_to_code = {int(p["competency_id"]): p["competency_code"] for p in competencies.values()}
        for edge in edges:
            pre_code = id_to_code.get(edge.pre_competency_id)
            post_code = id_to_code.get(edge.post_competency_id)
            if pre_code is None or post_code is None:
                continue
            prereq_by_post.setdefault(post_code, set()).add(pre_code)

    # Ancestors of the target: everything that must precede it.
    ancestors: set[str] = set()

    def _collect(code: str) -> None:
        for pre in prereq_by_post.get(code, set()):
            if pre not in ancestors:
                ancestors.add(pre)
                _collect(pre)

    _collect(target_competency_code)
    path_codes = ancestors | {target_competency_code}

    # Topological order: visit prerequisites first (ties by code).
    ordered: list[str] = []
    visited: set[str] = set()

    def _visit(code: str) -> None:
        if code in visited:
            return
        for pre in sorted(prereq_by_post.get(code, set())):
            if pre in path_codes:
                _visit(pre)
        visited.add(code)
        ordered.append(code)

    _visit(target_competency_code)

    path = []
    for code in ordered:
        profile = competencies.get(code, {})
        level = profile.get("mastery_level", "NOT_DEMONSTRATED")
        blocked_by = sorted(
            pre
            for pre in prereq_by_post.get(code, set())
            if competencies.get(pre, {}).get("mastery_level") != DEMONSTRATED
        )
        locked = bool(blocked_by)
        step_status = (
            "ready"
            if level == DEMONSTRATED
            else "locked"
            if locked
            else "in_progress"
            if profile.get("evidence_count", 0) > 0
            else "not_started"
        )
        path.append(
            {
                "competency_code": code,
                "competency_title": profile.get("competency_title", code),
                "mastery_level": level,
                "confidence": profile.get("confidence", 0.0),
                "evidence_count": profile.get("evidence_count", 0),
                "status": step_status,
                "locked": locked,
                "blocked_by": blocked_by,
            }
        )

    target_level = competencies[target_competency_code].get("mastery_level")
    any_locked = any(step["locked"] for step in path)
    any_progress = any(step["evidence_count"] > 0 for step in path)
    status = (
        "ready"
        if target_level == DEMONSTRATED
        else "blocked"
        if any_locked
        else "in_progress"
        if any_progress
        else "not_started"
    )

    blockers = sorted({pc for step in path for pc in step["blocked_by"]})

    return {
        "course_code": student_model.get("course_code"),
        "target": target_competency_code,
        "status": status,
        "total_steps": len(path),
        "blockers": blockers,
        "path": path,
        "earliest_next_step": earliest_next_step({"path": path}),
    }


def earliest_next_step(path: dict) -> dict | None:
    """The earliest unproven step on an ordered path (Sprint 8D).

    Deterministic: the first competency in study (topological) order whose
    mastery level is not DEMONSTRATED. ``blocked_by`` explains *why* it is
    not yet reachable — the answer is always explainable from the evidence
    and the prerequisite graph.
    """
    for step in path["path"]:
        if step["mastery_level"] != DEMONSTRATED:
            return {
                "competency_code": step["competency_code"],
                "competency_title": step["competency_title"],
                "status": step["status"],
                "blocked_by": list(step["blocked_by"]),
                "evidence_count": step["evidence_count"],
                "confidence": step["confidence"],
                "reason": (
                    "blocked_by_prerequisites" if step["blocked_by"] else "not_demonstrated"
                ),
            }
    return None
