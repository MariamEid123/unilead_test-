"""Sprint 5C/5D/5E/5F — adaptive engine, learning path, resources, readiness.

Deterministic rule coverage:

  - priority ladder ordering (remediation > prerequisites > practice >
    revalidate > advance > start);
  - 5E resource scoring (competency +3, misconception +2, weak +1) with
    deterministic tie-breaks;
  - 5D learning-path topology, lock/blocker labelling, and unlocking when a
    prerequisite is demonstrated;
  - 5F readiness gate (level==DEMONSTRATED AND confidence >= threshold) with
    exact reasons.

Real-pipeline integration (the ONLY demonstrable competency is pid-tuning,
so prerequisite unlocks are exercised via synthetic PHY211 student models).
"""

import time

import pytest
from fastapi.testclient import TestClient

from app.db import SessionLocal, crud
from app.services import adaptive_engine, learning_path, student_model, transfer_readiness

from .test_student_model import (
    _auth,
    _login,
    _mec271_pid,
    _new_instructor,
    _new_student,
    _submit_retry,
)


@pytest.fixture(scope="module")
def client():
    """Trigger app startup (bootstrap incl. remediation catalog) once."""
    from app.main import app

    return TestClient(app)


# --- fixtures ---------------------------------------------------------------


@pytest.fixture(scope="module")
def adapt_org(client):
    """Instructor + section (fresh student) + the seeded graph handles."""
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        assert univ is not None
        course, _ = _mec271_pid(db)
        student = _new_student("adapt", univ.id)
        instructor = _new_instructor("adapt", univ.id)
        stamp = f"{int(time.time() * 1000)}"
        section = crud.create_section(
            db,
            course_id=course.id,
            term=f"AD-T{stamp}",
            code=f"A{stamp[-4:]}",
            instructor_user_id=instructor["user_id"],
        )
        db.flush()
        crud.enroll_student_in_section(db, student_id=student["student_id"], section_id=section.id)
        db.commit()
    finally:
        db.close()
    return {"student": student, "instructor": instructor}


# --- profile factory (synthetic, mirrors the 5A profile shape) --------------


def _profile(
    *,
    code: str,
    title: str,
    level: str,
    confidence: float = 0.0,
    evidence_count: int = 0,
    weak: list[str] | None = None,
    misconceptions: list[str] | None = None,
    open_plan_id: int | None = None,
    prereqs: list[str] | None = None,
    competency_id: int | None = None,
) -> dict:
    return {
        "competency_code": code,
        "competency_title": title,
        "competency_id": competency_id if competency_id is not None else hash(code) % 1000,
        "mastery_level": level,
        "confidence": confidence,
        "evidence_count": evidence_count,
        "attempt_count": evidence_count,
        "weak_criteria": weak or [],
        "misconceptions": misconceptions or [],
        "remediation_open_count": 1 if open_plan_id is not None else 0,
        "remediation_completed_count": 0,
        "open_plan_id": open_plan_id,
        "prerequisite_codes": prereqs or [],
        "prerequisites_satisfied": False,
    }


def _model(*profiles: dict, course_code: str = "MEC271", course_title: str | None = None) -> dict:
    return {
        "student_id": "synthetic",
        "course_code": course_code,
        "course_title": course_title or (
            "Process Instrumentation & Control" if course_code == "MEC271" else course_code
        ),
        "total_competencies": len(profiles),
        "competencies": {p["competency_code"]: p for p in profiles},
    }


_ROOT = _profile(
    code="feedback-fundamentals", title="Feedback Fundamentals", level="NOT_DEMONSTRATED"
)
_TUNING = _profile(
    code="pid-tuning", title="PID Tuning", level="NOT_DEMONSTRATED", prereqs=["pid-reasoning"]
)


# --- 5C: priority ladder ----------------------------------------------------


