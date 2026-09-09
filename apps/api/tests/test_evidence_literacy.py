"""Sprint 8 — Evidence-Literacy Loop tests.

The vertical loop under test (every step explainable from evidence):

    students see the narrative (8A) -> claims are stamped with lineage (8B)
    -> the coach suggests actions from the adaptive focus ONLY (8C)
    -> the earliest next step comes from the learning path (8D)
    -> FAIL -> evidence -> remediation -> PASS genuinely changes state (8E)

Coverage:
  1. Narrative is empty before evidence; reads ``evidence_records`` only;
     a coach turn can never create a narrative fact; deterministic.
  2. A DEMONSTRATED claim is stamped with exactly the passing evidence ids,
     source counts, and full lineage.
  3. ``suggested_actions`` are a pure function of the adaptive focus and are
     identical across coach modes (the coach never decides the next step).
  4. ``earliest_next_step`` is the first unproven path step and flips to
     ``ready`` once the evidence supports mastery.
  5. Full loop: FAIL -> plan -> complete -> PASS -> mastery + narrative +
     adaptive state all change deterministically.
  6. RBAC: narrative requires auth; out-of-scope instructors and student
     tokens on instructor routes are rejected.
"""

import asyncio

import pytest
from ai_education.llm.config import LLMConfig
from ai_education.llm.mock import MockLLMProvider
from fastapi.testclient import TestClient

from app.db import SessionLocal, crud
from app.main import app
from app.services import adaptive_engine, coach_context, coach_engine, evidence_narrative
from app.services.simulation_contract import SIM_FAILING_GAINS, SIM_PASSING_GAINS

from .test_student_model import (
    _auth,
    _instructor_token,
    _login,
    _new_instructor,
    _new_student,
)

_SAFE_REPLY = (
    "Your last run missed the settling-time and SSE criteria. Let's raise the integral gain."
)

_MANDATORY = {"overshoot", "settling_time", "steady_state_error", "stable"}


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture()
def lit_student():
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        assert univ is not None
        fresh = _new_student("lit", univ.id)
        return {"student_id": fresh["student_id"], "email": fresh["email"]}
    finally:
        db.close()


def _cfg():
    return LLMConfig(provider_type="mock", model_name="test-8e", base_url="", api_key=None)


def _coach_turn(db, *, student_id, message, reply=_SAFE_REPLY):
    provider = MockLLMProvider(_cfg(), responses=[reply])
    return asyncio.run(
        coach_engine.run_coach_turn(db, student_id=student_id, message=message, provider=provider)
    )


def _run_sim(client, token, **gains):
    r = client.post("/api/simulation", json=gains, headers=_auth(token))
    assert r.status_code == 200, r.text
    return r.json()


def _me(client, token):
    r = client.get("/api/student-model/me", headers=_auth(token))
    assert r.status_code == 200, r.text
    return r.json()


def _path(client, token, code):
    r = client.get(f"/api/student-model/me/path/{code}", headers=_auth(token))
    assert r.status_code == 200, r.text
    return r.json()


def _complete_plan(client, token, plan_id):
    r = client.post(f"/api/retry/me/plans/{plan_id}/complete", headers=_auth(token))
    assert r.status_code == 200, r.text
    return r.json()


def _narrative_lineage(body, code):
    return body["evidence_narrative"]["competencies"][code]["evidence_lineage"]


def _focus(db, student_id):
    sm = coach_context.tool_student_model(db, student_id=student_id)
    return coach_context.tool_adaptive_focus(db, student_model=sm)


# --- 8A: the narrative read model reads evidence_records only ---------------------------


def test_narrative_empty_before_any_evidence(client, lit_student):
    token = _login(client, lit_student["email"])
    body = _me(client, token)

    n = body["evidence_narrative"]
    assert n["total_evidence"] == 0
    assert n["evidence_counts_by_source"] == {}

    pid = n["competencies"]["pid-tuning"]
    assert pid["evidence_lineage"] == []
    assert pid["proven_criteria"] == []
    assert set(pid["unproven_criteria"]) == _MANDATORY


def test_narrative_reads_only_evidence_records(client, lit_student):
    token = _login(client, lit_student["email"])
    sid = lit_student["student_id"]
    fail = _run_sim(client, token, **SIM_FAILING_GAINS)

    body = _me(client, token)
    n = body["evidence_narrative"]
    assert n["total_evidence"] == 1
    assert n["evidence_counts_by_source"] == {"simulation": 1}

    pid = n["competencies"]["pid-tuning"]
    (line,) = pid["evidence_lineage"]
    assert line["evidence_id"] == fail["evidence_id"]
    assert line["source_type"] == "simulation"
    assert line["source_ref_id"] is not None
    assert line["verdict_level"] != "DEMONSTRATED"
    assert {"overshoot", "stable"} <= set(line["passed_criteria"])
    assert "settling_time" in pid["unproven_criteria"]
    assert "steady_state_error" in pid["unproven_criteria"]

    # Deterministic — the same DB state always produces the same narrative.
    db = SessionLocal()
    try:
        sm = coach_context.tool_student_model(db, student_id=sid)
        again = evidence_narrative.build_evidence_narrative(db, student_model=sm)
        assert again["competencies"]["pid-tuning"]["evidence_lineage"] == pid["evidence_lineage"]
    finally:
        db.close()


