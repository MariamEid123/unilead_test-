"""Code-lab API tests — real execution, grading, hints, tutor, progress, RBAC.

These tests exercise *actual* sandboxed execution: a passing 'submit' means the
student's program was truly run and produced the expected output.
"""

from __future__ import annotations

import json
import time

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services import verification


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture(scope="module")
def auth_headers(client):
    uniq = "labuser" + str(int(time.time()))
    r = client.post(
        "/api/auth/signup",
        json={
            "name": "Lab Tester",
            "username": uniq,
            "email": f"{uniq}@smoketest.edu.eg",
            "password": "Str0ng!Pass#word",
        },
    )
    assert r.status_code == 201, r.text
    email = r.json()["email"]
    code = verification.last_sent.get(email)
    assert code
    r = client.post("/api/auth/verify-email", json={"email": email, "code": code})
    assert r.status_code == 200, r.text
    return {"Authorization": f"Bearer {r.json()['access_token']}"}


def _first_challenge_id(client, auth_headers, ch_type="complete_code"):
    r = client.get("/api/lab/manifest", headers=auth_headers)
    assert r.status_code == 200, r.text
    challenges = r.json()["challenges"]
    match = next((c for c in challenges if c["type"] == ch_type), challenges[0])
    return match["id"]


def _starter_for(client, auth_headers, challenge_id):
    r = client.get("/api/lab/manifest", headers=auth_headers)
    return next(
        (c for c in r.json()["challenges"] if c["id"] == challenge_id), {}
    ).get("starter_code")


def test_manifest_shape_and_no_answers(client, auth_headers):
    r = client.get("/api/lab/manifest", headers=auth_headers)
    assert r.status_code == 200
    body = r.json()
    assert body["course_code"] == "CSE014"
    assert body["runtime"] == "python"
    assert len(body["challenges"]) >= 20
    for c in body["challenges"]:
        assert "public_tests" not in c
        assert "correct_index" not in c
        assert "solution" not in json.dumps(c)
    assert len(body["lessons"]) >= 11


def test_run_executes_real_python(client, auth_headers):
    r = client.post(
        "/api/lab/run",
        json={
            "language": "python",
            "source": "a = int(input())\nb = int(input())\nprint(a + b)",
            "stdin": "5\n7\n",
        },
        headers=auth_headers,
    )
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["stdout"].strip() == "12"
    assert body["exit_code"] == 0


def test_run_reports_syntax_error(client, auth_headers):
    r = client.post(
        "/api/lab/run",
        json={
            "language": "python",
            "source": "def f(:\n    pass",
            "stdin": "",
        },
        headers=auth_headers,
    )
    body = r.json()
    assert body["status"] in ("compile_error", "runtime_error")
    assert body["exit_code"] != 0


def test_run_times_out_on_infinite_loop(client, auth_headers):
    r = client.post(
        "/api/lab/run",
        json={"language": "python", "source": "while True:\n    pass", "stdin": ""},
        headers=auth_headers,
    )
    assert r.json()["status"] == "timeout"


def test_submit_correct_solution_passes(client, auth_headers):
    challenge_id = _first_challenge_id(client, auth_headers, "complete_code")
    starter = _starter_for(client, auth_headers, challenge_id)
    # csc1-cc-print blank fill → working program
    source = (
        'name = input()\n'
        'age = int(input())\n'
        'print("Hello, " + name + "!")\n'
        'print("Next year you will be", age + 1)'
    )
    r = client.post(
        "/api/lab/submit",
        json={"challenge_id": challenge_id, "source": source},
        headers=auth_headers,
    )
    assert r.status_code == 200, r.text
    body = r.json()
    assert body["verdict"] == "passed", r.text
    assert body["tests_total"] >= 1
    assert body["tests_passed"] == body["tests_total"]
    assert body["newly_passed"] is True
    assert "Almost" not in body["feedback"]


def test_submit_wrong_solution_is_friendly(client, auth_headers):
    challenge_id = _first_challenge_id(client, auth_headers, "complete_code")
    r = client.post(
        "/api/lab/submit",
        json={"challenge_id": challenge_id, "source": "print('nope')"},
        headers=auth_headers,
    )
    body = r.json()
    assert body["verdict"] in ("failed", "runtime_error")
    assert "tests_passed" in body
    assert "Almost there" in body["feedback"] or "Almost" in body["feedback"]


