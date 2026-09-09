"""Sprint 5A/5B — the deterministic Student Model.

Derived *on demand* — never a snapshot table — from the immutable evidence
pipeline (EvidenceRecord + Rubric + Attempts + RemediationPlan). The model
answers, per competency:

  - the latest mastery ``level`` the rubric has actually proven;
  - the ``confidence`` that the level is real (recency-weighted pass ratio);
  - the ``weak_criteria`` that failed in the most recent non-passing evidence;
  - the misconceptions still standing in the way (tag frequency);
  - remediation state (open/completed counts + the open plan id).

Confidence contract (user-approved, Sprint 5B)::

    confidence = ( Σ_i λ^i · pass_i ) / ( Σ_i λ^i )

  - i is the recency index: 0 = newest evidence, raising toward older rows;
  - ``pass_i`` is the fraction of *mandatory* rubric criteria passed by
    evidence i (deterministic — the same rubric verdicts the MasteryEngine
    uses, never a reimplementation);
  - ``λ = 0.75`` — recency decay, tunable, never an LLM guess;
  - empty history → ``0.0``.

This is exactly the "later, separate layer" the MasteryEngine docstring
reserves: the number of attempts alone never decides mastery, and confidence
is only ever computed from what the rubric accepted.

No LLM participates anywhere in this module.
"""

from __future__ import annotations

import json
import logging
from collections import Counter
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Session

from ..db import crud, models
from .mastery_engine import evaluate_evidence

if TYPE_CHECKING:
    pass

_log = logging.getLogger("arete.student_model")

# Recency decay for the confidence contract. Newest evidence has weight λ^0 = 1.
LAMBDA = 0.75

DEMONSTRATED = "DEMONSTRATED"
NOT_STARTED = "NOT_DEMONSTRATED"

_DEFAULT_COURSE_CODE = "PHY211"


# --- Pure confidence contract (fully unit-testable) -------------------------


def confidence_from_passes(passes: list[float]) -> float:
    """Recency-weighted pass ratio. ``passes`` is newest-first.

    ``pass_i`` is generally the fraction of mandatory rubric criteria accepted
    for that piece of evidence (in [0, 1]); empty history yields ``0.0``.
    """
    if not passes:
        return 0.0
    num = 0.0
    den = 0.0
    for i, p in enumerate(passes):
        w = LAMBDA**i
        num += w * float(p)
        den += w
    return num / den


# --- Internal helpers --------------------------------------------------------


def _metrics_from_evidence(evidence: models.EvidenceRecord) -> dict:
    try:
        data = json.loads(evidence.metric_json or "{}")
    except (TypeError, ValueError):
        _log.warning("evidence %s has malformed metric_json", evidence.id)
        data = {}
    return data if isinstance(data, dict) else {}


def _context_dict(evidence: models.EvidenceRecord) -> dict:
    try:
        data = json.loads(evidence.context_json or "{}")
    except (TypeError, ValueError):
        data = {}
    return data if isinstance(data, dict) else {}


def _load_assessment(db: Session, competency: models.Competency) -> models.Assessment | None:
    """The active assessment holding the rubric for a competency (MASTERY first)."""
    assessments = crud.get_assessments_for_competency(db, competency_id=competency.id)
    for a in assessments:
        if a.kind == "MASTERY":
            return a
    return assessments[0] if assessments else None


def _count_attempts(db: Session, *, student_id: str, competency) -> int:
    assessment_ids = [
        a.id for a in crud.get_assessments_for_competency(db, competency_id=competency.id)
    ]
    if not assessment_ids:
        return 0
    return (
        db.query(models.AssessmentAttempt.id)
        .filter(
            models.AssessmentAttempt.student_id == student_id,
            models.AssessmentAttempt.assessment_id.in_(assessment_ids),
        )
        .count()
    )


