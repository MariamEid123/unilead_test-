"""AI Coach service — runs one turn of the deterministic Compass coach engine.

Keeps the ``/api/coach`` contract stable (via ``CoachResponse``), while the
actual coaching is produced by ``coach_engine.run_coach_turn`` over the
Sprint 5 deterministic layers. The LLM provider never decides what is true;
it only words the coach's reply.
"""

from __future__ import annotations

import logging
from collections import OrderedDict
from typing import TYPE_CHECKING

from fastapi import Request

from ..schemas.coach import CoachResponse
from . import coach_engine, student_state

_log = logging.getLogger("arete.coach")

if TYPE_CHECKING:
    from ai_education.llm.base import LLMProvider


# Track turn indices per student for backwards-compatible UI fields.
# LRU-bounded to prevent unbounded memory growth.
class _BoundedTurnCounters(OrderedDict):
    def __init__(self, maxsize: int = 500):
        super().__init__()
        self._maxsize = maxsize

    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
        super().__setitem__(key, value)
        if len(self) > self._maxsize:
            self.popitem(last=False)


_TURN_COUNTERS: _BoundedTurnCounters = _BoundedTurnCounters()


def _sanitize_log_input(text: str) -> str:
    """Strip control characters and truncate to prevent log injection."""
    clean = "".join(c for c in text if c.isprintable() or c in "\n\t")
    return clean[:200]


def _client_context_summary(context: dict | None) -> str:
    """A short, student-safe summary of the corroborative client context.

    The engine's VERIFIED FACTS never come from here; this exists so the
    wire protocol visibly carries the adaptive context (focus, next step,
    competency, evidence, misconception) on every interaction and the
    evidence timeline records that it was received.
    """
    if not context:
        return "none"
    parts = []
    if context.get("focus"):
        parts.append(f"focus={_sanitize_log_input(str(context['focus']))[:60]}")
    if context.get("earliest_next_step"):
        parts.append(f"next={_sanitize_log_input(str(context['earliest_next_step']))[:60]}")
    comp = context.get("competency")
    if isinstance(comp, dict) and (comp.get("name") or comp.get("id")):
        parts.append(f"competency={comp.get('name') or comp.get('id')}")
    evidence = context.get("evidence")
    if evidence:
        parts.append(f"evidence={len(evidence)} items")
    if context.get("misconception"):
        parts.append(f"misconception={_sanitize_log_input(str(context['misconception']))[:60]}")
    return "; ".join(parts) if parts else "context accepted"


def _next_turn_index(student_id: str) -> int:
    _TURN_COUNTERS[student_id] = _TURN_COUNTERS.get(student_id, 0) + 1
    return _TURN_COUNTERS[student_id]


def _reset_turn_index(student_id: str) -> None:
    _TURN_COUNTERS.pop(student_id, None)


def _resolve_provider(http_request: Request) -> LLMProvider:
    """The shared provider from app.state; falls back to the settings factory.
    The engine stays provider-agnostic (6F) — this is the single place the
    process resolves which concrete provider to use per request."""
    provider = getattr(http_request.app.state, "llm_provider", None)
    if provider is not None:
        return provider
    from ..config import Settings
    from ..main import build_provider  # lazy: main imports the routers

    return build_provider(Settings())


async def process_turn(request_data, http_request: Request, student_id: str) -> dict:
    """Process one coach turn for the given student via the Compass engine."""
    provider = _resolve_provider(http_request)

    from ..db import SessionLocal

    db = SessionLocal()
    try:
        result = await coach_engine.run_coach_turn(
            db,
            student_id=student_id,
            message=request_data.message,
            provider=provider,
            mode_hint=request_data.mode,
            target_competency_code=request_data.competency_id,
        )
    except ValueError:
        _log.exception("Coach turn for unknown student=%s", student_id)
        raise
    finally:
        db.close()

    coach_message = result["message"]
    active_mode = result["active_mode"]
    compass_comp_id = result["target_competency_id"]
    scaffolding = result["scaffolding_level"]
    suggested_actions = list(result["suggested_actions"])
    finished = result["finished"]
    if finished:
        _reset_turn_index(student_id)

    turn_index = _next_turn_index(student_id) - 1

    # Append an evidence timeline event so the Evidence Timeline UI shows
    # the coach interaction. The title and detail stay student-facing and
    # never expose engine-internal mode / scaffolding labels.
    student_state.append_evidence_event(
        student_id=student_id,
        event_type="coach_turn",
        title="Coach conversation",
        detail=(
            f'Student asked: "{_sanitize_log_input(request_data.message[:80])}". '
            f"Coach replied ({len(coach_message)} chars). "
            f"Adaptive context received: {_client_context_summary(request_data.context)}."
        ),
        result="INFO",
        competency_id=compass_comp_id,
    )

    return CoachResponse(
        message=coach_message,
        active_mode=active_mode,
        target_competency_id=compass_comp_id,
        scaffolding_level=scaffolding,
        suggested_actions=suggested_actions,
        turn_index=turn_index,
        total_turns=0,  # free-form, no fixed script length
        finished=finished,
    ).model_dump()
