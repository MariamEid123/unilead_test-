"""Sprint 5A/5B/5G — Student Model contract + API.

The Student Model is *derived on demand* from the immutable evidence
pipeline and the confidence contract is fully deterministic::

    confidence = ( Σ_i λ^i · pass_i ) / ( Σ_i λ^i )   λ = 0.75

where ``pass_i`` is the fraction of mandatory rubric criteria accepted for
evidence i, indexed newest-first.

Rules under test:

  1. ``confidence_from_passes`` — pure contract (recency makes newer wins
     count more; empty history → 0.0).
  2. The derived model reflects *what the rubric proved*, not attempts.
  3. weak_criteria comes from the most recent non-passing evidence.
  4. misconceptions aggregate evidence-context tags by frequency.
  5. remediation counts + open_plan_id come from the plan lifecycle.
  6. prerequisite gates are surfaced (prerequisites_satisfied).
  7. Student API: self-scoped read only; instructor token on /me → 403.
  8. Instructors: in-scope read OK; out-of-scope read → 403 + DENIED audit;
     unknown student → 404; student token on instructor route → 403.
"""

import time

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.db import SessionLocal, crud, models
from app.main import app
from app.services import remediation_flow, student_model


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


# --- helpers ----------------------------------------------------------------


def _new_student(uniq: str, university_id: int, course_code: str = "MEC271") -> dict:
    from app.auth.service import hash_password

    db = SessionLocal()
    try:
        uniq = f"{uniq}_sm_{int(time.time() * 1000)}"
        user = crud.create_user(
            db,
            email=f"{uniq}@arete.edu.eg",
            username=uniq,
            name=uniq.title(),
            password_hash=hash_password("Str0ng!Pass#word"),
            role="student",
            university_id=university_id,
            email_verified=True,
        )
        db.commit()
        student = crud.create_student(
            db,
            student_id=f"u{user.id}-student",
            user_id=user.id,
            display_name=user.name,
            university_id=university_id,
            course_code=course_code,
        )
        db.commit()
        return {
            "student_id": student.student_id,
            "student_user_id": user.id,
            "email": user.email,
            "username": user.username,
        }
    finally:
        db.close()


def _new_instructor(uniq: str, university_id: int) -> dict:
    from app.auth.service import hash_password

    db = SessionLocal()
    try:
        uniq = f"{uniq}_sm_inst_{int(time.time() * 1000)}"
        user = crud.create_user(
            db,
            email=f"{uniq}@arete.edu.eg",
            username=uniq,
            name=uniq.title() + " Instructor",
            password_hash=hash_password("Str0ng!Pass#word"),
            role="instructor",
            university_id=university_id,
            email_verified=True,
        )
        db.commit()
        return {"user_id": user.id, "email": user.email, "username": user.username}
    finally:
        db.close()


def _login(client: TestClient, email: str) -> str:
    r = client.post("/api/auth/login", json={"email": email, "password": "Str0ng!Pass#word"})
    assert r.status_code == 200, f"login failed: {r.text}"
    return r.json()["access_token"]


def _instructor_token(instructor: dict) -> str:
    from app.auth.service import create_access_token

    return create_access_token(subject=str(instructor["user_id"]))


