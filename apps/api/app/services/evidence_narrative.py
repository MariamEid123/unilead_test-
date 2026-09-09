"""Sprint 8A — the Evidence Narrative read model.

The narrative tells the *story the evidence tells*, and it reads from one
place only: the immutable ``evidence_records`` table. Never from the LLM,
never from the coach turn, never from a cached snapshot — if a fact is not
backed by an EvidenceRecord row (with a source_type + source_ref_id pointing
at the durable artifact that produced it), it is not a narrative fact.

Per competency it resolves:

  - ``proven_criteria``    — the mandatory rubric criteria the most recent
    evidence actually passed;
  - ``unproven_criteria``  — mandatory rubric criteria the most recent
    evidence still fails (i.e. what stands between the student and the next
    level);
  - ``misconception_tags`` — the deterministic misconception tags carried by
    the evidence context / item results (same source the Student Model uses);
  - ``evidence_lineage``   — one entry per EvidenceRecord: id, source type,
    source row reference, the deterministic verdict level that evidence
    achieved, the criteria it passed, and its timestamp.

Everything is a pure function of ``evidence_records`` + the competency rubric
(which defines what counts as proven). Deterministic: the same DB state always
yields the same narrative.
"""

from __future__ import annotations

import json
import logging
from collections import Counter
from typing import TYPE_CHECKING

from sqlalchemy.orm import Session

from ..db import crud
from . import mastery_engine

if TYPE_CHECKING:
    from ..db import models

_log = logging.getLogger("arete.evidence_narrative")

DEMONSTRATED = "DEMONSTRATED"


def _metrics_from_evidence(evidence: models.EvidenceRecord) -> dict:
    try:
        data = json.loads(evidence.metric_json or "{}")
    except (TypeError, ValueError):
        _log.warning("evidence %s has malformed metric_json", evidence.id)
        data = {}
    return data if isinstance(data, dict) else {}


def _load_rubric(db: Session, *, competency_id: int) -> tuple[list, dict | None]:
    """The MASTERY assessment's rubric for a competency, plus its pass_rule."""
    for assessment in crud.get_assessments_for_competency(db, competency_id=competency_id):
        if assessment.kind == "MASTERY":
            try:
                pass_rule = json.loads(assessment.pass_rule or "{}")
            except (TypeError, ValueError):
                pass_rule = {}
            return crud.get_rubric(db, assessment_id=assessment.id), pass_rule
    return [], None


def _competency_narrative(
    db: Session,
    *,
    profile: dict,
) -> dict:
    """One competency's evidence narrative (evidence_records only)."""
    competency_id = profile["competency_id"]
    student_id = profile["_student_id"]
    rubric, pass_rule = _load_rubric(db, competency_id=competency_id)
    mandatory_metrics = [c.metric_field for c in rubric if c.mandatory]

    rows = crud.get_evidence_for_competency(db, student_id=student_id, competency_id=competency_id)

    lineage: list[dict] = []
    latest_verdicts: list[dict] = []
    for evidence in rows:
        metrics = _metrics_from_evidence(evidence)
        level, verdicts, _reasons = mastery_engine.evaluate_evidence(rubric, metrics, pass_rule)
        passed = [v["metric"] for v in verdicts if v.get("mandatory") and v.get("passed")]
        lineage.append(
            {
                "evidence_id": evidence.id,
                "source_type": evidence.source_type,
                "source_ref_id": evidence.source_ref_id,
                "verdict_level": level,
                "passed_criteria": sorted(passed),
                "created_at": evidence.created_at.isoformat() if evidence.created_at else None,
            }
        )
        latest_verdicts = verdicts

    proven = sorted(v["metric"] for v in latest_verdicts if v.get("mandatory") and v.get("passed"))
    unproven = sorted(
        v["metric"] for v in latest_verdicts if v.get("mandatory") and not v.get("passed")
    )
    if not latest_verdicts and rubric:
        unproven = sorted(mandatory_metrics)

    return {
        "proven_criteria": proven,
        "unproven_criteria": unproven,
        "misconception_tags": list(profile.get("misconceptions") or []),
        "evidence_lineage": lineage,
    }


def build_evidence_narrative(db: Session, *, student_model: dict) -> dict:
    """The Evidence Narrative read model for one student's whole course.

    The only source of facts is ``evidence_records``; ``student_model`` only
    provides structure (which competencies exist, their ids) and the
    deterministic misconception aggregation the Student Model already owns.
    """
    competencies = student_model.get("competencies", {})
    source_counts: Counter[str] = Counter()
    narrative_by_code: dict[str, dict] = {}

    for code, profile in competencies.items():
        narrative = _competency_narrative(
            db,
            profile={**profile, "_student_id": student_model.get("student_id")},
        )
        narrative_by_code[code] = narrative
        for entry in narrative["evidence_lineage"]:
            source_counts[entry["source_type"]] += 1

    return {
        "student_id": student_model.get("student_id"),
        "course_code": student_model.get("course_code"),
        "total_evidence": sum(source_counts.values()),
        "evidence_counts_by_source": dict(sorted(source_counts.items())),
        "competencies": narrative_by_code,
    }
