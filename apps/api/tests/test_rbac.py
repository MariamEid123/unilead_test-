"""Sprint 4F — RBAC isolation tests for the Sprint 4 surface.

Authorization policy under test:

  - Unauthenticated (missing / invalid / revoked token) -> 401 everywhere.
  - Authenticated but wrong role                     -> 403.
  - Instructor read + action surface is *section-scoped*: an instructor
    can only see/act on students in sections they teach.
  - Out-of-scope but existing student -> 403 (not 404).
  - Genuinely missing resource        -> 404 (not 403).
  - Denied instructor reads are written to the audit trail with
    outcome="DENIED" so violations are reviewable.
  - Student routes are self-scoped by the JWT: a student can never pass
    another student's id anywhere.
"""

import random
import time

import pytest
from fastapi.testclient import TestClient

from app.db import SessionLocal, crud, models
from app.main import app

_FAIL_METRICS = {
    "overshoot": 20.0,
    "settling_time": 3.0,
    "steady_state_error": 0.05,
    "stable": False,
}


def _review_body() -> dict:
    """Body for the instructor ``/review`` route (requires competency_code)."""
    return {**_FAIL_METRICS, "competency_code": "pid-tuning"}


# --- fixtures ---------------------------------------------------------------


@pytest.fixture(scope="module")
def client():
    """Trigger app startup (create_all_tables + bootstrap) once per module."""
    return TestClient(app)


@pytest.fixture(scope="module")
def rbac_org():
    """Two instructors, three students, two sections:

    - section1 taught by `instructor` -> student_a enrolled
    - section2 taught by `second_instructor` -> student_c enrolled
    - student_b exists but is enrolled in no section at all
    """
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        assert univ is not None
        course, _ = _mec271_pid_tuning(db)
        stamp = f"{int(time.time() * 1000)}"

        instructor = _new_instructor("rbac_inst1", univ.id)
        second_instructor = _new_instructor("rbac_inst2", univ.id)
        student_a = _new_student("rbac_a", univ.id)
        student_b = _new_student("rbac_b", univ.id)
        student_c = _new_student("rbac_c", univ.id)

        section1 = crud.create_section(
            db,
            course_id=course.id,
            term=f"T{stamp}",
            code=f"S1-{stamp[-4:]}",
            instructor_user_id=instructor["user_id"],
        )
        section2 = crud.create_section(
            db,
            course_id=course.id,
            term=f"T{stamp}",
            code=f"S2-{stamp[-4:]}",
            instructor_user_id=second_instructor["user_id"],
        )
        db.flush()
        crud.enroll_student_in_section(
            db, student_id=student_a["student_id"], section_id=section1.id
        )
        crud.enroll_student_in_section(
            db, student_id=student_c["student_id"], section_id=section2.id
        )
        db.commit()
    finally:
        db.close()

    return {
        "student_a": student_a,
        "student_b": student_b,
        "student_c": student_c,
        "instructor": instructor,
        "second_instructor": second_instructor,
    }


# --- helpers ----------------------------------------------------------------


def _new_student(uniq: str, university_id: int) -> dict:
    from app.auth.service import hash_password

    db = SessionLocal()
    try:
        uniq = f"{uniq}_{int(time.time() * 1000)}"
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
        }
    finally:
        db.close()


def _new_instructor(uniq: str, university_id: int) -> dict:
    from app.auth.service import hash_password

    db = SessionLocal()
    try:
        uniq = f"{uniq}_inst_{int(time.time() * 1000)}"
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
        return {"user_id": user.id, "email": user.email}
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


def _mec271_pid_tuning(db: SessionLocal):
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


def _missing_sid() -> str:
    """A student id that will never exist in the database."""
    return f"u{random.SystemRandom().randint(10**8, 10**9)}-student"


# --- 401: unauthenticated ---------------------------------------------------