def test_rule_open_plan_beats_everything(adapt_org):
    failing = {
        **{
            "competency_code": "pid-tuning",
            "competency_title": "PID Tuning",
            "mastery_level": "NOT_DEMONSTRATED",
        },
        "open_plan_id": 42,
        "weak_criteria": ["overshoot"],
        "misconceptions": ["unstable_gains"],
        "confidence": 0.1,
        "evidence_count": 2,
    }
    comps = {"pid-tuning": failing, "feedback-fundamentals": _ROOT}
    step = adaptive_engine.rule_for_profile(comps, failing)
    assert step["action"] == "complete_remediation"
    assert step["priority"] == adaptive_engine.PRIORITY["complete_remediation"]
    assert step["plan_id"] == 42


def test_rule_missing_prerequisite_before_practice(adapt_org):
    profiling = _profile(
        code="pid-tuning",
        title="PID Tuning",
        level="NOT_DEMONSTRATED",
        weak=["overshoot"],
        misconceptions=["unstable_gains"],
        evidence_count=3,
        prereqs=["pid-reasoning"],
    )
    comps = {
        "pid-tuning": profiling,
        "pid-reasoning": _profile(
            code="pid-reasoning", title="PID Reasoning", level="NOT_DEMONSTRATED"
        ),
    }
    step = adaptive_engine.rule_for_profile(comps, profiling)
    assert step["action"] == "unlock_prerequisite"
    assert step["priority"] == 2
    assert step["missing_prerequisites"] == ["pid-reasoning"]


def test_rule_practice_on_weak_criteria(adapt_org):
    profiling = _profile(
        code="pid-tuning",
        title="PID Tuning",
        level="NOT_DEMONSTRATED",
        weak=["overshoot"],
        misconceptions=["unstable_gains"],
        evidence_count=3,
        prereqs=["pid-reasoning"],
    )
    comps = {
        "pid-tuning": profiling,
        "pid-reasoning": _profile(
            code="pid-reasoning", title="PID Reasoning", level="DEMONSTRATED", confidence=0.9
        ),
    }
    step = adaptive_engine.rule_for_profile(comps, profiling)
    assert step["action"] == "practice"
    assert step["priority"] == 3
    assert step["weak_criteria"] == ["overshoot"]


def test_rule_revalidate_low_confidence(adapt_org):
    demonstrated = _profile(
        code="pid-tuning",
        title="PID Tuning",
        level="DEMONSTRATED",
        confidence=0.4,
        evidence_count=2,
    )
    comps = {"pid-tuning": demonstrated}
    step = adaptive_engine.rule_for_profile(comps, demonstrated)
    assert step["action"] == "revalidate"
    assert step["priority"] == 4


def test_rule_advance_confident(adapt_org):
    demonstrated = _profile(
        code="pid-tuning",
        title="PID Tuning",
        level="DEMONSTRATED",
        confidence=0.9,
        evidence_count=2,
    )
    comps = {"pid-tuning": demonstrated}
    step = adaptive_engine.rule_for_profile(comps, demonstrated)
    assert step["action"] == "advance"
    assert step["priority"] == 5


def test_rule_start_no_evidence(adapt_org):
    step = adaptive_engine.rule_for_profile({"feedback-fundamentals": _ROOT}, _ROOT)
    assert step["action"] == "start"
    assert step["priority"] == 6
    assert step["reason"] == "no_evidence_yet"


def test_recommend_steps_sorted_with_focus(adapt_org):
    transfer = _profile(
        code="charge-transfer",
        title="Charge Transfer",
        level="NOT_DEMONSTRATED",
        misconceptions=["charge_conservation_misunderstood"],
        evidence_count=3,
        prereqs=["charge-units"],
    )
    units = _profile(
        code="charge-units", title="Charge Units", level="DEMONSTRATED", confidence=0.9
    )
    root = _profile(
        code="charge-properties", title="Interaction & The Elementary Charge",
        level="NOT_DEMONSTRATED",
    )
    db = SessionLocal()
    try:
        steps = adaptive_engine.recommend_next_steps(db, _model(transfer, units, root))
    finally:
        db.close()
    priorities = [s["priority"] for s in steps]
    assert priorities == sorted(priorities)
    focus = adaptive_engine.focus_step(steps)
    assert focus["priority"] == priorities[0]
    # The charge-transfer practice step carries catalog resources; others do not.
    practice = next(s for s in steps if s["action"] == "practice")
    assert practice["resources"]
    assert all(s.get("resources") in (None, []) for s in steps if s is not practice)