def test_narrative_is_deterministic_across_reads(client, lit_student):
    token = _login(client, lit_student["email"])
    assert _me(client, token)["evidence_narrative"] == _me(client, token)["evidence_narrative"]


def test_coach_turn_creates_no_narrative_facts(client, lit_student):
    token = _login(client, lit_student["email"])
    sid = lit_student["student_id"]
    _run_sim(client, token, **SIM_FAILING_GAINS)

    before = _me(client, token)["evidence_narrative"]

    db = SessionLocal()
    try:
        _coach_turn(db, student_id=sid, message="Help me fix my tuning.")
    finally:
        db.close()

    assert _me(client, token)["evidence_narrative"] == before


# --- 8B: mastery claims are stamped with their evidence --------------------------------


def test_pass_stamps_the_demonstrated_claim(client, lit_student):
    token = _login(client, lit_student["email"])
    fail = _run_sim(client, token, **SIM_FAILING_GAINS)
    _complete_plan(client, token, fail["remediation_plan_id"])
    passed = _run_sim(client, token, **SIM_PASSING_GAINS)
    assert passed["mastery_level"] == "DEMONSTRATED"

    body = _me(client, token)
    pid = body["competencies"]["pid-tuning"]
    assert pid["mastery_level"] == "DEMONSTRATED"
    assert pid["evidence_ids"] == [fail["evidence_id"], passed["evidence_id"]]
    assert pid["evidence_sources"] == {"simulation": 2}
    # The DEMONSTRATED claim is stamped with exactly the passing evidence(s).
    assert pid["proven_evidence_ids"] == [passed["evidence_id"]]

    n_pid = body["evidence_narrative"]["competencies"]["pid-tuning"]
    assert set(n_pid["proven_criteria"]) == _MANDATORY
    assert n_pid["unproven_criteria"] == []


# --- 8C: the coach can never decide the next step --------------------------------------


def test_actions_for_focus_is_fully_deterministic_and_mode_independent():
    focus_cases = [
        {"action": "start", "competency_code": "pid-fundamentals"},
        {
            "action": "unlock_prerequisite",
            "competency_code": "pid-reasoning",
            "missing_prerequisites": ["pid-fundamentals"],
        },
        {"action": "practice", "competency_code": "pid-tuning", "weak_criteria": ["settling_time"]},
        {"action": "revalidate", "competency_code": "pid-tuning", "confidence": 0.4},
        {"action": "advance", "competency_code": "pid-tuning", "confidence": 0.9},
        {"action": "complete_remediation", "competency_code": "pid-tuning", "plan_id": 7},
        None,
    ]
    for _ in range(2):  # identity across calls — nothing stochastic
        for focus in focus_cases:
            assert coach_engine.actions_for_focus(focus) == coach_engine.actions_for_focus(focus)


def test_coach_suggested_actions_ignore_the_mode(client, lit_student):
    token = _login(client, lit_student["email"])
    sid = lit_student["student_id"]
    _run_sim(client, token, **SIM_FAILING_GAINS)

    db = SessionLocal()
    try:
        focus = _focus(db, sid)
        hint_ctx = coach_context.build_coach_context(
            db, student_id=sid, intent_code="HINT", intent_mode="HINT"
        )
        remediate_ctx = coach_context.build_coach_context(
            db, student_id=sid, intent_code="DIAGNOSE", intent_mode="REMEDIATE"
        )
        assert hint_ctx["focus"] == remediate_ctx["focus"] == focus

        def _turn(ctx):
            provider = MockLLMProvider(_cfg(), responses=[_SAFE_REPLY])
            return asyncio.run(
                coach_engine.run_coach_turn(
                    db, student_id=sid, message="what should I do?", provider=provider, context=ctx
                )
            )

        hint_result = _turn(hint_ctx)
        remediate_result = _turn(remediate_ctx)
        expected = coach_engine.actions_for_focus(focus)
        assert hint_result["suggested_actions"] == expected
        assert remediate_result["suggested_actions"] == expected
    finally:
        db.close()


def test_coach_suggested_actions_track_the_focus_through_the_loop(client, lit_student):
    sid = lit_student["student_id"]

    db = SessionLocal()
    try:
        focus = _focus(db, sid)
        actions = coach_engine.actions_for_focus(focus)
        result = _coach_turn(db, student_id=sid, message="where do I start?")
        assert result["suggested_actions"] == actions
        # Fresh MEC271 student: the retained instrument has no unlocked
        # prerequisite — the focus is simply the first step.
        assert focus["action"] == "start"
        assert focus["competency_code"] == "pid-tuning"
        assert "Begin pid-tuning" in " ".join(actions)
    finally:
        db.close()


