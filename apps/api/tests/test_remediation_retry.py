"""4E tests — Remediation + Retry.

The immutable evidence pipeline:

    Failed Evidence -> RemediationPlan(evidence_id) -> Retry -> New
    AssessmentAttempt -> New EvidenceRecord -> Mastery Engine.

Rules under test (from the user's spec — "Remediation is not Mastery, and
Retry is not Reset"):

  1. A failing attempt creates a remediation plan.
  2. The plan is *linked to the evidence* that revealed the problem.
  3. A retry creates a NEW AssessmentAttempt (never overwrites the old one).
  4. Old evidence is never modified.
  5. A successful retry passes through the Mastery Engine (never a direct
     ``DEMONSTRATED`` write anywhere).
  6. A failed retry doesn't erase Mastery history.
  7. A student cannot use another student's retry/plan.
  8. An instructor cannot access students outside their sections.
  9. Repeated retries never overwrite Mastery history.
 10. A mid-flow failure rolls the whole attempt+evidence+mastery back.
"""

import json
import time

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.db import SessionLocal, crud, models
from app.main import app
from app.services import mastery_engine, remediation_flow

# --- fixtures ---------------------------------------------------------------


@pytest.fixture(scope="module")
def client():
    """Trigger app startup (create_all_tables + bootstrap) once per module."""
    return TestClient(app)


# --- helpers ----------------------------------------------------------------


def _new_student(uniq: str, university_id: int) -> dict:
    import time as _t

    from app.auth.service import hash_password

    db = SessionLocal()
    try:
        uniq = f"{uniq}_{int(_t.time() * 1000)}"
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
    import time as _t

    from app.auth.service import hash_password

    db = SessionLocal()
    try:
        uniq = f"{uniq}_inst_{int(_t.time() * 1000)}"
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
        return {
            "user_id": user.id,
            "email": user.email,
            "username": user.username,
        }
    finally:
        db.close()


def _login(client: TestClient, email: str) -> str:
    r = client.post("/api/auth/login", json={"email": email, "password": "Str0ng!Pass#word"})
    assert r.status_code == 200, f"login failed: {r.text}"
    return r.json()["access_token"]


def _instructor_token(instructor: dict) -> str:
    """Instructors have no student record, so mint the JWT directly (same
    path the app uses and the admin tests use)."""
    from app.auth.service import create_access_token

    return create_access_token(subject=str(instructor["user_id"]))