# --- 5E: resource scoring ---------------------------------------------------


def test_resource_scoring_competency_misconception(adapt_org):
    db = SessionLocal()
    try:
        picks = adaptive_engine.select_remediation_resources(
            db,
            competency_code="charge-transfer",
            weak_criteria=["conservation"],
            misconceptions=["charge_conservation_misunderstood"],
            limit=2,
        )
    finally:
        db.close()
    assert picks, "expected seeded charge-transfer resources"
    assert picks[0]["resource_code"] == "res-transfer-conservation-fix"  # +3 comp, +2 miscon
    assert picks[0]["score"] == 5
    # Physics rows carry no rubric-metric signal, so the second pick is
    # competency-only (tie-break on resource_code).
    assert picks[1]["resource_code"] == "res-transfer-qprimer"  # +3 comp
    assert picks[1]["score"] == 3


def test_resource_scoring_prefix_conversion_misconception(adapt_org):
    db = SessionLocal()
    try:
        picks = adaptive_engine.select_remediation_resources(
            db,
            competency_code="charge-units",
            weak_criteria=[],
            misconceptions=["prefix_misconverted"],
            limit=1,
        )
    finally:
        db.close()
    assert picks and picks[0]["resource_code"] == "res-units-prefix-fix"
    assert picks[0]["score"] == 5  # +3 comp, +2 miscon


# --- 5D: learning path topology ---------------------------------------------


def _all_fresh(db) -> dict:
    """A synthetic Student Model of every PHY211 competency (all fresh).

    Uses the *real* DB competency ids so the graph edges ``build_learning_path``
    reads (mapped through ``competency_id``) resolve to these profiles.
    """
    from app.db.models import Course

    course = db.query(Course).filter(Course.code == "PHY211").order_by(Course.id).first()
    assert course is not None
    competencies = crud.get_competencies_for_course(db, course_id=course.id)
    ids = {c.code: c.id for c in competencies}
    specs = [
        ("charge-properties", "Interaction & The Elementary Charge", []),
        ("charge-quantization", "Charge Quantization", ["charge-properties"]),
        ("charge-units", "Charge Units", ["charge-quantization"]),
        ("charge-transfer", "Charge Transfer", ["charge-units"]),
        ("charging-methods", "Charging Methods", ["charge-properties"]),
    ]
    return _model(
        *(
            _profile(
                code=code,
                title=title,
                level="NOT_DEMONSTRATED",
                prereqs=prereqs,
                competency_id=ids[code],
            )
            for code, title, prereqs in specs
        ),
        course_code="PHY211",
        course_title="Introductory Physics II",
    )


def test_path_blocks_until_prerequisite_demonstrated(adapt_org):
    db = SessionLocal()
    try:
        path = learning_path.build_learning_path(
            db, student_model=_all_fresh(db), target_competency_code="charge-transfer"
        )
    finally:
        db.close()
    assert path["target"] == "charge-transfer"
    assert path["total_steps"] == 4
    codes = [s["competency_code"] for s in path["path"]]
    assert codes == [
        "charge-properties",
        "charge-quantization",
        "charge-units",
        "charge-transfer",
    ]
    assert path["status"] == "blocked"
    assert path["path"][0]["locked"] is False  # charge-properties has no prereqs
    assert path["path"][1]["blocked_by"] == ["charge-properties"]
    assert path["path"][1]["locked"] is True
    assert path["blockers"] == ["charge-properties", "charge-quantization", "charge-units"]