def test_no_token_401_everywhere(client, rbac_org):
    matrix = [
        ("get", "/api/competencies", None),
        ("get", "/api/progress", None),
        ("get", "/api/evidence/me/timeline", None),
        ("get", "/api/retry/me/plans", None),
        ("post", "/api/retry/pid-tuning", _FAIL_METRICS),
        ("get", "/api/instructor/summary", None),
        ("get", "/api/instructor/students", None),
        ("get", "/api/instructor/aggregate", None),
        ("get", f"/api/instructor/students/{rbac_org['student_a']['student_id']}", None),
        ("get", f"/api/evidence/{rbac_org['student_a']['student_id']}/timeline", None),
        ("get", "/api/admin/universities", None),
        ("get", "/api/admin/org", None),
    ]
    for method, url, body in matrix:
        r = client.request(method, url, json=body)
        assert r.status_code == 401, f"{method.upper()} {url} -> {r.status_code}"


def test_bad_or_revoked_token_401(client, rbac_org):
    from app.auth.service import create_access_token

    student = rbac_org["student_a"]
    revoked = create_access_token(subject=str(student["student_user_id"]), token_version=99_999_999)
    for bad in ("not.a.jwt.token", revoked):
        r = client.get("/api/evidence/me/timeline", headers=_auth(bad))
        assert r.status_code == 401, f"token {bad[:12]!r} -> {r.status_code}"


# --- role mismatch ----------------------------------------------------------


def test_student_role_blocked_from_instructor_and_admin(client, rbac_org):
    token = _login(client, rbac_org["student_a"]["email"])
    sid = rbac_org["student_a"]["student_id"]
    for method, url, body in [
        ("get", "/api/instructor/summary", None),
        ("get", "/api/instructor/students", None),
        ("get", f"/api/instructor/students/{sid}", None),
        ("get", f"/api/evidence/{sid}/timeline", None),
        ("post", f"/api/retry/students/{sid}/review", _review_body()),
        ("get", f"/api/retry/students/{sid}/plans", None),
        ("get", "/api/admin/universities", None),
        ("get", "/api/admin/org", None),
    ]:
        r = client.request(method, url, json=body, headers=_auth(token))
        assert r.status_code == 403, f"{method.upper()} {url} -> {r.status_code}"


def test_instructor_role_blocked_from_student_and_admin(client, rbac_org):
    token = _instructor_token(rbac_org["instructor"])
    for method, url, body in [
        ("post", "/api/retry/pid-tuning", _FAIL_METRICS),
        ("get", "/api/retry/me/plans", None),
        ("get", "/api/evidence/me/timeline", None),
        ("get", "/api/admin/universities", None),
        ("get", "/api/admin/org", None),
    ]:
        r = client.request(method, url, json=body, headers=_auth(token))
        assert r.status_code == 403, f"{method.upper()} {url} -> {r.status_code}"


# --- self-scope: students ---------------------------------------------------


def test_student_self_routes_work(client, rbac_org):
    token = _login(client, rbac_org["student_a"]["email"])
    assert client.get("/api/evidence/me/timeline", headers=_auth(token)).status_code == 200
    assert client.get("/api/retry/me/plans", headers=_auth(token)).status_code == 200
    r = client.post("/api/retry/pid-tuning", json=_FAIL_METRICS, headers=_auth(token))
    assert r.status_code == 200, r.text
    body = r.json()
    # The retry created a brand-new attempt + evidence for *this* student,
    # and the level came from the Mastery Engine (failing metrics).
    assert body["attempt_number"] == 1
    assert body["evidence_id"] > 0
    assert body["remediation_plan_id"] is not None
    assert body["level"] == "NOT_DEMONSTRATED"


# --- cross-section instructor isolation -------------------------------------


def test_instructor_scoped_access_ok_for_own_student(client, rbac_org):
    token = _instructor_token(rbac_org["instructor"])
    sid = rbac_org["student_a"]["student_id"]

    detail = client.get(f"/api/instructor/students/{sid}", headers=_auth(token))
    assert detail.status_code == 200, detail.text
    assert detail.json()["student_id"] == sid

    timeline = client.get(f"/api/evidence/{sid}/timeline", headers=_auth(token))
    assert timeline.status_code == 200

    plans = client.get(f"/api/retry/students/{sid}/plans", headers=_auth(token))
    assert plans.status_code == 200


