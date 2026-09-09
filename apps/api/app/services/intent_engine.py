"""Sprint 6B — deterministic coach intent engine.

The student's turn is classified into one of six teaching intents. The
classification is keyword-driven and, when no keyword matches, driven by the
deterministic adaptive focus — the LLM never chooses its own intent, so the
*what to coach* decision stays in the education core.

Intents and their screen mode:

    TEACH      -> LEARN      (teach the concept)
    HINT       -> HINT       (a single small hint)
    DIAGNOSE   -> REMEDIATE  (say why the last attempt failed)
    REMEDIATE  -> REMEDIATE  (rebuild the foundational concept)
    REFLECT    -> REFLECT    (summarise what was learned)
    TEACH_BACK -> TRANSFER   (verify transfer / teach it back)

A legacy ``mode`` from the CoachRequest may be supplied as an explicit hint
and is mapped onto the intent set deterministically.
"""

from __future__ import annotations

import re

Intent = str  # one of TEACH | HINT | DIAGNOSE | REMEDIATE | REFLECT | TEACH_BACK

TEACH = "TEACH"
HINT = "HINT"
DIAGNOSE = "DIAGNOSE"
REMEDIATE = "REMEDIATE"
REFLECT = "REFLECT"
TEACH_BACK = "TEACH_BACK"

INTENTS = (TEACH, HINT, DIAGNOSE, REMEDIATE, REFLECT, TEACH_BACK)

# Intent -> active coach mode (matches the existing CoachModeLiteral surface).
MODE_BY_INTENT = {
    TEACH: "LEARN",
    HINT: "HINT",
    DIAGNOSE: "REMEDIATE",
    REMEDIATE: "REMEDIATE",
    REFLECT: "REFLECT",
    TEACH_BACK: "TRANSFER",
}

# Legacy CoachMode hints -> intent (mode is an explicit human choice).
MODE_HINT_TO_INTENT = {
    "LEARN": TEACH,
    "HINT": HINT,
    "REMEDIATE": REMEDIATE,
    "REFLECT": REFLECT,
    "TRANSFER": TEACH_BACK,
    "PRACTICE": TEACH,  # practice prompts are teach-first questions
}

# Keyword rules, in priority order — first regex hit wins.
# Specific signals (teach-back, remediate) outrank the generic teach verbs,
# because "teach it back …" and "review the concept …" contain teach words.
_KEYWORD_RULES: list[tuple[re.Pattern, str]] = [
    (
        re.compile(r"teach.{0,6}back|in my own words|explain back|\bverify\b|test me", re.I),
        TEACH_BACK,
    ),
    (
        re.compile(
            r"\bremediat\w*|review (the )?(concept|material)|redo|go back|\bbasics\b",
            re.I,
        ),
        REMEDIATE,
    ),
    (re.compile(r"\bhint\b|\bstuck\b|\bclue\b|help me (start|begin)", re.I), HINT),
    (
        re.compile(
            r"\bdiagnos|why did i fail|what went wrong|\bwent wrong\b|\bmistake\b|where did i", re.I
        ),
        DIAGNOSE,
    ),
    (
        re.compile(
            r"\bteach\b|\bexplain\b|\bwhat is\b|\bwhat's\b|\bconcept\b|\bhow does\b|\bunderstand\b",
            re.I,
        ),
        TEACH,
    ),
    (re.compile(r"\breflect\b|\bsummari|\bwhat did i learn\b|\brecap\b|\bwrap", re.I), REFLECT),
]


def intent_from_mode(mode: str | None) -> str | None:
    """Deterministic mapping of a legacy CoachMode (explicit user choice)."""
    if mode is None:
        return None
    return MODE_HINT_TO_INTENT.get(mode.upper())


def _focus_fallback_intent(focus: dict | None) -> str:
    """Map the deterministic adaptive focus to an intent when no keyword hit."""
    if focus is None:
        return TEACH
    action = focus.get("action")
    if action in ("complete_remediation", "practice", "revalidate"):
        return DIAGNOSE
    if action == "unlock_prerequisite":
        return TEACH
    return TEACH


def resolve_intent(
    message: str,
    *,
    focus: dict | None = None,
    explicit_intent: str | None = None,
    mode_hint: str | None = None,
) -> str:
    """Classify one student turn.

    Precedence: explicit intent > legacy mode hint > keyword rules > focus.
    """
    if explicit_intent is not None:
        return explicit_intent.upper()
    mode_intent = intent_from_mode(mode_hint)
    if mode_intent is not None:
        return mode_intent
    for pattern, intent in _KEYWORD_RULES:
        if pattern.search(message):
            return intent
    return _focus_fallback_intent(focus)