def _aggregate_misconceptions(
    db: Session,
    *,
    student_id: str,
    competency,
    evidence_ctx_tags: list[str],
    limit: int = 5,
) -> list[str]:
    """Misconception tags by frequency: evidence context + item-result tags.

    Deterministic: desc by count, then asc by tag. Item results carry tags
    from any assessment attempt against an assessment of this competency.
    """
    counts: Counter[str] = Counter()
    for tag in evidence_ctx_tags:
        if tag:
            counts[str(tag)] += 1

    assessment_ids = [
        a.id for a in crud.get_assessments_for_competency(db, competency_id=competency.id)
    ]
    if assessment_ids:
        rows = (
            db.query(models.AttemptItemResult.misconception_tag)
            .join(
                models.AssessmentAttempt,
                models.AssessmentAttempt.id == models.AttemptItemResult.attempt_id,
            )
            .join(models.Assessment, models.Assessment.id == models.AssessmentAttempt.assessment_id)
            .filter(
                models.Assessment.id.in_(assessment_ids),
                models.AssessmentAttempt.student_id == student_id,
                models.AttemptItemResult.misconception_tag.isnot(None),
            )
            .all()
        )
        for (tag,) in rows:
            if tag:
                counts[str(tag)] += 1

    return [tag for tag, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))][:limit]


def _resolve_course(
    db: Session, *, course_code: str | None = None, course_id: int | None = None
) -> models.Course:
    """Resolve the course scope: explicit id > explicit code > default."""
    if course_id is not None:
        course = db.get(models.Course, course_id)
        if course is None:
            raise ValueError(f"course {course_id} not found")
        return course
    code = course_code or _DEFAULT_COURSE_CODE
    course = (
        db.query(models.Course)
        .filter(models.Course.code == code)
        .order_by(models.Course.id)
        .first()
    )
    if course is None:
        raise ValueError(f"course {code} not found; has bootstrap seeded the org tree?")
    return course


# --- Model construction -------------------------------------------------------


def _build_competency_profile(
    db: Session,
    *,
    student_id: str,
    competency: models.Competency,
    prereq_comp_ids: list[int],
    levels_by_comp_id: dict[int, str],
    code_by_id: dict[int, str],
) -> dict:
    """One competency's derived profile (Sprint 5A). Deterministic."""
    assessment = _load_assessment(db, competency)
    rubric = crud.get_rubric(db, assessment_id=assessment.id) if assessment is not None else []
    try:
        pass_rule = json.loads(assessment.pass_rule or "{}") if assessment is not None else {}
    except (TypeError, ValueError):
        pass_rule = {}

    evidence_rows = crud.get_evidence_for_competency(
        db, student_id=student_id, competency_id=competency.id
    )

    pass_fractions: list[float] = []
    failed_sets: list[list[str]] = []
    evidence_ctx_tags: list[str] = []
    last_evidence_at: str | None = None
    # Sprint 8B — lineage stamping for the mastery claim of this competency.
    evidence_sources: Counter[str] = Counter()
    proven_ids: list[int] = []

    for ev in reversed(evidence_rows):  # newest first (recency index 0 = newest)
        metrics = _metrics_from_evidence(ev)
        if rubric:
            _level, verdicts, _codes = evaluate_evidence(rubric, metrics, pass_rule)
            pf = _pass_fraction(verdicts)
            if _level == DEMONSTRATED:
                proven_ids.append(ev.id)
        else:
            # No rubric to verify against → proof is only "metrics exist".
            _level = NOT_STARTED
            pf = 1.0 if metrics else 0.0
            verdicts = []
        evidence_sources[ev.source_type] += 1
        pass_fractions.append(pf)
        failed_sets.append([v["metric"] for v in verdicts if v["mandatory"] and not v["passed"]])
        if pf < 1.0:
            ctx = _context_dict(ev)
            tag = ctx.get("misconception") or ctx.get("misconception_tag")
            if tag:
                evidence_ctx_tags.append(str(tag))
        if last_evidence_at is None:
            last_evidence_at = _iso_or_none(ev.created_at)

    confidence = round(confidence_from_passes(pass_fractions), 4)
    # Weak criteria come from the most recent evidence that still had failures.
    weak_criteria = next((failed for failed in failed_sets if failed), [])

    latest = crud.get_latest_mastery(db, student_id=student_id, competency_id=competency.id)
    level = latest.level if latest is not None else NOT_STARTED

    misconceptions = _aggregate_misconceptions(
        db, student_id=student_id, competency=competency, evidence_ctx_tags=evidence_ctx_tags
    )

    plans = (
        db.query(models.RemediationPlan)
        .filter(
            models.RemediationPlan.student_id == student_id,
            models.RemediationPlan.competency_id == competency.code,
        )
        .order_by(models.RemediationPlan.created_at.desc())
        .all()
    )
    remediation_open = sum(1 for p in plans if p.status == "open")
    remediation_completed = sum(1 for p in plans if p.status == "completed")
    open_plan = next((p for p in plans if p.status == "open"), None)

    return {
        "competency_code": competency.code,
        "competency_title": competency.title,
        "competency_id": competency.id,
        "mastery_level": level,
        "confidence": confidence,
        "attempt_count": _count_attempts(db, student_id=student_id, competency=competency),
        "evidence_count": len(evidence_rows),
        "weak_criteria": weak_criteria,
        "misconceptions": misconceptions,
        "remediation_open_count": remediation_open,
        "remediation_completed_count": remediation_completed,
        "open_plan_id": int(open_plan.id) if open_plan is not None else None,
        "evidence_ids": [ev.id for ev in evidence_rows],
        "evidence_sources": dict(evidence_sources),
        "proven_evidence_ids": sorted(proven_ids),
        "prerequisite_codes": sorted(
            code_by_id[pid] for pid in prereq_comp_ids if pid in code_by_id
        ),
        "prerequisites_satisfied": all(
            levels_by_comp_id.get(pid) == DEMONSTRATED for pid in prereq_comp_ids
        ),
        "last_evidence_at": last_evidence_at,
    }


