"""Sprint 6 — Compass AI Coach engine contract.

Coverage:
  1. 6A/6D — CoachContext is a faithful, deterministic snapshot of the DB
     (focus, plan ids, evidence counts all match what the DB says).
  2. Orchestration — a safe LLM reply passes through and the guarded system
     prompt carries the verified facts.
  3. 6C — a violating reply is replaced by the deterministic fallback and the
     turn is flagged.
  4. 6E — turns persist as conversation context only.
  5. Read-only guarantee — the coach never touches evidence/mastery/remediation.
  6. 6F — provider selection matrix; the engine itself never instantiates one.
  7. Router RBAC for /api/coach.
"""

import asyncio

import pytest
from ai_education.llm.config import LLMConfig
from ai_education.llm.mock import MockLLMProvider
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.db import SessionLocal, crud, models
from app.main import app
from app.services import coach_context, coach_engine

from .test_student_model import (
    _auth,
    _login,
    _mec271_pid,
    _new_student,
    _submit_retry,
)

_FAIL = {"overshoot": 20.0, "settling_time": 3.0, "steady_state_error": 0.05, "stable": False}
_SAFE_REPLY = "Let's check the overshoot criterion — what do you think changed?"


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


class _RecordingProvider(MockLLMProvider):
    """Mock provider that also records every message batch it saw."""

    def __init__(self, config, responses=None):
        super().__init__(config, responses=responses)
        self.seen: list[list] = []

    async def generate(self, messages, **kwargs):
        self.seen.append(list(messages))
        return await super().generate(messages, **kwargs)


def _cfg():
    return LLMConfig(provider_type="mock", model_name="test-coach", base_url="", api_key=None)


def _run(db: Session, *, student_id: str, message: str, provider, **kwargs) -> dict:
    return asyncio.run(
        coach_engine.run_coach_turn(
            db, student_id=student_id, message=message, provider=provider, **kwargs
        )
    )


@pytest.fixture()
def failing_student():
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        assert univ is not None
        fresh = _new_student("coachfail", univ.id)
        _, comp = _mec271_pid(db)
        _submit_retry(db, fresh["student_id"], comp, _FAIL)
        return {"student_id": fresh["student_id"], "email": fresh["email"]}
    finally:
        db.close()


@pytest.fixture()
def fresh_student():
    """A fresh PHY211 student so the coach surfaces prerequisite unlocks."""
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        assert univ is not None
        fresh = _new_student("coachfresh", univ.id, course_code="PHY211")
        return {"student_id": fresh["student_id"], "email": fresh["email"]}
    finally:
        db.close()


# --- 6A/6D: CoachContext is the DB, faithfully ----------------------------------------


def _context_for(student_id: str, intent: str, mode: str) -> dict:
    db = SessionLocal()
    try:
        return coach_context.build_coach_context(
            db, student_id=student_id, intent_code=intent, intent_mode=mode
        )
    finally:
        db.close()


def test_context_matches_db_for_failing_student(failing_student):
    sid = failing_student["student_id"]
    ctx = _context_for(sid, "DIAGNOSE", "REMEDIATE")

    assert ctx["version"] == "1"
    assert ctx["student_id"] == sid
    assert ctx["course"]["code"] == "MEC271"
    assert ctx["intent"] == {"code": "DIAGNOSE", "mode": "REMEDIATE"}

    focus = ctx["focus"]
    assert focus["action"] == "complete_remediation"
    assert focus["competency_code"] == "pid-tuning"
    assert focus["plan_id"] is not None

    codes = [c["competency_code"] for c in ctx["competencies"]]
    assert codes == sorted(codes)
    # MEC271 carries exactly one competency: the retained PID-Tuning instrument.
    assert codes == ["pid-tuning"]

    # Truthfulness: the plan the coach would reference is really open.
    db = SessionLocal()
    try:
        plan = crud.get_remediation_plan(db, plan_id=focus["plan_id"])
        assert plan is not None
        assert plan.status == "open"
        assert ctx["evidence"]["attempted_count"] == 1
        tuning = next(c for c in ctx["competencies"] if c["competency_code"] == "pid-tuning")
        assert tuning["evidence_count"] == 1
        assert tuning["mastery_level"] == "NOT_DEMONSTRATED"
        assert tuning["remediation_open_count"] == 1
        assert ctx["transfer"]["ready"] is False
        assert ctx["transfer"]["progress"] == "0/1"
    finally:
        db.close()


def test_context_fresh_student_focuses_on_prerequisites(fresh_student):
    ctx = _context_for(fresh_student["student_id"], "TEACH", "LEARN")
    # The physics root (charge-properties) is demonstrated first; the earliest
    # gated competency is charge-quantization.
    assert ctx["focus"]["action"] == "unlock_prerequisite"
    assert ctx["focus"]["competency_code"] == "charge-quantization"
    assert ctx["focus"]["missing_prerequisites"] == ["charge-properties"]

    # No open plans, no evidence, nothing demonstrated → transfer blocked.
    assert ctx["remediation"]["open_count"] == 0
    assert ctx["evidence"]["attempted_count"] == 0
    assert ctx["transfer"]["ready"] is False

    # Learning path targets the adaptive focus competency, deterministically.
    assert ctx["learning_path"]["target"] == "charge-quantization"
    assert ctx["learning_path"]["total_steps"] == 2
    assert ctx["learning_path"]["status"] == "blocked"
    assert ctx["learning_path"]["blockers"] == ["charge-properties"]


# --- Orchestration + 6E ---------------------------------------------------------------


