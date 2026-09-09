"""Curriculum catalog API tests — course/module/lesson views + practice grading.

The physics bundle is imported at app bootstrap (``boot_default_organization``),
so these tests assert against PHY211 / its L1 lesson on the shared DB.
"""

import json
import time

import pytest
from fastapi.testclient import TestClient

from app.db import SessionLocal, models
from app.main import app
from app.services import verification


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture(scope="module")
def auth_headers(client):
    uniq = "curric" + str(int(time.time()))
    r = client.post(
        "/api/auth/signup",
        json={
            "name": "Curriculum Test",
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


def _answer_indexes() -> dict[int, int]:
    db = SessionLocal()
    try:
        items = (
            db.query(models.PracticeItem)
            .join(models.Lesson)
            .filter(models.Lesson.code == "L1")
            .all()
        )
        return {
            item.id: int(json.loads(item.answer_json).get("correct_index", -1))
            for item in items
        }
    finally:
        db.close()


def test_courses_list(client, auth_headers):
    r = client.get("/api/curriculum/courses", headers=auth_headers)
    assert r.status_code == 200
    codes = [c["code"] for c in r.json()]
    assert "PHY211" in codes
    phy = next(c for c in r.json() if c["code"] == "PHY211")
    assert phy["module_count"] >= 1
    assert phy["lesson_count"] >= 1


def test_course_detail_tree(client, auth_headers):
    r = client.get("/api/curriculum/courses/PHY211", headers=auth_headers)
    assert r.status_code == 200
    body = r.json()
    assert body["code"] == "PHY211"
    lesson_codes = {
        lesson["code"]
        for module in body["modules"]
        for lesson in module["lessons"]
    }
    assert "L1" in lesson_codes


def test_lesson_detail(client, auth_headers):
    r = client.get("/api/curriculum/lessons/L1", headers=auth_headers)
    assert r.status_code == 200
    body = r.json()
    assert body["title"]
    assert body["objectives"]
    assert body["prerequisites"]
    assert body["course_code"] == "PHY211"
    assert body["module_code"] == "M1"
    comp_codes = {c["code"] for c in body["competencies"]}
    assert "charge-transfer" in comp_codes
    assert body["video_count"] == 2
    assert body["practice_count"] >= 10


def test_lecture_sections(client, auth_headers):
    r = client.get("/api/curriculum/lessons/L1/lecture", headers=auth_headers)
    assert r.status_code == 200
    sections = r.json()
    assert sections
    types = {s["section_type"] for s in sections}
    assert "SUMMARY" not in types
    assert {"TEXT", "FORMULA", "EXAMPLE"} <= types
    ordered = [s["sort_order"] for s in sections]
    assert ordered == sorted(ordered)


def test_summary_sections(client, auth_headers):
    r = client.get("/api/curriculum/lessons/L1/summary", headers=auth_headers)
    assert r.status_code == 200
    types = {s["section_type"] for s in r.json()}
    assert "SUMMARY" in types


def test_videos(client, auth_headers):
    r = client.get("/api/curriculum/lessons/L1/videos", headers=auth_headers)
    assert r.status_code == 200
    videos = r.json()
    assert len(videos) == 2
    assert all(v["metadata"]["objective"] for v in videos)


def test_it001_course_and_materials(client, auth_headers):
    """IT001 is the data-driven IT course; its Materials tab is fed by the API."""
    r = client.get("/api/curriculum/courses/IT001", headers=auth_headers)
    assert r.status_code == 200
    body = r.json()
    assert body["code"] == "IT001"
    lesson_codes = {
        lesson["code"]
        for module in body["modules"]
        for lesson in module["lessons"]
    }
    assert {"IT1", "IT2", "IT3"} <= lesson_codes

    r = client.get("/api/curriculum/courses/IT001/materials", headers=auth_headers)
    assert r.status_code == 200
    materials = r.json()
    assert materials, "IT001 should expose at least one lesson with materials"
    lesson_blocks = {m["lesson_code"] for m in materials}
    assert "IT1" in lesson_blocks
    all_resources = [res for m in materials for res in m["resources"]]
    assert all(res["title"] for res in all_resources)
    assert any(res["external_url"] for res in all_resources)


def test_practice_items_list_hides_answers(client, auth_headers):
    r = client.get("/api/curriculum/lessons/L1/practice", headers=auth_headers)
    assert r.status_code == 200
    items = r.json()
    assert items
    for item in items:
        assert item["options"]
        assert item["level"] in {"UNDERSTAND", "APPLY", "TRANSFER"}
        assert "answer" not in item
        assert "explanation" not in str(item)
        assert "correct_index" not in str(item)


def test_practice_grade_correct_and_wrong(client, auth_headers):
    answers = _answer_indexes()
    assert answers
    item_id, correct_index = next(iter(answers.items()))
    wrong = 0 if correct_index != 0 else 1

    r = client.post(
        f"/api/curriculum/lessons/L1/practice/grade",
        headers=auth_headers,
        json={"item_id": item_id, "selected_index": correct_index},
    )
    assert r.status_code == 200
    assert r.json()["correct"] is True
    assert r.json()["explanation"]

    r = client.post(
        f"/api/curriculum/lessons/L1/practice/grade",
        headers=auth_headers,
        json={"item_id": item_id, "selected_index": wrong},
    )
    assert r.status_code == 200
    assert r.json()["correct"] is False
    assert r.json()["correct_index"] == correct_index


def test_non_student_can_browse_catalog(client, auth_headers):
    """Catalog is university-wide: an admin/instructor must be able to browse it.

    The catalog never requires a Student row, so non-student roles must not 403.
    """
    db = SessionLocal()
    try:
        student = db.query(models.Student).order_by(models.Student.id.desc()).first()
        assert student is not None
        student_user_id = student.user_id
        user = db.query(models.User).filter(models.User.id == student_user_id).first()
        assert user is not None
        user.role = "admin"
        db.commit()
    finally:
        db.close()
    try:
        r = client.get("/api/curriculum/courses", headers=auth_headers)
        assert r.status_code == 200, r.text
        r = client.get("/api/curriculum/courses/PHY211", headers=auth_headers)
        assert r.status_code == 200, r.text
        r = client.get("/api/curriculum/lessons/L1/practice", headers=auth_headers)
        assert r.status_code == 200, r.text
    finally:
        db = SessionLocal()
        try:
            user = db.query(models.User).filter(models.User.id == student_user_id).first()
            if user is not None:
                user.role = "student"
                db.commit()
        finally:
            db.close()


def test_unknown_course_and_lesson_404(client, auth_headers):
    r = client.get("/api/curriculum/courses/NOPE999", headers=auth_headers)
    assert r.status_code == 404
    r = client.get("/api/curriculum/lessons/nope-lesson", headers=auth_headers)
    assert r.status_code == 404


def test_requires_auth(client):
    for path in (
        "/api/curriculum/courses",
        "/api/curriculum/lessons/L1",
        "/api/curriculum/lessons/L1/practice",
    ):
        assert client.get(path).status_code == 401