def _auth(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def _mec271_pid_tuning(db: Session):
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


def _rubric(db: Session, comp) -> list:
    for a in crud.get_assessments_for_competency(db, competency_id=comp.id):
        if a.kind == "MASTERY":
            return crud.get_rubric(db, assessment_id=a.id)
    raise AssertionError("MASTERY assessment not found")


def _ok(*, overshoot=4.0, settling=1.2, sse=0.005, stable=True) -> dict:
    return {
        "overshoot": overshoot,
        "settling_time": settling,
        "steady_state_error": sse,
        "stable": stable,
    }


def _fail(*, overshoot=20.0, settling=3.0, sse=0.05, stable=False) -> dict:
    return {
        "overshoot": overshoot,
        "settling_time": settling,
        "steady_state_error": sse,
        "stable": stable,
    }


# --- 1: FAIL -> remediation, linked to the triggering evidence --------


def test_failure_creates_remediation_plan(client):
    """A failing attempt creates an open remediation plan (requirement 1)."""
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        student = _new_student("remed_created", univ.id)
        _, comp = _mec271_pid_tuning(db)

        result = remediation_flow.submit_retry(
            db,
            student_id=student["student_id"],
            competency_code=comp.code,
            metrics=_fail(),
        )
        db.commit()
        assert result["level"] != "DEMONSTRATED"
        assert result["remediation_plan_id"] is not None

        plan = crud.get_remediation_plan(db, plan_id=result["remediation_plan_id"])
        assert plan is not None
        assert plan.student_id == student["student_id"]
        assert plan.competency_id == comp.code
        assert plan.status == "open"
        assert plan.created_at is not None
    finally:
        db.close()


def test_remediation_plan_linked_to_correct_evidence(client):
    """The plan references the exact evidence that revealed the problem."""
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        student = _new_student("remed_linked", univ.id)
        _, comp = _mec271_pid_tuning(db)

        result = remediation_flow.submit_retry(
            db,
            student_id=student["student_id"],
            competency_code=comp.code,
            metrics=_fail(),
        )
        db.commit()
        plan = crud.get_remediation_plan(db, plan_id=result["remediation_plan_id"])
        # Linked to the *evidence that revealed the failure* (test #2).
        assert plan.evidence_id == result["evidence_id"]
        codes = json.loads(plan.reason_codes_json)
        assert codes, "reason codes must explain why remediation was offered"

        # Reverse lookup: the evidence's plan stays findable.
        found = crud.get_remediation_plan_for_evidence(db, evidence_id=result["evidence_id"])
        assert found is not None
        assert found.id == plan.id
    finally:
        db.close()


# --- 3 + 4: retry = new attempt; old evidence untouched -------------------


def test_retry_creates_a_new_attempt(client):
    """Retry = a NEW AssessmentAttempt, never a mutation of the old one."""
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        student = _new_student("remed_new_attempt", univ.id)
        _, comp = _mec271_pid_tuning(db)
        assessment = None
        for a in crud.get_assessments_for_competency(db, competency_id=comp.id):
            if a.kind == "MASTERY":
                assessment = a
        assert assessment is not None

        r1 = remediation_flow.submit_retry(
            db, student_id=student["student_id"], competency_code=comp.code, metrics=_fail()
        )
        db.commit()
        r2 = remediation_flow.submit_retry(
            db, student_id=student["student_id"], competency_code=comp.code, metrics=_fail()
        )
        db.commit()

        # Two distinct attempts with sequential numbers.
        assert r1["attempt_number"] == 1
        assert r2["attempt_number"] == 2
        assert r1["attempt_id"] != r2["attempt_id"]

        attempts = crud.get_attempts_for_student(
            db, assessment_id=assessment.id, student_id=student["student_id"]
        )
        assert [a.attempt_number for a in attempts] == [1, 2]
    finally:
        db.close()


def test_old_evidence_is_never_modified(client):
    """Every retry appends a new evidence row; prior evidence stays intact."""
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        student = _new_student("remed_evidence_immut", univ.id)
        _, comp = _mec271_pid_tuning(db)

        r1 = remediation_flow.submit_retry(
            db, student_id=student["student_id"], competency_code=comp.code, metrics=_fail()
        )
        db.commit()
        r2 = remediation_flow.submit_retry(
            db, student_id=student["student_id"], competency_code=comp.code, metrics=_ok()
        )
        db.commit()

        evidence = crud.get_evidence_for_competency(
            db, student_id=student["student_id"], competency_id=comp.id
        )
        assert len(evidence) == 2
        assert [e.id for e in evidence] == [r1["evidence_id"], r2["evidence_id"]]
        # The first record still carries its original failing metrics.
        assert json.loads(evidence[0].metric_json) == _fail()
        assert json.loads(evidence[1].metric_json) == _ok()
    finally:
        db.close()


# --- 5 + 6: successful retry via Mastery Engine; failed retry keeps history -


def test_successful_retry_passes_through_mastery_engine(client):
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        student = _new_student("remed_pass_engine", univ.id)
        _, comp = _mec271_pid_tuning(db)

        r1 = remediation_flow.submit_retry(
            db, student_id=student["student_id"], competency_code=comp.code, metrics=_fail()
        )
        db.commit()
        assert r1["level"] == "NOT_DEMONSTRATED"

        # Successful retry -> the engine records a MasteryRecord with the
        # "all_mandatory_passed" reason. Nothing here writes the level.
        r2 = remediation_flow.submit_retry(
            db, student_id=student["student_id"], competency_code=comp.code, metrics=_ok()
        )
        db.commit()
        assert r2["passed"] is True
        assert r2["passed_count"] == len(_rubric(db, comp))
        assert r2["level"] == "DEMONSTRATED"

        latest = crud.get_latest_mastery(
            db, student_id=student["student_id"], competency_id=comp.id
        )
        assert latest is not None
        assert latest.level == "DEMONSTRATED"
        assert "all_mandatory_passed" in json.loads(latest.reason_codes_json)

        # The open plan was auto-completed on demonstration.
        assert r2["remediation_plan_id"] is None
        for plan in crud.get_remediation_plans_for_student(db, student_id=student["student_id"]):
            assert plan.status == "completed"
            assert plan.completed_at is not None
    finally:
        db.close()


def test_failed_retry_does_not_erase_mastery_history(client):
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        student = _new_student("remed_no_erase", univ.id)
        _, comp = _mec271_pid_tuning(db)

        # Progress then pass (DEVELOPING -> DEMONSTRATED).
        remediation_flow.submit_retry(
            db, student_id=student["student_id"], competency_code=comp.code, metrics=_fail()
        )
        db.commit()
        remediation_flow.submit_retry(
            db, student_id=student["student_id"], competency_code=comp.code, metrics=_ok()
        )
        db.commit()

        before = crud.get_mastery_history(
            db, student_id=student["student_id"], competency_id=comp.id
        )
        assert [h.level for h in before] == ["NOT_DEMONSTRATED", "DEMONSTRATED"]

        # A later failing retry must not downgrade or erase anything
        # (back to NOT_DEMONSTRATED metrics, but highest proven wins).
        r3 = remediation_flow.submit_retry(
            db,
            student_id=student["student_id"],
            competency_code=comp.code,
            metrics=_fail(),
        )
        db.commit()
        assert r3["level"] == "DEMONSTRATED"  # highest proven wins

        after = crud.get_mastery_history(
            db, student_id=student["student_id"], competency_id=comp.id
        )
        assert [h.level for h in after] == ["NOT_DEMONSTRATED", "DEMONSTRATED"]
        assert len(after) == len(before)
    finally:
        db.close()


# --- 7 + 8: RBAC ------------------------------------------------------------


def test_student_cannot_use_another_students_retry_or_plan(client):
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        a = _new_student("remed_rbac_a", univ.id)
        b = _new_student("remed_rbac_b", univ.id)
        _, comp = _mec271_pid_tuning(db)

        result = remediation_flow.submit_retry(
            db, student_id=b["student_id"], competency_code=comp.code, metrics=_fail()
        )
        db.commit()
        other_plan_id = result["remediation_plan_id"]

        # Student A (not the plan owner) cannot complete B's plan —
        # complete_plan rejects foreign students.
        token_a = _login(client, a["email"])
        r = client.post(
            f"/api/retry/me/plans/{other_plan_id}/complete",
            headers=_auth(token_a),
        )
        assert r.status_code == 403  # complete_plan rejects foreign student

        # A's own /me/plans route is self-scoped: it only ever returns A's
        # plans, never B's.
        r = client.get("/api/retry/me/plans", headers=_auth(token_a))
        assert r.status_code == 200
        assert all(p["student_id"] == a["student_id"] for p in r.json())
    finally:
        db.close()


def test_instructor_cannot_access_outside_sections(client):
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        student = _new_student("remed_scope", univ.id)
        instr = _new_instructor("remed_scope", univ.id)
        course, comp = _mec271_pid_tuning(db)

        remediation_flow.submit_retry(
            db, student_id=student["student_id"], competency_code=comp.code, metrics=_fail()
        )
        db.commit()

        # Instructor with no sections for this student -> 403.
        token = _instructor_token(instr)
        r = client.get(f"/api/retry/students/{student['student_id']}/plans", headers=_auth(token))
        assert r.status_code == 403

        # And the review-retry path is gated the same way.
        r = client.post(
            f"/api/retry/students/{student['student_id']}/review",
            json={**_ok(), "competency_code": comp.code},
            headers=_auth(token),
        )
        assert r.status_code == 403

        # Once the student is enrolled in a section the instructor teaches,
        # the same instructor CAN review (still through the Mastery Engine).
        uniq_term = f"{int(time.time())}"
        section = crud.create_section(
            db,
            course_id=course.id,
            term=uniq_term,
            code=f"S{uniq_term}",
            instructor_user_id=instr["user_id"],
        )
        crud.enroll_student_in_section(db, student_id=student["student_id"], section_id=section.id)
        db.commit()
        r = client.get(f"/api/retry/students/{student['student_id']}/plans", headers=_auth(token))
        assert r.status_code == 200
        assert r.json(), "scoped instructor should see the student's plans"
    finally:
        db.close()


# --- 9: repeated retry never overwrites Mastery history ---------------------


def test_repeated_retry_never_overwrites_mastery_history(client):
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        student = _new_student("remed_repeat", univ.id)
        _, comp = _mec271_pid_tuning(db)

        for _ in range(3):
            remediation_flow.submit_retry(
                db, student_id=student["student_id"], competency_code=comp.code, metrics=_fail()
            )
        db.commit()
        history = crud.get_mastery_history(
            db, student_id=student["student_id"], competency_id=comp.id
        )
        # Failing evidence only yields NOT_DEMONSTRATED once; the engine
        # appends on state change only — 1 row, never 3.
        assert [h.level for h in history] == ["NOT_DEMONSTRATED"]

        for _ in range(2):
            remediation_flow.submit_retry(
                db, student_id=student["student_id"], competency_code=comp.code, metrics=_ok()
            )
        db.commit()
        history = crud.get_mastery_history(
            db, student_id=student["student_id"], competency_id=comp.id
        )
        assert [h.level for h in history] == ["NOT_DEMONSTRATED", "DEMONSTRATED"]
    finally:
        db.close()


# --- 10: transaction rollback on Evidence/Mastery failure -------------------


def test_transaction_rolls_back_when_engine_fails(client, monkeypatch):
    """If the Mastery Engine raises mid-flow, the whole retry (attempt,
    item results, evidence) must roll back — nothing is persisted half-way."""
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        student = _new_student("remed_rollback", univ.id)
        _, comp = _mec271_pid_tuning(db)
        assessment = None
        for a in crud.get_assessments_for_competency(db, competency_id=comp.id):
            if a.kind == "MASTERY":
                assessment = a
        assert assessment is not None

        def _boom(*args, **kwargs):
            raise RuntimeError("engine failure")

        monkeypatch.setattr(mastery_engine, "resolve_and_record", _boom)

        with pytest.raises(RuntimeError):
            remediation_flow.submit_retry(
                db, student_id=student["student_id"], competency_code=comp.code, metrics=_ok()
            )
        db.rollback()

        attempts = crud.get_attempts_for_student(
            db, assessment_id=assessment.id, student_id=student["student_id"]
        )
        assert attempts == []
        evidence = crud.get_evidence_for_competency(
            db, student_id=student["student_id"], competency_id=comp.id
        )
        assert evidence == []
        history = crud.get_mastery_history(
            db, student_id=student["student_id"], competency_id=comp.id
        )
        assert history == []
    finally:
        db.close()
