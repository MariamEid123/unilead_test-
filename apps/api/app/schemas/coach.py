"""Schemas for the AI Coach endpoint.

The original mock schema only accepted ``turn_index``; the wired version
accepts an optional ``mode`` (one of the six CoachMode values) and an
optional ``competency_id`` so the orchestrator can build a richer context.
The response now exposes the orchestrator's ``active_mode``,
``scaffolding_level``, and any ``suggested_actions`` — which in Sprint 8C are
produced exclusively by the adaptive focus step (never by the coach mode).
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

# Mirrors ai_education.domain.enums.CoachMode — duplicated here so the
# Compass schema layer doesn't need to import the engine package.
CoachModeLiteral = Literal["LEARN", "HINT", "PRACTICE", "REFLECT", "REMEDIATE", "TRANSFER"]


class CoachRequest(BaseModel):
    """One coach turn from the student."""

    message: str = Field(
        ..., min_length=1, max_length=4000, description="The student's message to the coach."
    )
    mode: CoachModeLiteral | None = Field(
        default=None,
        description=(
            "Optional explicit coach mode. If omitted, the reasoning engine "
            "picks one based on the student's evidence history."
        ),
    )
    competency_id: str | None = Field(
        default=None,
        max_length=64,
        description=(
            "Optional Compass competency id (e.g. 'charge-transfer'). If "
            "omitted, the manager's current target competency is used."
        ),
    )
    context: dict | None = Field(
        default=None,
        description=(
            "Optional client-supplied learning-context snapshot shared by the "
            "UI on every turn: focus, earliest_next_step, competency, "
            "evidence, and misconception. This is corroborative only — it is "
            "recorded on the student's evidence timeline, never injected into "
            "the coach's VERIFIED FACTS, which always come from the database."
        ),
    )


class CoachResponse(BaseModel):
    """The coach's reply after one turn."""

    message: str = Field(..., description="The coach's reply text.")
    active_mode: CoachModeLiteral = Field(..., description="The mode that handled this turn.")
    target_competency_id: str | None = Field(
        default=None,
        description="Compass competency id the coach is currently targeting.",
    )
    scaffolding_level: str | None = Field(
        default=None,
        description="Adaptive scaffolding level (LOW / MEDIUM / HIGH).",
    )
    suggested_actions: list[str] = Field(
        default_factory=list,
        description=(
            "Suggested next actions derived ONLY from the adaptive focus step "
            "(Sprint 8C) — the coach mode never decides what to do next."
        ),
    )
    # Kept for backwards compatibility with the original mock UI — the
    # frontend reads ``turn_index`` and ``finished`` to manage the chat
    # flow. With the real orchestrator there's no script length, so we
    # synthesise these from the conversation size.
    turn_index: int = Field(default=0, description="Current turn index.")
    total_turns: int = Field(
        default=0,
        description=(
            "Total turns in the current scripted flow (0 means free-form, no fixed script)."
        ),
    )
    finished: bool = Field(
        default=False,
        description="True when the coach considers this competency complete.",
    )