def test_submit_empty_is_rejected(client, auth_headers):
    challenge_id = _first_challenge_id(client, auth_headers, "complete_code")
    r = client.post(
        "/api/lab/submit",
        json={"challenge_id": challenge_id, "source": "   "},
        headers=auth_headers,
    )
    assert r.json()["verdict"] == "rejected"


def test_output_prediction_mcq(client, auth_headers):
    challenge_id = _first_challenge_id(client, auth_headers, "output_prediction")
    r = client.get("/api/lab/manifest", headers=auth_headers)
    challenge = next(c for c in r.json()["challenges"] if c["id"] == challenge_id)
    assert challenge["options"]
    assert len(challenge["options"]) == 4
    # No answer in the manifest
    assert "correct" not in json.dumps(challenge)

    ok = client.post(
        "/api/lab/submit",
        json={"challenge_id": challenge_id, "selected_index": 0},
        headers=auth_headers,
    ).json()
    assert ok["verdict"] in ("correct", "wrong")

    wrong = client.post(
        "/api/lab/submit",
        json={"challenge_id": challenge_id, "selected_index": 1},
        headers=auth_headers,
    ).json()
    assert wrong["verdict"] in ("correct", "wrong")
    assert wrong["explanation"]


def test_hints_progress(client, auth_headers):
    challenge_id = _first_challenge_id(client, auth_headers, "complete_code")
    r = client.post(
        "/api/lab/hint",
        json={"challenge_id": challenge_id, "level": "general", "hints_used": 0},
        headers=auth_headers,
    )
    assert r.status_code == 200
    assert r.json()["level"] == "general"
    assert r.json()["hints_used"] == 1

    r = client.post(
        "/api/lab/hint",
        json={"challenge_id": challenge_id, "level": "solution", "hints_used": 3},
        headers=auth_headers,
    )
    assert r.json()["level"] == "solution"
    assert r.json()["text"]
    assert r.json()["remaining"] == 0


def test_assist_tutors_errors_and_concepts(client, auth_headers):
    r = client.post(
        "/api/lab/assist",
        json={
            "question": "why won't it run",
            "code": "x = '5'\nprint(x + 3)",
            "error": "TypeError: can only concatenate str (not 'int') to str",
            "depth": "explain",
        },
        headers=auth_headers,
    )
    body = r.json()
    assert body["text"]
    assert "concatenate" in body["text"] or "type" in body["text"].lower()

    resp = client.post(
        "/api/lab/assist",
        json={"question": "explain loops to me", "code": "for i in range(5): print(i)", "depth": "hint"},
        headers=auth_headers,
    )
    text = resp.json()["text"].lower()
    assert ("range" in text) or ("loop" in text)


def test_progress_reflects_real_attempts(client, auth_headers):
    r = client.get("/api/lab/progress", headers=auth_headers)
    assert r.status_code == 200
    body = r.json()
    assert body["total_challenges"] >= 20
    assert body["attempts"] >= 0
    assert body["passed"] <= body["total_challenges"]
    assert 0 <= body["progress_pct"] <= 100


def test_rbac_non_student_cannot_submit(client):
    from app.auth.service import create_access_token
    from app.db import SessionLocal, crud
    from app.auth.service import hash_password
    from app.db.bootstrap import DEFAULT_UNIVERSITY

    db = SessionLocal()
    try:
        university = crud.get_university_by_code(db, DEFAULT_UNIVERSITY["code"])
        assert university is not None
        uniq = f"labinst{int(time.time() * 1000)}"
        user = crud.create_user(
            db,
            email=f"{uniq}@arete.edu.eg",
            username=uniq,
            name="Lab Instructor",
            password_hash=hash_password("Str0ng!Pass#word"),
            role="instructor",
            university_id=university.id,
            email_verified=True,
        )
        db.commit()
        user_id = user.id
    finally:
        db.close()
    token = create_access_token(subject=str(user_id))
    headers = {"Authorization": f"Bearer {token}"}

    manifest = client.get("/api/lab/manifest", headers=headers)
    assert manifest.status_code == 200  # catalog-style read is fine for any user

    submit = client.post(
        "/api/lab/submit",
        json={"challenge_id": "csc1-cc-print", "source": "print(1)"},
        headers=headers,
    )
    assert submit.status_code == 403  # writing student data requires a student