def test_instructor_blocked_outside_their_sections(client, rbac_org):
    token = _instructor_token(rbac_org["instructor"])
    # student_b: exists but enrolled nowhere -> 403 (not 404).
    sid_b = rbac_org["student_b"]["student_id"]
    # student_c: belongs to the *other* instructor's section -> 403.
    sid_c = rbac_org["student_c"]["student_id"]

    for sid in (sid_b, sid_c):
        detail = client.get(f"/api/instructor/students/{sid}", headers=_auth(token))
        assert detail.status_code == 403, f"detail {sid} -> {detail.status_code}"
        timeline = client.get(f"/api/evidence/{sid}/timeline", headers=_auth(token))
        assert timeline.status_code == 403, f"timeline {sid} -> {timeline.status_code}"
        plans = client.get(f"/api/retry/students/{sid}/plans", headers=_auth(token))
        assert plans.status_code == 403, f"plans {sid} -> {plans.status_code}"
        review = client.post(
            f"/api/retry/students/{sid}/review", json=_review_body(), headers=_auth(token)
        )
        assert review.status_code == 403, f"review {sid} -> {review.status_code}"


def test_second_instructor_only_sees_own_section(client, rbac_org):
    second = _instructor_token(rbac_org["second_instructor"])
    sid_c = rbac_org["student_c"]["student_id"]
    sid_a = rbac_org["student_a"]["student_id"]

    assert client.get(f"/api/instructor/students/{sid_c}", headers=_auth(second)).status_code == 200
    assert client.get(f"/api/evidence/{sid_c}/timeline", headers=_auth(second)).status_code == 200
    assert client.get(f"/api/instructor/students/{sid_a}", headers=_auth(second)).status_code == 403
    assert client.get(f"/api/evidence/{sid_a}/timeline", headers=_auth(second)).status_code == 403


def test_missing_student_is_404_not_403(client, rbac_org):
    token = _instructor_token(rbac_org["instructor"])
    missing = _missing_sid()
    assert (
        client.get(f"/api/instructor/students/{missing}", headers=_auth(token)).status_code == 404
    )
    assert client.get(f"/api/evidence/{missing}/timeline", headers=_auth(token)).status_code == 404


# --- retry trace scoping ----------------------------------------------------


def test_plan_trace_scoped_and_missing_plan_404(client, rbac_org):
    token = _instructor_token(rbac_org["instructor"])
    other = _instructor_token(rbac_org["second_instructor"])
    sid_a = rbac_org["student_a"]["student_id"]

    review = client.post(
        f"/api/retry/students/{sid_a}/review", json=_review_body(), headers=_auth(token)
    )
    assert review.status_code == 200, review.text
    plan_id = review.json()["remediation_plan_id"]
    assert plan_id is not None

    # In-scope instructor can trace it.
    assert client.get(f"/api/retry/plans/{plan_id}/trace", headers=_auth(token)).status_code == 200
    # Out-of-scope instructor cannot.
    assert client.get(f"/api/retry/plans/{plan_id}/trace", headers=_auth(other)).status_code == 403
    # Missing plan -> 404.
    assert client.get("/api/retry/plans/999999999/trace", headers=_auth(token)).status_code == 404


# --- denied reads are audited -----------------------------------------------


def test_denied_instructor_read_is_audited(client, rbac_org):
    token = _instructor_token(rbac_org["instructor"])
    sid_b = rbac_org["student_b"]["student_id"]
    before = client.get(f"/api/instructor/students/{sid_b}", headers=_auth(token))
    assert before.status_code == 403

    db = SessionLocal()
    try:
        row = (
            db.query(models.AuditLog)
            .filter(
                models.AuditLog.actor_user_id == rbac_org["instructor"]["user_id"],
                models.AuditLog.action == "instructor_view",
                models.AuditLog.target_id == sid_b,
                models.AuditLog.outcome == "DENIED",
            )
            .order_by(models.AuditLog.id.desc())
            .first()
        )
        assert row is not None, "denied read must be written to the audit trail"
        assert "not in an instructor's section" in row.detail
    finally:
        db.close()