def test_engine_safe_turn_uses_guarded_context_and_persists(failing_student):
    db = SessionLocal()
    try:
        provider = _RecordingProvider(_cfg(), responses=[_SAFE_REPLY])
        result = _run(
            db, student_id=failing_student["student_id"], message="hint please", provider=provider
        )

        assert result["intent"] == "HINT"
        assert result["active_mode"] == "HINT"
        assert result["message"] == _SAFE_REPLY
        assert result["guardrail_blocked"] is False
        assert result["fallback_used"] is False
        assert result["finished"] is False
        assert result["target_competency_id"] == "pid-tuning"

        # The system prompt carried the guarded facts to the model.
        system_msg = provider.seen[0][0]
        assert system_msg.role == "system"
        assert "VERIFIED FACTS" in system_msg.content
        assert "Never give away the answer" in system_msg.content
        assert "pid-tuning" in system_msg.content
        assert provider.seen[0][-1].content == "hint please"

        # 6E: conversation persisted as session context.
        conv = crud.get_latest_conversation(db, failing_student["student_id"])
        assert conv is not None
        assert [m.sender for m in conv.messages] == ["student", "coach"]
        assert conv.messages[-1].text == _SAFE_REPLY
    finally:
        db.close()


def test_engine_continues_existing_conversation(failing_student):
    db = SessionLocal()
    try:
        provider = _RecordingProvider(_cfg(), responses=[_SAFE_REPLY, _SAFE_REPLY])
        _run(db, student_id=failing_student["student_id"], message="first", provider=provider)
        _run(db, student_id=failing_student["student_id"], message="second", provider=provider)

        conv = crud.get_latest_conversation(db, failing_student["student_id"])
        assert conv is not None
        # One conversation reused, four messages total.
        assert len(conv.messages) == 4
        assert [m.sender for m in conv.messages] == [
            "student",
            "coach",
            "student",
            "coach",
        ]
        # The second turn's LLM call saw the previous turns (context, not truth).
        assert provider.seen[1][1].content == "first"  # history user turn
    finally:
        db.close()


# --- 6C -------------------------------------------------------------------------------


def test_engine_blocks_violating_reply(failing_student):
    db = SessionLocal()
    try:
        provider = _RecordingProvider(
            _cfg(), responses=["You have mastered PID! The correct gain is Kp = 2.0."]
        )
        result = _run(
            db,
            student_id=failing_student["student_id"],
            message="what went wrong?",
            provider=provider,
        )

        assert result["guardrail_blocked"] is True
        assert "unearned_mastery_claim" in result["violations"]
        assert "assessment_answer_leak" in result["violations"]
        assert "won't hand you the answer" in result["message"]
        # The violating text never reached the student's history.
        conv = crud.get_latest_conversation(db, failing_student["student_id"])
        assert conv is not None
        assert conv.messages[-1].text == result["message"]
        assert "mastered PID" not in conv.messages[-1].text
    finally:
        db.close()


# --- Read-only guarantee ---------------------------------------------------------------


def test_engine_never_writes_learning_truth(failing_student):
    db = SessionLocal()
    try:
        sid = failing_student["student_id"]
        evidence_before = (
            db.query(models.EvidenceRecord).filter(models.EvidenceRecord.student_id == sid).count()
        )
        mastery_before = (
            db.query(models.MasteryRecord).filter(models.MasteryRecord.student_id == sid).count()
        )

        provider = _RecordingProvider(_cfg(), responses=[_SAFE_REPLY, "bad claim: 5 attempts"])
        _run(db, student_id=sid, message="hi", provider=provider)
        _run(db, student_id=sid, message="hint", provider=provider)

        evidence_after = (
            db.query(models.EvidenceRecord).filter(models.EvidenceRecord.student_id == sid).count()
        )
        mastery_after = (
            db.query(models.MasteryRecord).filter(models.MasteryRecord.student_id == sid).count()
        )
        assert evidence_after == evidence_before
        assert mastery_after == mastery_before

        # The failed retry plan is still open (coach never completes it).
        plan = crud.get_remediation_plan(
            db, plan_id=_context_for(sid, "D", "R")["focus"]["plan_id"]
        )
        assert plan is not None
        assert plan.status == "open"
    finally:
        db.close()


def test_provider_factory_matrix():
    """6F — selection lives in one factory; the engine takes whatever it gets."""
    from ai_education.llm import MockLLMProvider, OllamaProvider, OpenAIProvider

    from app.config import Settings
    from app.main import build_provider

    assert isinstance(build_provider(Settings(llm_provider_type="mock")), MockLLMProvider)
    assert isinstance(build_provider(Settings(llm_provider_type="ollama")), OllamaProvider)
    assert isinstance(build_provider(Settings(llm_provider_type="openai")), OpenAIProvider)


# --- Router / RBAC --------------------------------------------------------------------


def test_router_coach_requires_auth(client):
    r = client.post("/api/coach", json={"message": "hi"})
    assert r.status_code in (401, 403)


def test_router_coach_turn_ok(client, failing_student):
    token = _login(client, failing_student["email"])
    r = client.post("/api/coach", json={"message": "give me a hint"}, headers=_auth(token))
    assert r.status_code == 200
    body = r.json()
    assert body["message"]
    assert body["active_mode"] in ("LEARN", "HINT", "PRACTICE", "REFLECT", "REMEDIATE", "TRANSFER")
    assert body["scaffolding_level"] in ("LOW", "MEDIUM", "HIGH")


def test_router_coach_uses_fallback_when_provider_empty(client, failing_student):
    # Default provider (app.state) has an empty mock queue → engine fallback.
    token = _login(client, failing_student["email"])
    r = client.post("/api/coach", json={"message": "explain overshoot"}, headers=_auth(token))
    assert r.status_code == 200
    assert r.json()["message"]
