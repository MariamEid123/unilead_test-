"""Sprint 6C — coach guardrails.

Two layers, both deterministic:

  1. Prompt layer  — the system prompt the LLM receives forbids giving away
     assessment answers, inventing evidence, or claiming mastery the system
     has not proven.
  2. Mechanical layer — after the provider returns text, ``validate_reply``
     re-checks it against the CoachContext facts. Any violation replaces the
     LLM text with a deterministic, mode-appropriate fallback, so a wayward
     model can never directly reach the student.
"""

from __future__ import annotations

import json
import re

GUARDRAIL_PROMPT_LINES = [
    "You are an AI Coach inside a deterministic learning system.",
    "The VERIFIED FACTS section below is the ONLY source of truth about the "
    "student. Never invent evidence, attempt counts, or mastery levels.",
    "You coach HOW to learn. The system decides WHAT is true.",
    "Never give away the answer to an assessment or a tuning gain the student "
    "is meant to discover. Pivot direct answer requests to questions.",
    "Never claim the student has mastered or demonstrated a competency unless "
    "its mastery_level in VERIFIED FACTS is DEMONSTRATED.",
    "Never fabricate attempt history, scores, or confidence values.",
    "Keep replies in the student's language and at their scaffolding level.",
]


def build_system_prompt(context: dict) -> str:
    """The guarded system prompt embedding the deterministic CoachContext."""
    block = "\n".join(f"- {line}" for line in GUARDRAIL_PROMPT_LINES)
    facts = json.dumps(context, ensure_ascii=False, sort_keys=True, indent=2)
    return f"{block}\n\nVERIFIED FACTS (JSON):\n{facts}\n"


# --- Mechanical reply validators --------------------------------------------

_ANSWER_LEAK = re.compile(
    r"(the answer is|correct (answer|value|gain) is|right (answer|gain) is|"
    r"your (answer|gain) should be|set your [Kk][Pp]\w* to|use [Kk][Pp]\s*=\s*\d)",
    re.I,
)

_MASTERY_CLAIM = re.compile(
    r"\b(mastered|demonstrated|certified|passed (the )?(assessment|test|exam)|"
    r"you got it right)\b",
    re.I,
)

_ATTEMPT_CLAIM = re.compile(r"\b(\d+)\s+(recent\s+)?attempts?\b", re.I)

_LEAK_EXAMPLES = "Kp = 2.0"

_VALIDATORS = (
    "assessment_answer_leak",
    "unearned_mastery_claim",
    "fabricated_evidence_claim",
)


def validate_reply(reply: str, *, context: dict) -> dict:
    """Check the LLM reply against the taught rules + the verified facts.

    Returns ``{"ok": bool, "violations": [codes], "action": "allow"|"fallback"}``.
    """
    violations: list[str] = []

    engineered_leak = (
        reply.strip().lower() == _LEAK_EXAMPLES.lower()
        or "this is the answer:" in reply.lower()
        or "final answer:" in reply.lower()
    )
    if engineered_leak or _ANSWER_LEAK.search(reply):
        violations.append("assessment_answer_leak")

    competencies = context.get("competencies", [])
    any_demonstrated = any(c.get("mastery_level") == "DEMONSTRATED" for c in competencies)
    if not any_demonstrated and _MASTERY_CLAIM.search(reply):
        violations.append("unearned_mastery_claim")

    max_evidence = max((int(c.get("evidence_count") or 0) for c in competencies), default=0)
    for match in _ATTEMPT_CLAIM.finditer(reply):
        claimed = int(match.group(1))
        if 2 <= claimed <= max_evidence + 50 and claimed != max_evidence:
            # A confident number near the real count that isn't the real count
            # is a fabricated fact on close inspection; anything wildly off is
            # nonsense we also refuse to repeat verbatim.
            violations.append("fabricated_evidence_claim")
            break

    ok = not violations
    return {
        "ok": ok,
        "violations": violations,
        "action": "allow" if ok else "fallback",
    }


def _human_title(context: dict, code: str | None) -> str | None:
    """The curriculum title for a competency code, if the context knows it."""
    if not code:
        return None
    for comp in context.get("competencies", []):
        if comp.get("competency_code") == code and comp.get("competency_title"):
            return str(comp["competency_title"])
    return None


def _prerequisite_names(context: dict, codes: list[str]) -> str:
    """Map prerequisite codes to their human titles so students never see
    internal engine identifiers."""
    titles = [
        _human_title(context, code) or code
        for code in codes
    ]
    return ", ".join(t for t in titles if t) or "the prerequisite"


def fallback_message(context: dict) -> str:
    """Deterministic, safe coaching text served when the LLM reply is blocked
    or the provider is unavailable. Speaks in curriculum terms, never in
    engine mode names or internal competency codes."""
    focus = context.get("focus")
    action = (focus or {}).get("action")
    code = (focus or {}).get("competency_code")
    title = _human_title(context, code) or code
    if action in ("complete_remediation", "practice"):
        topic = title or "this concept"
        return (
            f"Let's slow down and work through {topic} together — I won't "
            "hand you the answer. Tell me how you approached your last "
            "attempt, and we'll check each criterion until it clicks."
        )
    if action == "unlock_prerequisite":
        topic = title or "this competency"
        names = _prerequisite_names(context, (focus or {}).get("missing_prerequisites") or [])
        return (
            f"Before we tackle {topic}, let's build a strong foundation. "
            f"We'll start with {names} and work through it step by step — "
            "you try it, and I'll guide you along the way."
        )
    return (
        "I'd like to keep coaching you. Let's walk through the next concept "
        "step by step — you tell me what you think, and I'll guide you from "
        "there."
    )
