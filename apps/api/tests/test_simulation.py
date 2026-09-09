"""Sprint 7 — Robotics Simulation / Proof Layer e2e tests.

Coverage:
  1. 7A/7B/7C — determinism pins: same task + gains ⇒ bit-identical metrics,
     and the recorded snapshots for the failing / passing gain sets.
  2. 7D/7E — one /api/simulation run routes through the standard evidence
     pipeline: AssessmentAttempt + AttemptItemResult rubric verdicts +
     SimulationRun lineage + EvidenceRecord + resolve_and_record + remediation
     plan (open on FAIL, completed on PASS).
  3. 7F — the coach reads the simulation runs (facts only) and a coaching
     turn never mutates evidence, attempts, or plans.
  4. 7G — the full loop: FAIL → evidence → diagnosis → remediation plan →
     coach turn → PASS → plan completed → mastery DEMONSTRATED.
  5. RBAC: unauthenticated / instructor on /api/simulation is rejected;
     unknown task_id → 404.
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
from app.services.simulation_contract import (
    SIM_FAILING_GAINS,
    SIM_PASSING_GAINS,
    SIMULATION_TASKS,
    simulate_gains,
)

from .test_student_model import _auth, _login, _new_student

_SAFE_REPLY = (
    "Your last run missed the settling-time and SSE criteria. Let's raise the integral gain."
)


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


class _RecordingProvider(MockLLMProvider):
    def __init__(self, config, responses=None):
        super().__init__(config, responses=responses)
        self.seen: list[list] = []

    async def generate(self, messages, **kwargs):
        self.seen.append(list(messages))
        return await super().generate(messages, **kwargs)


def _cfg():
    return LLMConfig(provider_type="mock", model_name="test-sim", base_url="", api_key=None)


def _coach_turn(db: Session, *, student_id: str, message: str, provider) -> dict:
    return asyncio.run(
        coach_engine.run_coach_turn(db, student_id=student_id, message=message, provider=provider)
    )


@pytest.fixture()
def sim_student():
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        assert univ is not None
        fresh = _new_student("sim", univ.id)
        return {"student_id": fresh["student_id"], "email": fresh["email"]}
    finally:
        db.close()


def _counts(student_id: str) -> dict:
    db = SessionLocal()
    try:
        return {
            "runs": db.query(models.SimulationRun)
            .filter(models.SimulationRun.student_id == student_id)
            .count(),
            "evidence": db.query(models.EvidenceRecord)
            .filter(models.EvidenceRecord.student_id == student_id)
            .count(),
            "attempts": db.query(models.AssessmentAttempt)
            .filter(models.AssessmentAttempt.student_id == student_id)
            .count(),
            "plans": db.query(models.RemediationPlan)
            .filter(models.RemediationPlan.student_id == student_id)
            .count(),
        }
    finally:
        db.close()


def _run_sim(client, token: str, **gains) -> dict:
    r = client.post("/api/simulation", json=gains, headers=_auth(token))
    assert r.status_code == 200, f"simulation failed: {r.text}"
    return r.json()


# --- 7A/7B/7C: determinism + contract metrics ----------------------------------------


def test_simulation_is_deterministic():
    task = "pid-001"
    for gains in (SIM_FAILING_GAINS, SIM_PASSING_GAINS):
        first = simulate_gains(task, **gains)
        second = simulate_gains(task, **gains)
        assert first == second, "same task + gains must produce identical metrics"


def test_contract_metrics_pinned_for_known_gain_sets():
    failing = simulate_gains("pid-001", **SIM_FAILING_GAINS)
    # The default gains do NOT meet the MEC271 rubric (ST<=2.0, SSE<=0.01).
    assert failing["overshoot"] == 0.0
    assert failing["settling_time"] == 4.0  # never settled in the 4s horizon
    assert failing["steady_state_error"] > 0.01
    assert failing["stable"] is True
    assert not all(
        [
            failing["overshoot"] <= 10.0,
            failing["settling_time"] <= 2.0,
            failing["steady_state_error"] <= 0.01,
            failing["stable"],
        ]
    )

    passing = simulate_gains("pid-001", **SIM_PASSING_GAINS)
    assert passing["overshoot"] == 0.0
    assert passing["settling_time"] <= 2.0
    assert passing["steady_state_error"] <= 0.01
    assert passing["stable"] is True


def test_contract_task_preset_is_single_source():
    task = SIMULATION_TASKS["pid-001"]
    assert task.competency_code == "pid-tuning"
    assert (task.dt, task.duration) == (0.01, 4.0)


# --- 7D/7E/7G: one failing run -> full evidence pipeline -----------------------------


def test_failing_run_writes_attempt_evidence_run_and_plan(client, sim_student):
    token = _login(client, sim_student["email"])
    sid = sim_student["student_id"]

    r = _run_sim(client, token, **SIM_FAILING_GAINS)
    assert r["result"] == "FAIL"
    assert r["requirements_met"] is False
    assert r["attempt"] == 1
    assert r["attempt_id"] is not None
    assert r["evidence_id"] is not None
    assert r["remediation_plan_id"] is not None
    assert r["mastery_level"] != "DEMONSTRATED"
    assert r["misconception"] == "MISSING_INTEGRAL_ACTION"

    db = SessionLocal()
    try:
        # Durable SimulationRun lineage row.
        run = (
            db.query(models.SimulationRun)
            .filter(models.SimulationRun.student_id == sid)
            .order_by(models.SimulationRun.id.desc())
            .first()
        )
        assert run is not None
        assert (run.kp, run.ki, run.kd) == (
            SIM_FAILING_GAINS["kp"],
            SIM_FAILING_GAINS["ki"],
            SIM_FAILING_GAINS["kd"],
        )
        assert run.competency_id == "pid-tuning" and run.task_id == "pid-001"
        assert run.result == "FAIL" and run.requirements_met is False

        # One SUBMITTED, failed assessment attempt with 4 rubric verdicts.
        attempt = db.get(models.AssessmentAttempt, r["attempt_id"])
        assert attempt is not None
        assert attempt.status == "SUBMITTED"
        assert attempt.passed is False
        item_rows = db.query(models.AttemptItemResult).filter(
            models.AttemptItemResult.attempt_id == attempt.id
        )
        assert item_rows.count() == 4
        assert {row.metric_field for row in item_rows} == {
            "overshoot",
            "settling_time",
            "steady_state_error",
            "stable",
        }
        assert not all(row.passed for row in item_rows)

        # EvidenceRecord source=simulation, metrics in rubric keys.
        evidence = db.get(models.EvidenceRecord, r["evidence_id"])
        assert evidence is not None
        assert evidence.source_type == "simulation"
        assert evidence.source_ref_id == run.id
        import json

        metrics = json.loads(evidence.metric_json)
        assert set(metrics) == {
            "overshoot",
            "settling_time",
            "rise_time",
            "steady_state_error",
            "stable",
        }
        assert json.loads(evidence.context_json)["simulation_run_id"] == run.id

        # Open remediation plan tied to the exact evidence.
        plan = db.get(models.RemediationPlan, r["remediation_plan_id"])
        assert plan is not None
        assert plan.status == "open"
        assert plan.evidence_id == evidence.id
        assert plan.competency_id == "pid-tuning"
    finally:
        db.close()


# --- 7F: coach reads simulation runs; turns never mutate -----------------------------


def test_coach_context_exposes_simulation_runs(client, sim_student):
    token = _login(client, sim_student["email"])
    sid = sim_student["student_id"]
    _run_sim(client, token, **SIM_FAILING_GAINS)

    db = SessionLocal()
    try:
        ctx = coach_context.build_coach_context(
            db, student_id=sid, intent_code="DIAGNOSE", intent_mode="REMEDIATE"
        )
    finally:
        db.close()

    sim = ctx["simulation"]
    assert sim["total_runs"] == 1
    assert sim["latest_result"] == "FAIL"
    latest = sim["latest_run"]
    assert latest["result"] == "FAIL"
    assert latest["competency_code"] == "pid-tuning"
    assert (latest["kp"], latest["ki"], latest["kd"]) == (
        SIM_FAILING_GAINS["kp"],
        SIM_FAILING_GAINS["ki"],
        SIM_FAILING_GAINS["kd"],
    )
    assert latest["steady_state_error"] > 0.01
    assert sim["latest_run"]["run_id"] == latest["run_id"]


def test_coach_turn_is_read_only_over_simulation_state(client, sim_student):
    token = _login(client, sim_student["email"])
    sid = sim_student["student_id"]
    _run_sim(client, token, **SIM_FAILING_GAINS)

    before = _counts(sid)
    provider = _RecordingProvider(_cfg(), responses=[_SAFE_REPLY])

    db = SessionLocal()
    try:
        result = _coach_turn(
            db, student_id=sid, message="What went wrong in my run?", provider=provider
        )
        assert result["guardrail_blocked"] is False
    finally:
        db.close()

    after = _counts(sid)
    assert after == before, "a coach turn must never create runs/evidence/attempts/plans"
    # The guarded system prompt carried the failed run as a fact.
    prompt_text = "\n".join(
        getattr(m, "content", "") or "" for batch in provider.seen for m in batch
    )
    assert "simulation" in prompt_text
    assert '"steady_state_error"' in prompt_text


# --- 7G: FAIL -> ... -> PASS completes the plan and demonstrates mastery -------------


def test_full_loop_fail_to_mastery(client, sim_student):
    token = _login(client, sim_student["email"])
    sid = sim_student["student_id"]

    first = _run_sim(client, token, **SIM_FAILING_GAINS)
    assert first["result"] == "FAIL"
    plan_id = first["remediation_plan_id"]

    # The coach sees the failed run facts (7F) and coaches — evidence unchanged.
    provider = _RecordingProvider(_cfg(), responses=[_SAFE_REPLY])
    db = SessionLocal()
    try:
        _coach_turn(db, student_id=sid, message="Help me fix my tuning.", provider=provider)
    finally:
        db.close()

    second = _run_sim(client, token, **SIM_PASSING_GAINS)
    assert second["result"] == "PASS"
    assert second["requirements_met"] is True
    assert second["attempt"] == 2
    assert second["remediation_plan_id"] is None
    assert second["mastery_level"] == "DEMONSTRATED"

    db = SessionLocal()
    try:
        # The plan opened by the failed run is now completed.
        plan = db.get(models.RemediationPlan, plan_id)
        assert plan is not None
        assert plan.status == "completed"

        # Mastery is recorded by the engine, not hand-written.
        mastery = crud.get_latest_mastery(db, student_id=sid, competency_id=_comp_id(db))
        assert mastery is not None
        assert mastery.level == "DEMONSTRATED"

        # Transfer gate: pid-tuning no longer blocks.
        ctx = coach_context.build_coach_context(
            db, student_id=sid, intent_code="PRACTICE", intent_mode="TRANSITION"
        )
        assert ctx["simulation"]["latest_result"] == "PASS"
        assert ctx["simulation"]["total_runs"] == 2
        assert all(
            b["competency_code"] != "pid-tuning" for b in ctx["transfer"]["blocked_competencies"]
        )
    finally:
        db.close()


def _comp_id(db: Session) -> int:
    course = (
        db.query(models.Course)
        .filter(models.Course.code == "MEC271")
        .order_by(models.Course.id)
        .first()
    )
    comp = crud.get_competency_by_code(db, course_id=course.id, code="pid-tuning")
    assert comp is not None
    return comp.id


# --- RBAC + task contract -------------------------------------------------------------


def test_simulation_requires_student_auth(client):
    r = client.post("/api/simulation", json=SIM_FAILING_GAINS)
    assert r.status_code == 401


def test_simulation_rejects_instructor_token(client, sim_student):
    from app.auth.service import create_access_token

    db = SessionLocal()
    try:
        uniq = f"siminst_{id(db)}"
        user = crud.create_user(
            db,
            email=f"{uniq}@arete.edu.eg",
            username=uniq,
            name=uniq,
            password_hash="x",
            role="instructor",
            university_id=1,
            email_verified=True,
        )
        db.commit()
        token = create_access_token(subject=str(user.id))
    finally:
        db.close()
    r = client.post("/api/simulation", json=SIM_FAILING_GAINS, headers=_auth(token))
    assert r.status_code == 403


def test_simulation_unknown_task_is_404(client, sim_student):
    token = _login(client, sim_student["email"])
    r = client.post(
        "/api/simulation",
        json={"kp": 2.0, "ki": 0.5, "kd": 0.1, "task_id": "no-such-task"},
        headers=_auth(token),
    )
    assert r.status_code == 404
