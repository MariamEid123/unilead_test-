"""Sprint 4D — the Mastery Engine.

Deterministic, evidence-based mastery resolution. This module is the
single source of truth for the question *"what level has this student
proven for a competency?"*.

Pipeline (the architectural contract):

    Simulation            (or assessment , transfer, ...)
        ↓
    EvidenceRecord        - *what the student did* (objective metrics only)
        ↓
    Rubric Evaluation     - *what counts as success* (deterministic rules)
        ↓
    MasteryRecord         - *what we have proven* (immutable history)
        ↓
    CompetencySnapshot    - derived, read-fast cache of the latest level

Rules enforced here:
  - Level ladder:  NOT_DEMONSTRATED < DEVELOPING < DEMONSTRATED.
  - DEMONSTRATED  requires ALL mandatory rubric criteria to hold on a single
    valid piece of objective evidence (``all_mandatory`` gate).
  - DEVELOPING    applies when at least one mandatory criterion holds but the
    full gate does not.
  - NOT_DEMONSTRATED otherwise (no evidence yet, or nothing passes).
  - The *number of attempts* never decides mastery by itself — only what the
    evidence actually shows. (2-of-3 style confidence policies are a later,
    separate layer and are deliberately not consulted here.)
  - No LLM participates. Decisions are pure functions of rubric + metrics.

MasteryRecord rows are immutable and never overwritten; each distinct level
resolution appends one row, so a student's journey
``NOT_DEMONSTRATED -> DEVELOPING -> DEMONSTRATED`` is three rows. The derived
CompetencySnapshot is refreshed to the latest resolved level for fast reads.
"""

from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING

from sqlalchemy.orm import Session

from ..db import crud, models

if TYPE_CHECKING:
    pass

_log = logging.getLogger("arete.mastery")

# Canonical level ladder: index = strength.
LEVELS = ("NOT_DEMONSTRATED", "DEVELOPING", "DEMONSTRATED")
LEVEL_ORDER = {name: i for i, name in enumerate(LEVELS)}

# Downward snapshot statuses (keeps the Compass status contract in one place).
MASTERY_TO_SNAPSHOT_STATUS = {
    "NOT_DEMONSTRATED": "not_started",
    "DEVELOPING": "developing",
    "DEMONSTRATED": "demonstrated",
}

# Rubric operators supported by the deterministic evaluator.
_OPS = {
    "<=": lambda actual, threshold: actual is not None and actual <= threshold,
    "<": lambda actual, threshold: actual is not None and actual < threshold,
    ">=": lambda actual, threshold: actual is not None and actual >= threshold,
    ">": lambda actual, threshold: actual is not None and actual > threshold,
    "==": lambda actual, threshold: actual is not None and actual == threshold,
    "is_true": lambda actual, threshold: bool(actual) is True,
    "is_false": lambda actual, threshold: bool(actual) is False,
}


def _load_assessment(db: Session, competency: models.Competency) -> models.Assessment | None:
    """The active MASTERY assessment for a competency (rubric source)."""
    assessments = crud.get_assessments_for_competency(db, competency_id=competency.id)
    for a in assessments:
        if a.kind == "MASTERY":
            return a
    return assessments[0] if assessments else None


def evaluate_criterion(criterion: models.AssessmentRubricCriterion, metrics: dict) -> dict:
    """Evaluate one rubric criterion against evidence metrics. Pure + safe.

    Missing metrics count as a failed criterion (no data → not proven).
    Returns a dict the caller can stash into an attempt/verdict log.
    """
    actual = metrics.get(criterion.metric_field)
    op = _OPS.get(criterion.operator)
    # Numbers compare numerically; bools compare as truth.
    try:
        if op is None:
            passed = False
        elif criterion.threshold is not None:
            passed = bool(op(float(actual), float(criterion.threshold)))
        else:
            passed = bool(op(actual, None))
    except (TypeError, ValueError):
        passed = False
    return {
        "metric": criterion.metric_field,
        "operator": criterion.operator,
        "threshold": criterion.threshold,
        "actual": actual,
        "passed": passed,
        "mandatory": criterion.mandatory,
    }


def evaluate_evidence(
    rubric: list[models.AssessmentRubricCriterion],
    metrics: dict,
    pass_rule: dict | None = None,
) -> tuple[str, list[dict], list[str]]:
    """Deterministically resolve a competency level from evidence metrics.

    Returns ``(level, verdicts, reason_codes)``. Raises nothing; a missing
    rubric or empty metrics resolves to NOT_DEMONSTRATED.

    The ``pass_rule`` dict may carry ``all_mandatory`` (default True) and/or
    ``min_criteria`` — both are defensive overrides; the default gate is
    "all mandatory criteria must pass".
    """
    if not rubric:
        return "NOT_DEMONSTRATED", [], ["no_rubric"]

    verdicts = [evaluate_criterion(c, metrics) for c in rubric]
    mandatory = [v for v in verdicts if v["mandatory"]]
    mandatory_passed = [v for v in mandatory if v["passed"]]

    all_mandatory = bool((pass_rule or {}).get("all_mandatory", True))
    min_criteria = int((pass_rule or {}).get("min_criteria", len(mandatory)))

    gate_satisfied = all_mandatory and len(mandatory_passed) == len(mandatory)
    if not all_mandatory:
        gate_satisfied = len(mandatory_passed) >= max(min_criteria, 1)

    if gate_satisfied:
        return "DEMONSTRATED", verdicts, ["all_mandatory_passed"]
    if mandatory_passed:
        codes = [f"mandatory_failed:{v['metric']}" for v in mandatory if not v["passed"]]
        return "DEVELOPING", verdicts, codes or ["partial_passed"]
    return "NOT_DEMONSTRATED", verdicts, ["no_criterion_passed"]


