"""Sprint 5F — transfer readiness.

Deterministic gate that answers *"is this student ready to move on / transfer
credit from course X?"*. A competency is transferable only when:

  - its mastery level is ``DEMONSTRATED``; and
  - its confidence (recency-weighted pass ratio) is at or above a threshold.

Anything below that is reported as a blocker with an exact reason, so the
instructor (and later the AI Coach) sees *why* the bridge is not open yet.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

_log = logging.getLogger("arete.transfer_readiness")

DEMONSTRATED = "DEMONSTRATED"


def compute_transfer_readiness(
    student_model: dict,
    *,
    required_competencies: list[str] | None = None,
    confidence_threshold: float = 0.60,
) -> dict:
    """Transfer readiness for one student across a set of competencies.

    ``required_competencies`` defaults to every competency in the course
    (from the Student Model). Deterministic: competencies are checked in code
    order and reasons are exact.
    """
    competencies = student_model.get("competencies", {})
    codes = sorted(required_competencies or list(competencies.keys()))
    # Only keep codes that exist in the course model.
    codes = [code for code in codes if code in competencies]

    blocked: list[dict] = []
    for code in codes:
        profile = competencies[code]
        level = profile.get("mastery_level", "NOT_DEMONSTRATED")
        confidence = profile.get("confidence", 0.0)
        if level != DEMONSTRATED:
            blocked.append(
                {
                    "competency_code": code,
                    "reason": f"level:{level}",
                }
            )
        elif confidence < confidence_threshold:
            blocked.append(
                {
                    "competency_code": code,
                    "reason": f"confidence_below:{confidence}",
                }
            )

    demonstrated = sum(1 for c in codes if competencies[c]["mastery_level"] == DEMONSTRATED)
    return {
        "course_code": student_model.get("course_code"),
        "ready": len(blocked) == 0,
        "progress": f"{demonstrated}/{len(codes)}",
        "required_competencies": codes,
        "blocked_competencies": blocked,
        "confidence_threshold": confidence_threshold,
    }