def _auth(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def _mec271_pid(db: Session):
    course = (
        db.query(models.Course)
        .filter(models.Course.code == "MEC271")
        .order_by(models.Course.id)
        .first()
    )
    assert course is not None
    comp = crud.get_competency_by_code(db, course_id=course.id, code="pid-tuning")
    assert comp is not None
    return course, comp


def _submit_retry(db: Session, student_id: str, comp, metrics: dict, context=None):
    """Drive a retry through the real 4E pipeline (new evidence + mastery)."""
    result = remediation_flow.submit_retry(
        db, student_id=student_id, competency_code=comp.code, metrics=metrics, context=context or {}
    )
    db.commit()
    return result


# --- fixtures ---------------------------------------------------------------


@pytest.fixture(scope="module")
def seeded():
    """One pid-tuning student with a known evidence + plan history."""
    db = SessionLocal()
    try:
        university = crud.get_university_by_code(db, "ARETE")
        assert university is not None
        course, _comp = _mec271_pid(db)

        # Users first (nested sessions), then sections/writes on `db`.
        student = _new_student("contract", university.id)
        other = _new_student("outsider", university.id)
        instr = _new_instructor("contract", university.id)
        second_instructor = _new_instructor("contractb", university.id)

        stamp = f"{int(time.time() * 1000)}"
        section_a = crud.create_section(
            db,
            course_id=course.id,
            term=f"SM-T{stamp}",
            code="A",
            instructor_user_id=instr["user_id"],
        )
        # Section B is taught by a DIFFERENT instructor, so `other` is out of
        # scope for the primary instructor (who must get a 403 + DENIED audit).
        section_b = crud.create_section(
            db,
            course_id=course.id,
            term=f"SM-T{stamp}",
            code="B",
            instructor_user_id=second_instructor["user_id"],
        )
        db.flush()
        crud.enroll_student_in_section(
            db, student_id=student["student_id"], section_id=section_a.id
        )
        crud.enroll_student_in_section(db, student_id=other["student_id"], section_id=section_b.id)
        db.commit()

        course_id = course.id
        section_a_id = section_a.id
        section_b_id = section_b.id
    finally:
        db.close()
    return {
        "student": student,
        "other": other,
        "instructor": instr,
        "second_instructor": second_instructor,
        "course_id": course_id,
        "section_a_id": section_a_id,
        "section_b_id": section_b_id,
    }


def _fresh_db_student(uniq: str, course_code: str = "MEC271") -> dict:
    """A *fresh* student (no evidence) inside module-scoped helper so each of
    the rule tests starts from a clean slate."""
    db = SessionLocal()
    try:
        university = crud.get_university_by_code(db, "ARETE")
        return _new_student(uniq, university.id, course_code=course_code)
    finally:
        db.close()


# --- 1. pure confidence contract --------------------------------------------


def test_confidence_empty_history_is_zero():
    assert student_model.confidence_from_passes([]) == 0.0


def test_confidence_single_pass_is_one():
    assert student_model.confidence_from_passes([1.0]) == 1.0


def test_confidence_recency_favors_newer_evidence():
    # Newest evidence (index 0) is weighted λ^0 = 1. A pass on top of
    # earlier fails beats a fail on top of earlier passes.
    l = student_model.LAMBDA  # noqa: E741
    newer_wins = student_model.confidence_from_passes([1.0, 0.0])
    older_wins = student_model.confidence_from_passes([0.0, 1.0])
    assert newer_wins == pytest.approx(1.0 / (1.0 + l))
    assert older_wins == pytest.approx(l / (1.0 + l))
    assert newer_wins > older_wins


def test_confidence_fractional_passes_are_supported():
    # Two evidence rows, newest passes half, older passes fully.
    assert student_model.confidence_from_passes([0.5, 1.0]) == pytest.approx(
        (1.0 * 0.5 + student_model.LAMBDA * 1.0) / (1.0 + student_model.LAMBDA)
    )


# --- 2-6. derived model ------------------------------------------------------


def test_model_empty_student_is_all_not_started(seeded):
    fresh = _fresh_db_student("empty")
    db = SessionLocal()
    try:
        model = student_model.build_student_model(db, student_id=fresh["student_id"])
    finally:
        db.close()
    assert model["student_id"] == fresh["student_id"]
    assert model["course_code"] == "MEC271"
    # MEC271 carries exactly one competency: the retained PID-Tuning instrument.
    assert model["total_competencies"] == 1
    assert model["attempted_count"] == 0
    assert model["demonstrated_count"] == 0
    for p in model["competencies"].values():
        assert p["mastery_level"] == "NOT_DEMONSTRATED"
        assert p["confidence"] == 0.0
        assert p["evidence_count"] == 0


def test_model_reflects_rubric_proof_not_attempts(seeded):
    """A passing retry proves DEMONSTRATED; attempts alone never do."""
    db = SessionLocal()
    try:
        course, comp = _mec271_pid(db)
        fresh = _new_student("proof", crud.get_university_by_code(db, "ARETE").id)
        sid = fresh["student_id"]
        # _ok() metrics: overshoot 4, settling 1.2, sse 0.005, stable.
        _submit_retry(
            db,
            sid,
            comp,
            {"overshoot": 4.0, "settling_time": 1.2, "steady_state_error": 0.005, "stable": True},
        )
        model = student_model.build_student_model(db, student_id=sid)
        p = model["competencies"]["pid-tuning"]
        assert p["mastery_level"] == "DEMONSTRATED"
        assert p["confidence"] == 1.0
        assert p["evidence_count"] == 1
        assert p["attempt_count"] >= 1
        assert p["weak_criteria"] == []

        # Now a failing metric — the newest evidence is partial.
        _submit_retry(
            db,
            sid,
            comp,
            {"overshoot": 20.0, "settling_time": 1.2, "steady_state_error": 0.005, "stable": True},
        )
        model2 = student_model.build_student_model(db, student_id=sid)
        p2 = model2["competencies"]["pid-tuning"]
        # Rubric gate still satisfied by the strongest evidence → DEMONSTRATED.
        assert p2["mastery_level"] == "DEMONSTRATED"
        # But confidence drops because the newest evidence only partially passed.
        assert p2["confidence"] < 1.0
        # Weak criteria surface from the most recent non-passing evidence.
        assert "overshoot" in p2["weak_criteria"]
    finally:
        db.close()


def test_model_weak_criteria_and_misconceptions(seeded):
    db = SessionLocal()
    try:
        _, comp = _mec271_pid(db)
        fresh = _new_student("weak", crud.get_university_by_code(db, "ARETE").id)
        sid = fresh["student_id"]
        # First attempt fails settling_time; context tags the misconception.
        _submit_retry(
            db,
            sid,
            comp,
            {"overshoot": 60.0, "settling_time": 3.5, "steady_state_error": 0.05, "stable": False},
            context={"misconception": "unstable_gains"},
        )
        model = student_model.build_student_model(db, student_id=sid)
        p = model["competencies"]["pid-tuning"]
        assert p["mastery_level"] in ("DEVELOPING", "NOT_DEMONSTRATED")
        assert set(p["weak_criteria"]) == {
            "overshoot",
            "settling_time",
            "steady_state_error",
            "stable",
        }
        assert "unstable_gains" in p["misconceptions"]
        # A remediation plan was auto-created by the 4E pipeline.
        assert p["remediation_open_count"] >= 1
        assert p["open_plan_id"] is not None
        assert p["attempt_count"] >= 1
    finally:
        db.close()


def test_model_remediation_counts_reflect_lifecycle(seeded):
    db = SessionLocal()
    try:
        _, comp = _mec271_pid(db)
        fresh = _new_student("plan", crud.get_university_by_code(db, "ARETE").id)
        sid = fresh["student_id"]
        _submit_retry(
            db,
            sid,
            comp,
            {"overshoot": 50.0, "settling_time": 4.0, "steady_state_error": 0.03, "stable": False},
        )
        plan_id = crud.get_open_remediation_plans(db, student_id=sid, competency_id=comp.code)[0].id
        crud.complete_remediation_plan(db, plan_id=plan_id)
        db.commit()

        model = student_model.build_student_model(db, student_id=sid)
        p = model["competencies"]["pid-tuning"]
        assert p["remediation_completed_count"] >= 1
        assert p["remediation_open_count"] == 0
        assert p["open_plan_id"] is None
    finally:
        db.close()


def test_model_prerequisite_satisfied_flag(seeded):
    db = SessionLocal()
    try:
        # A PHY211-student course resolves to the physics graph; MEC271's
        # retained instrument has no prerequisites.
        fresh = _fresh_db_student("prereq", course_code="PHY211")
        model = student_model.build_student_model(db, student_id=fresh["student_id"])
        # charge-transfer requires charge-units. Nothing demonstrated → false.
        p_transfer = model["competencies"]["charge-transfer"]
        assert p_transfer["prerequisite_codes"] == ["charge-units"]
        assert p_transfer["prerequisites_satisfied"] is False
        # charge-properties is the graph root: no prerequisites.
        assert model["competencies"]["charge-properties"]["prerequisites_satisfied"] is True
    finally:
        db.close()


# --- 7-8. API + RBAC --------------------------------------------------------


def test_api_self_model_and_role_policy(client, seeded):
    token = _login(client, seeded["student"]["email"])
    r = client.get("/api/student-model/me", headers=_auth(token))
    assert r.status_code == 200
    body = r.json()
    assert body["student_id"] == seeded["student"]["student_id"]
    assert body["course_code"] == "MEC271"
    # MEC271 carries exactly one competency: the retained PID-Tuning instrument.
    assert set(body["competencies"]) == {"pid-tuning"}

    # Instructor token on the student route → 403 (Sprint 4F policy).
    itok = _instructor_token(seeded["instructor"])
    r2 = client.get("/api/student-model/me", headers=_auth(itok))
    assert r2.status_code == 403


def test_api_instructor_scope_policy(client, seeded):
    itok = _instructor_token(seeded["instructor"])

    # In-scope (enrolled in section A) → OK.
    r = client.get(
        f"/api/student-model/instructors/{seeded['student']['student_id']}/model",
        headers=_auth(itok),
    )
    assert r.status_code == 200
    assert r.json()["student_id"] == seeded["student"]["student_id"]

    # Out-of-scope (section B) → 403 + DENIED audit row.
    r2 = client.get(
        f"/api/student-model/instructors/{seeded['other']['student_id']}/model",
        headers=_auth(itok),
    )
    assert r2.status_code == 403

    db = SessionLocal()
    try:
        denied = (
            db.query(models.AuditLog)
            .filter(
                models.AuditLog.actor_user_id == seeded["instructor"]["user_id"],
                models.AuditLog.outcome == "DENIED",
                models.AuditLog.detail.contains("student model"),
                models.AuditLog.target_id == seeded["other"]["student_id"],
            )
            .order_by(models.AuditLog.id.desc())
            .first()
        )
        assert denied is not None, "DENIED audit row missing"
    finally:
        db.close()

    # Unknown student → 404 (resource genuinely missing, not scope).
    r3 = client.get(
        "/api/student-model/instructors/sm-unknown-student/model",
        headers=_auth(itok),
    )
    assert r3.status_code == 404

    # A student token on an instructor route → 403.
    stok = _login(client, seeded["student"]["email"])
    r4 = client.get(
        f"/api/student-model/instructors/{seeded['student']['student_id']}/model",
        headers=_auth(stok),
    )
    assert r4.status_code == 403


def test_api_adaptive_path_readiness_endpoints(client, seeded):
    token = _login(client, seeded["student"]["email"])
    h = _auth(token)

    r = client.get("/api/student-model/me/adaptive", headers=h)
    assert r.status_code == 200
    steps = r.json()
    assert isinstance(steps, list)
    # No evidence yet → the retained instrument has no prerequisites to
    # unlock, so the only step is "start". Priorities stay non-decreasing.
    actions = [s["action"] for s in steps]
    assert actions == ["start"]
    assert all(steps[i]["priority"] <= steps[i + 1]["priority"] for i in range(len(steps) - 1))
    # The focus step is the highest-priority intervention.
    assert steps[0]["priority"] == min(s["priority"] for s in steps)

    r2 = client.get("/api/student-model/me/path/pid-tuning", headers=h)
    assert r2.status_code == 200
    path = r2.json()
    assert path["target"] == "pid-tuning"
    # MEC271 now carries only the retained PID-Tuning instrument (1 node).
    assert path["path"][0]["competency_code"] == "pid-tuning"
    assert path["path"][-1]["competency_code"] == "pid-tuning"
    assert path["total_steps"] == 1

    r3 = client.get("/api/student-model/me/readiness", headers=h)
    assert r3.status_code == 200
    ready = r3.json()
    assert ready["ready"] is False
    assert ready["progress"] == "0/1"
    # Every competency in the course is blocked (no evidence anywhere).
    assert {b["competency_code"] for b in ready["blocked_competencies"]} == {"pid-tuning"}
    assert all(b["reason"].startswith("level:") for b in ready["blocked_competencies"])

    # Invalid target competency → 404.
    r4 = client.get("/api/student-model/me/path/nope", headers=h)
    assert r4.status_code == 404


def test_api_instructor_adaptive_and_readiness(client, seeded):
    itok = _instructor_token(seeded["instructor"])
    sid = seeded["student"]["student_id"]

    r = client.get(f"/api/student-model/instructors/{sid}/adaptive", headers=_auth(itok))
    assert r.status_code == 200
    actions = [s["action"] for s in r.json()]
    # No evidence yet → the sole retained competency offers only "start".
    assert actions == ["start"]

    r2 = client.get(f"/api/student-model/instructors/{sid}/readiness", headers=_auth(itok))
    assert r2.status_code == 200
    assert r2.json()["ready"] is False