def _pass_fraction(verdicts: list[dict]) -> float:
    mandatory = [v for v in verdicts if v["mandatory"]]
    if not mandatory:
        return 0.0
    return sum(1 for v in mandatory if v["passed"]) / len(mandatory)


def _iso_or_none(value) -> str | None:
    if value is None:
        return None
    if value.tzinfo is None:
        value = value.replace(tzinfo=UTC)
    return value.isoformat()


def build_student_model(
    db: Session,
    *,
    student_id: str,
    course_code: str | None = None,
    course_id: int | None = None,
) -> dict:
    """Derive the full Student Model for one student in one course (5B).

    Read-only, deterministic, and computed per request — nothing is cached or
    stored, so this view can never drift from the evidence it summarizes.
    """
    student = crud.get_student_by_id(db, student_id)
    if student is None:
        raise ValueError(f"student {student_id!r} not found")

    course = _resolve_course(
        db, course_code=course_code or student.course_code, course_id=course_id
    )
    competencies = crud.get_competencies_for_course(db, course_id=course.id)

    # Latest resolved level per competency (prerequisite lookups reuse it).
    levels_by_comp_id: dict[int, str] = {}
    for comp in competencies:
        latest = crud.get_latest_mastery(db, student_id=student_id, competency_id=comp.id)
        levels_by_comp_id[comp.id] = latest.level if latest is not None else NOT_STARTED

    # Prerequisite edges: post_competency_id -> [pre competency codes].
    edges = (
        db.query(models.CompetencyPrerequisite)
        .filter(models.CompetencyPrerequisite.course_id == course.id)
        .all()
    )
    prereq_ids_by_post: dict[int, list[int]] = {}
    for edge in edges:
        prereq_ids_by_post.setdefault(edge.post_competency_id, []).append(edge.pre_competency_id)
    code_by_id = {c.id: c.code for c in competencies}

    profiles: dict[str, dict] = {}
    for comp in competencies:
        prereq_ids = prereq_ids_by_post.get(comp.id, [])
        profiles[comp.code] = _build_competency_profile(
            db,
            student_id=student_id,
            competency=comp,
            prereq_comp_ids=prereq_ids,
            levels_by_comp_id=levels_by_comp_id,
            code_by_id=code_by_id,
        )

    attempted = [p for p in profiles.values() if p["evidence_count"] > 0]
    demonstrated = [p for p in profiles.values() if p["mastery_level"] == DEMONSTRATED]
    overall_confidence = (
        round(sum(p["confidence"] for p in attempted) / len(attempted), 4) if attempted else 0.0
    )

    return {
        "student_id": student_id,
        "course_code": course.code,
        "course_title": course.title,
        "generated_at": datetime.now(UTC).isoformat(),
        "total_competencies": len(competencies),
        "attempted_count": len(attempted),
        "demonstrated_count": len(demonstrated),
        "overall_confidence": overall_confidence,
        "competencies": profiles,
    }