# --- 8D: the earliest next step is explainable -----------------------------------------


def test_earliest_next_step_tracks_the_path(client, lit_student):
    token = _login(client, lit_student["email"])

    before = _path(client, token, "pid-tuning")
    assert before["earliest_next_step"]["competency_code"] == "pid-tuning"
    assert before["earliest_next_step"]["reason"] == "not_demonstrated"

    fail = _run_sim(client, token, **SIM_FAILING_GAINS)
    _complete_plan(client, token, fail["remediation_plan_id"])
    _run_sim(client, token, **SIM_PASSING_GAINS)

    after = _path(client, token, "pid-tuning")
    tuning_step = next(s for s in after["path"] if s["competency_code"] == "pid-tuning")
    assert tuning_step["mastery_level"] == "DEMONSTRATED"
    assert tuning_step["status"] == "ready"  # deterministic given the passing evidence
    # The sole path step is now proven — there is no earlier unproven step.
    assert after["earliest_next_step"] is None


# --- 8E: the full vertical loop ---------------------------------------------------------


def test_full_loop_fail_remediate_pass_changes_educational_state(client, lit_student):
    token = _login(client, lit_student["email"])
    sid = lit_student["student_id"]

    before = _me(client, token)
    assert before["attempted_count"] == 0
    assert before["evidence_narrative"]["total_evidence"] == 0

    # FAIL -> evidence + remediation plan.
    fail = _run_sim(client, token, **SIM_FAILING_GAINS)
    assert fail["mastery_level"] != "DEMONSTRATED"
    assert fail["remediation_plan_id"] is not None
    assert fail["attempt"] == 1

    middle = _me(client, token)
    # attempted_count counts competencies with evidence, not attempts.
    assert middle["attempted_count"] == 1
    assert middle["demonstrated_count"] == 0
    assert middle["evidence_narrative"]["total_evidence"] == 1
    assert middle["competencies"]["pid-tuning"]["attempt_count"] == 1
    assert [e["evidence_id"] for e in _narrative_lineage(middle, "pid-tuning")] == [
        fail["evidence_id"]
    ]

    # Remediation is completed, then a PASS demonstrates mastery.
    assert _complete_plan(client, token, fail["remediation_plan_id"])["status"] == "completed"
    passed = _run_sim(client, token, **SIM_PASSING_GAINS)
    assert passed["mastery_level"] == "DEMONSTRATED"
    assert passed["remediation_plan_id"] is None
    assert passed["attempt"] == 2

    after = _me(client, token)
    assert after["attempted_count"] == 1  # still one competency with evidence
    assert after["demonstrated_count"] == 1
    assert after["evidence_narrative"]["total_evidence"] == 2
    assert after["competencies"]["pid-tuning"]["attempt_count"] == 2
    assert after["competencies"]["pid-tuning"]["mastery_level"] == "DEMONSTRATED"

    # Narrative flips to "proven" — from evidence_records only.
    n_after = after["evidence_narrative"]["competencies"]["pid-tuning"]
    assert set(n_after["proven_criteria"]) == _MANDATORY
    assert n_after["unproven_criteria"] == []
    assert {e["evidence_id"] for e in n_after["evidence_lineage"]} == {
        fail["evidence_id"],
        passed["evidence_id"],
    }

    # The system's next step is evidence-driven: the retained instrument is
    # now demonstrated and confident, so the focus is a clean "advance".
    db = SessionLocal()
    try:
        sm = coach_context.tool_student_model(db, student_id=sid)
        steps = adaptive_engine.recommend_next_steps(db, student_model=sm)
        focus = steps[0]
        assert focus["action"] == "advance"
        assert focus["competency_code"] == "pid-tuning"
        assert focus["reason"] == "demonstrated_and_confident"
    finally:
        db.close()


# --- RBAC -------------------------------------------------------------------------------


def test_narrative_requires_student_auth(client):
    assert client.get("/api/student-model/me").status_code == 401


def test_narrative_instructor_scope(client, lit_student):
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        inst = _new_instructor("litinst", univ.id)
        token = _instructor_token(inst)
    finally:
        db.close()

    sid = lit_student["student_id"]
    # An out-of-scope instructor must never read another student's narrative.
    r = client.get(f"/api/student-model/instructors/{sid}/model", headers=_auth(token))
    assert r.status_code == 403


def test_narrative_rejects_student_token_on_instructor_route(client, lit_student):
    token = _login(client, lit_student["email"])
    sid = lit_student["student_id"]
    r = client.get(f"/api/student-model/instructors/{sid}/model", headers=_auth(token))
    assert r.status_code == 403
