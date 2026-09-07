"""Regression tests for JWT-scoped, course-specific lecture progress."""

import time

from fastapi.testclient import TestClient

from app.main import app
from app.services import verification


def _create_verified_user(client: TestClient, prefix: str) -> dict:
    email = f"{prefix}@courseprogress.edu.eg"
    response = client.post(
        "/api/auth/signup",
        json={
            "name": prefix,
            "username": prefix,
            "email": email,
            "password": "Str0ng!Pass#word",
        },
    )
    assert response.status_code == 201, response.text
    verify = client.post(
        "/api/auth/verify-email",
        json={"email": email, "code": verification.last_sent[email]},
    )
    assert verify.status_code == 200, verify.text
    return {"Authorization": f"Bearer {verify.json()['access_token']}"}


def test_course_progress_is_separate_and_jwt_scoped() -> None:
    client = TestClient(app)
    stamp = str(time.time_ns())
    user_a = _create_verified_user(client, f"coursea{stamp}")
    user_b = _create_verified_user(client, f"courseb{stamp}")

    assert client.get("/api/progress").status_code == 401
    initial = client.get("/api/progress", headers=user_a)
    assert initial.status_code == 200
    assert {course["course_id"] for course in initial.json()["courses"]} == {"physics", "math-zero"}

    physics = client.post("/api/progress/lectures/introduction-to-physics", headers=user_a)
    assert physics.status_code == 200
    assert physics.json()["course_id"] == "physics"
    assert physics.json()["completed_lectures"] == 1

    # Replaying completion is idempotent because user_id + lecture_id is unique.
    replay = client.post("/api/progress/lectures/introduction-to-physics", headers=user_a)
    assert replay.json()["completed_lectures"] == 1
    math = client.post("/api/progress/lectures/numbers-and-operations", headers=user_a)
    assert math.json()["course_id"] == "math-zero"
    assert math.json()["completed_lectures"] == 1

    summary = client.get("/api/progress", headers=user_a).json()
    assert summary["last_active_course"] == "math-zero"
    assert summary["last_lecture"] == "numbers-and-operations"
    assert client.get("/api/progress/physics", headers=user_b).json()["completed_lectures"] == 0
    assert client.get("/api/progress/not-a-course", headers=user_a).status_code == 404
    assert client.post("/api/progress/lectures/not-a-lecture", headers=user_a).status_code == 404
