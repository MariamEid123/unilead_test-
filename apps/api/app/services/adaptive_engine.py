"""Sprint 5C/5E — deterministic adaptive controller.

Rule-based next-step engine that consumes the Student Model produced by
``student_model`` and produces a prioritized list of interventions.
No LLM participates — every rule is a pure function of mastery level,
confidence, weak criteria, misconceptions, prerequisite codes, and
remediation-plan state.

Priority ladder (higher takes precedence):

  1. ``complete_remediation`` — an open plan exists: finish it first.
  2. ``unlock_prerequisite`` — a prerequisite has not been demonstrated:
     study it before attempting the target.
  3. ``practice`` — rubric criteria still failing: targeted practice backed
     by the 5E remediation catalog.
  4. ``revalidate`` — ``DEMONSTRATED`` but confidence is low (stale or
     sparse evidence): re-check.
  5. ``advance`` — ``DEMONSTRATED`` and confident: move to the next
     competency in the learning path.
  6. ``start`` — no evidence yet: take the first step.

The 5E resource selector scores catalog rows against the student's current
state (competency, misconceptions, weak criteria) and recommends the best
fit.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from sqlalchemy.orm import Session

from ..db import crud

if TYPE_CHECKING:
    pass

_log = logging.getLogger("arete.adaptive_engine")

# Priority constants — lower integer = higher priority.
PRIORITY = {
    "complete_remediation": 1,
    "unlock_prerequisite": 2,
    "practice": 3,
    "revalidate": 4,
    "advance": 5,
    "start": 6,
}

# Below this confidence threshold a *DEMONSTRATED* competency is revalidated.
REVALIDATE_CONFIDENCE = 0.60

_MAX_STEPS = 10


# --- Resource selection (5E) ------------------------------------------------


def select_remediation_resources(
    db: Session,
    *,
    competency_code: str,
    weak_criteria: list[str],
    misconceptions: list[str],
    limit: int = 2,
) -> list[dict]:
    """Score and rank catalog resources against the student's current state.

    Scoring (deterministic, no LLM):
      +3  competency match
      +2  misconception match
      +1  rubric criterion (weak) match
      ties → resource_code ascending
    """
    from ..db.models import RemediationResource

    candidates = crud.get_active_remediation_resources(db, competency_code=competency_code)
    scored: list[tuple[int, str, RemediationResource]] = []

    for res in candidates:
        score = 0
        if res.competency_code == competency_code:
            score += 3
        if res.misconception_tag and res.misconception_tag in misconceptions:
            score += 2
        if res.metric_field and res.metric_field in weak_criteria:
            score += 1
        if score > 0:
            scored.append((score, res.resource_code, res))

    scored.sort(key=lambda t: (-t[0], t[1]))
    return [
        {
            "resource_code": res.resource_code,
            "title": res.title,
            "kind": res.kind,
            "body": res.body,
            "score": score,
        }
        for score, _code, res in scored[:limit]
    ]


# --- Next-step rules (5C) ---------------------------------------------------


def _missing_prerequisites(competencies: dict[str, dict], profile: dict) -> list[str]:
    return sorted(
        pc
        for pc in profile.get("prerequisite_codes", [])
        if competencies.get(pc, {}).get("mastery_level", "NOT_DEMONSTRATED") != "DEMONSTRATED"
    )


def rule_for_profile(competencies: dict[str, dict], profile: dict) -> dict | None:
    """One competency's highest-priority step (first matching rule wins)."""
    level = profile["mastery_level"]

    if level != "DEMONSTRATED" and profile.get("open_plan_id") is not None:
        return {
            "priority": PRIORITY["complete_remediation"],
            "action": "complete_remediation",
            "reason": "open_remediation_plan",
            "competency_code": profile["competency_code"],
            "competency_title": profile["competency_title"],
            "plan_id": profile["open_plan_id"],
        }

    missing = _missing_prerequisites(competencies, profile)
    if level != "DEMONSTRATED" and missing:
        return {
            "priority": PRIORITY["unlock_prerequisite"],
            "action": "unlock_prerequisite",
            "reason": "prerequisite_not_demonstrated",
            "competency_code": profile["competency_code"],
            "competency_title": profile["competency_title"],
            "missing_prerequisites": missing,
        }

    if level != "DEMONSTRATED" and profile.get("weak_criteria"):
        return {
            "priority": PRIORITY["practice"],
            "action": "practice",
            "reason": "weak_rubric_criteria",
            "competency_code": profile["competency_code"],
            "competency_title": profile["competency_title"],
            "weak_criteria": list(profile["weak_criteria"]),
            "misconceptions": list(profile["misconceptions"]),
        }

    if level == "DEMONSTRATED" and profile["confidence"] < REVALIDATE_CONFIDENCE:
        return {
            "priority": PRIORITY["revalidate"],
            "action": "revalidate",
            "reason": "low_confidence",
            "competency_code": profile["competency_code"],
            "competency_title": profile["competency_title"],
            "confidence": profile["confidence"],
        }

    if level == "DEMONSTRATED" and not missing:
        return {
            "priority": PRIORITY["advance"],
            "action": "advance",
            "reason": "demonstrated_and_confident",
            "competency_code": profile["competency_code"],
            "competency_title": profile["competency_title"],
            "confidence": profile["confidence"],
        }

    if level == "NOT_DEMONSTRATED" and profile.get("evidence_count", 0) == 0:
        return {
            "priority": PRIORITY["start"],
            "action": "start",
            "reason": "no_evidence_yet",
            "competency_code": profile["competency_code"],
            "competency_title": profile["competency_title"],
        }

    return {
        "priority": PRIORITY["practice"],
        "action": "practice",
        "reason": "not_demonstrated",
        "competency_code": profile["competency_code"],
        "competency_title": profile["competency_title"],
        "weak_criteria": list(profile.get("weak_criteria", [])),
        "misconceptions": list(profile.get("misconceptions", [])),
    }


def recommend_next_steps(
    db: Session,
    student_model: dict,
    *,
    resource_limit: int = 2,
) -> list[dict]:
    """Produce a prioritized intervention list from the Student Model.

    Reads only the remediation catalog from the DB (resource selection);
    the student's state comes entirely from ``student_model``. ``steps[0]``
    is the focus — the single most actionable intervention.
    """
    competencies = student_model.get("competencies", {})

    steps: list[dict] = []
    for _code, profile in competencies.items():
        step = rule_for_profile(competencies, profile)
        if step is not None:
            steps.append(step)

    steps.sort(key=lambda s: (s["priority"], s["competency_code"]))

    for step in steps:
        if step["action"] == "practice":
            profile = competencies.get(step["competency_code"], {})
            step["resources"] = select_remediation_resources(
                db,
                competency_code=step["competency_code"],
                weak_criteria=profile.get("weak_criteria", []),
                misconceptions=profile.get("misconceptions", []),
                limit=resource_limit,
            )

    return steps[:_MAX_STEPS]


def focus_step(steps: list[dict]) -> dict | None:
    """The single most actionable step, or ``None``."""
    return steps[0] if steps else None