def test_path_unlocks_when_prerequisite_demonstrated(adapt_org):
    db = SessionLocal()
    try:
        model = _all_fresh(db)
        model["competencies"]["charge-properties"]["mastery_level"] = "DEMONSTRATED"
        model["competencies"]["charge-properties"]["confidence"] = 0.9
        path = learning_path.build_learning_path(
            db, student_model=model, target_competency_code="charge-transfer"
        )
    finally:
        db.close()
    quant = path["path"][1]
    assert quant["competency_code"] == "charge-quantization"
    assert quant["locked"] is False  # its single prerequisite is now demonstrated
    assert quant["status"] == "not_started"
    assert path["path"][0]["status"] == "ready"
    assert path["status"] == "blocked"  # charge-units still chains on charge-quantization


def test_path_unknown_target_raises(adapt_org):
    db = SessionLocal()
    try:
        with pytest.raises(ValueError):
            learning_path.build_learning_path(
                db, student_model=_all_fresh(db), target_competency_code="nope"
            )
    finally:
        db.close()


# --- 5F: transfer readiness -------------------------------------------------


def test_readiness_fresh_student_blocked(adapt_org):
    db = SessionLocal()
    try:
        model = student_model.build_student_model(db, student_id=adapt_org["student"]["student_id"])
    finally:
        db.close()
    result = transfer_readiness.compute_transfer_readiness(model)
    assert result["ready"] is False
    # MEC271 carries only the retained pid-tuning instrument.
    assert result["progress"] == "0/1"
    assert len(result["blocked_competencies"]) == 1
    assert all(b["reason"].startswith("level:") for b in result["blocked_competencies"])


def test_readiness_after_successful_demonstration(adapt_org):
    db = SessionLocal()
    try:
        _, comp = _mec271_pid(db)
        _submit_retry(
            db,
            adapt_org["student"]["student_id"],
            comp,
            {"overshoot": 4.0, "settling_time": 1.2, "steady_state_error": 0.005, "stable": True},
        )
        model = student_model.build_student_model(db, student_id=adapt_org["student"]["student_id"])
        result = transfer_readiness.compute_transfer_readiness(model)
    finally:
        db.close()
    # The sole competency of the retained MEC271 course is now demonstrated.
    assert result["ready"] is True
    assert result["progress"] == "1/1"
    assert result["blocked_competencies"] == []


def test_readiness_confidence_threshold(adapt_org):
    low = _profile(
        code="pid-tuning",
        title="PID Tuning",
        level="DEMONSTRATED",
        confidence=0.4,
        evidence_count=3,
    )
    res = transfer_readiness.compute_transfer_readiness(
        _model(low), required_competencies=["pid-tuning"], confidence_threshold=0.60
    )
    assert res["ready"] is False
    assert res["progress"] == "1/1"  # level counts as demonstrated; confidence gates it
    assert res["blocked_competencies"][0]["reason"] == "confidence_below:0.4"

    high = _profile(
        code="pid-tuning",
        title="PID Tuning",
        level="DEMONSTRATED",
        confidence=0.95,
        evidence_count=3,
    )
    res2 = transfer_readiness.compute_transfer_readiness(
        _model(high), required_competencies=["pid-tuning"], confidence_threshold=0.60
    )
    assert res2["ready"] is True
    assert res2["progress"] == "1/1"
    assert res2["blocked_competencies"] == []


# --- real-pipeline integration ----------------------------------------------


def test_adaptive_api_focus_is_remediation_after_failure(client, adapt_org):
    """Real retry (auto plan) surfaces a focused complete_remediation step.

    Uses a *fresh* student so an earlier test in this module (which
    demonstrated the shared module-scoped student) cannot pollute it.
    """
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        fresh = _new_student("focus", univ.id)
        _, comp = _mec271_pid(db)
        _submit_retry(
            db,
            fresh["student_id"],
            comp,
            {"overshoot": 20.0, "settling_time": 3.0, "steady_state_error": 0.05, "stable": False},
        )
        email = fresh["email"]
    finally:
        db.close()

    token = _login(client, email)
    headers = _auth(token)
    r = client.get("/api/student-model/me/adaptive", headers=headers)
    assert r.status_code == 200
    steps = r.json()
    assert steps[0]["action"] == "complete_remediation"
    assert steps[0]["competency_code"] == "pid-tuning"
    assert steps[0]["plan_id"] is not None