def _metrics_from_evidence(evidence: models.EvidenceRecord) -> dict:
    try:
        data = json.loads(evidence.metric_json or "{}")
    except (TypeError, ValueError):
        _log.warning("evidence %s has malformed metric_json", evidence.id)
        data = {}
    return data if isinstance(data, dict) else {}


def resolve_and_record(
    db: Session,
    *,
    student_id: str,
    competency: models.Competency,
    evidence_ids: list[int] | None = None,
) -> models.MasteryRecord | None:
    """Evaluate a student's latest objective evidence and append a mastery row.

    Reads every immutable EvidenceRecord for (student, competency), finds the
    strongest one that satisfies the rubric gate, resolves the level, and
    appends a MasteryRecord **only when the level changes**. Then refreshes
    the derived ``CompetencySnapshot`` (latest resolved state).

    Returns the new/unchanged latest MasteryRecord, or ``None`` when there is
    neither evidence nor rubric to decide on.
    """
    evidence = crud.get_evidence_for_competency(
        db, student_id=student_id, competency_id=competency.id
    )
    if not evidence:
        return None

    assessment = _load_assessment(db, competency)
    if assessment is None:
        return None
    rubric = crud.get_rubric(db, assessment_id=assessment.id)
    if not rubric:
        return None

    try:
        pass_rule = json.loads(assessment.pass_rule or "{}")
    except (TypeError, ValueError):
        pass_rule = {}

    # Pick the strongest evidence that satisfies the gate: iterate from newest
    # → oldest, keep the first level achieved (evidence is ordered oldest first,
    # so reversing yields the latest first).
    chosen: tuple[str, list[dict], list[str], list[int]] | None = None
    for ev in reversed(evidence):
        if evidence_ids and ev.id not in evidence_ids:
            continue
        level, verdicts, reasons = evaluate_evidence(rubric, _metrics_from_evidence(ev), pass_rule)
        if chosen is None or LEVEL_ORDER[level] > LEVEL_ORDER[chosen[0]]:
            chosen = (level, verdicts, reasons, [ev.id])
        if LEVEL_ORDER[level] == LEVEL_ORDER["DEMONSTRATED"]:
            break  # highest achievable — stop early

    if chosen is None:
        return None

    level, verdicts, reasons, driving_ids = chosen

    latest = crud.get_latest_mastery(db, student_id=student_id, competency_id=competency.id)
    if latest is not None and latest.level == level:
        # No state change → history stays untouched (immutable).
        return latest

    record = crud.add_mastery_record(
        db,
        student_id=student_id,
        competency_id=competency.id,
        level=level,
        rubric_json=json.dumps(verdicts),
        reason_codes_json=json.dumps(reasons),
        evidence_ids_json=json.dumps(driving_ids),
    )
    db.flush()

    # Refresh the derived snapshot (status + simple progress share).
    crud.upsert_competency(
        db,
        student_id=student_id,
        competency_id=competency.code,
        competency_name=competency.title,
        status=MASTERY_TO_SNAPSHOT_STATUS.get(level, "not_started"),
        progress=_snapshot_progress(verdicts),
    )
    db.flush()
    return record


def _snapshot_progress(verdicts: list[dict]) -> int:
    """0-100 progress for the derived snapshot (deterministic heuristic)."""
    if not verdicts:
        return 0
    passed = sum(1 for v in verdicts if v["passed"])
    return round(passed / len(verdicts) * 100)


def resolve_level_for_display(db: Session, *, student_id: str, competency_id: int) -> dict:
    """Best-effort current mastery view for read endpoints.

    Returns the latest resolved level (or NOT_DEMONSTRATED when nothing has
    been decided), plus the evidence count. Never writes.
    """
    latest = crud.get_latest_mastery(db, student_id=student_id, competency_id=competency_id)
    evidence_count = len(
        crud.get_evidence_for_competency(db, student_id=student_id, competency_id=competency_id)
    )
    return {
        "level": latest.level if latest is not None else "NOT_DEMONSTRATED",
        "level_order": LEVEL_ORDER.get(
            latest.level if latest is not None else "NOT_DEMONSTRATED", 0
        ),
        "evidence_count": evidence_count,
        "reason_codes": json.loads(latest.reason_codes_json) if latest else [],
        "resolved_at": latest.resolved_at if latest is not None else None,
    }


def competencies_with_latest_mastery(
    db: Session, *, student_id: str, competency_ids: list[int]
) -> dict[int, dict]:
    """Map competency_id → current display-level, for grouped reads."""
    # Simple approach: fetch history per competency and keep latest — small N.
    out: dict[int, dict] = {}
    for cid in competency_ids:
        latest = crud.get_latest_mastery(db, student_id=student_id, competency_id=cid)
        out[cid] = {
            "level": latest.level if latest else "NOT_DEMONSTRATED",
            "evidence_count": len(
                crud.get_evidence_for_competency(db, student_id=student_id, competency_id=cid)
            ),
        }
    return out
