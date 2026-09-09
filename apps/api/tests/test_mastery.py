"""4D tests — the Mastery Engine.

Deterministic, evidence-based mastery resolution. Verifies the core rules:

  - Levels: NOT_DEMONSTRATED < DEVELOPING < DEMONSTRATED.
  - DEMONSTRATED requires ALL mandatory rubric criteria on valid evidence.
  - MasteryRecord is an immutable history: each *state change* appends a row,
    rows are never overwritten or deleted.
  - Number of attempts alone does not decide mastery (a third attempt that
    fails 2/4 does NOT downgrade a proven demonstration).
  - The derived CompetencySnapshot reflects the latest resolved level.
"""

import json

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.db import SessionLocal, crud
from app.db.models import Competency, Course, EvidenceRecord
from app.main import app
from app.services import mastery_engine

# --- fixtures ---------------------------------------------------------------


@pytest.fixture(scope="module")
def client():
    """Trigger app startup (create_all_tables + bootstrap) once per module."""
    return TestClient(app)


# --- helpers ----------------------------------------------------------------


def _new_student(uniq: str, university_id: int) -> dict:
    """Create a verified student using the same pattern as test_admin."""
    import time

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
        }
    finally:
        db.close()


def _mec271_pid_tuning(db: Session) -> Competency:
    course = db.query(Course).filter(Course.code == "MEC271").order_by(Course.id).first()
    assert course is not None, "MEC271 course must exist (bootstrap)"
    comp = crud.get_competency_by_code(db, course_id=course.id, code="pid-tuning")
    assert comp is not None, "pid-tuning competency must exist (bootstrap)"
    return comp


def _rubric_criteria(db: Session, comp: Competency) -> list:
    assessment = None
    for a in crud.get_assessments_for_competency(db, competency_id=comp.id):
        if a.kind == "MASTERY":
            assessment = a
            break
    assert assessment is not None, "MASTERY assessment must exist for pid-tuning"
    return assessment, crud.get_rubric(db, assessment_id=assessment.id)


def _record_evidence(
    db: Session,
    *,
    student_id: str,
    comp: Competency,
    metrics: dict,
    source_ref_id: int,
) -> EvidenceRecord:
    return crud.add_evidence(
        db,
        student_id=student_id,
        competency_id=comp.id,
        source_type="simulation",
        source_ref_id=source_ref_id,
        metric_json=json.dumps(metrics),
        context_json=json.dumps({"kp": 1.0, "ki": 0.1, "kd": 0.05}),
    )


def _pid_metrics(*, overshoot=20.0, settling=3.0, sse=0.05, stable=False) -> dict:
    return {
        "stable": stable,
        "overshoot": overshoot,
        "settling_time": settling,
        "steady_state_error": sse,
        "rise_time": 0.3,
    }


# --- tests ------------------------------------------------------------------


def test_mastery_rules_and_history(client):
    """PID Tuning progression 0/4 -> 3/4 -> 4/4 -> back-to-fail gives
    NOT_DEMONSTRATED -> DEVELOPING -> DEMONSTRATED, and stays there."""
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        student = _new_student("mastery_prog", univ.id)
        comp = _mec271_pid_tuning(db)
        assessment, rubric = _rubric_criteria(db, comp)
        assert len(rubric) == 4
        assert all(r.mandatory for r in rubric)

        sid = student["student_id"]

        # 1) Attempt with 0/4 criteria passing -> NOT_DEMONSTRATED
        _record_evidence(db, student_id=sid, comp=comp, metrics=_pid_metrics(), source_ref_id=1)
        db.commit()
        r1 = mastery_engine.resolve_and_record(db, student_id=sid, competency=comp)
        db.commit()
        assert r1 is not None
        assert r1.level == "NOT_DEMONSTRATED"
        assert "no_criterion_passed" in json.loads(r1.reason_codes_json)

        # 2) Attempt with 3/4 passing -> DEVELOPING
        _record_evidence(
            db,
            student_id=sid,
            comp=comp,
            metrics=_pid_metrics(overshoot=4.0, settling=1.2, sse=0.005, stable=False),
            source_ref_id=2,
        )
        db.commit()
        r2 = mastery_engine.resolve_and_record(db, student_id=sid, competency=comp)
        db.commit()
        assert r2 is not None
        assert r2.level == "DEVELOPING"
        assert any("mandatory_failed" in c for c in json.loads(r2.reason_codes_json))

        # 3) Attempt with 4/4 passing -> DEMONSTRATED (the gate)
        ev3 = _record_evidence(
            db,
            student_id=sid,
            comp=comp,
            metrics=_pid_metrics(overshoot=4.0, settling=1.2, sse=0.005, stable=True),
            source_ref_id=3,
        )
        db.commit()
        r3 = mastery_engine.resolve_and_record(db, student_id=sid, competency=comp)
        db.commit()
        assert r3 is not None
        assert r3.level == "DEMONSTRATED"
        assert "all_mandatory_passed" in json.loads(r3.reason_codes_json)
        assert json.loads(r3.evidence_ids_json) == [ev3.id]

        # 4) A later failing attempt must NOT downgrade (highest proven wins)
        _record_evidence(db, student_id=sid, comp=comp, metrics=_pid_metrics(), source_ref_id=4)
        db.commit()
        r4 = mastery_engine.resolve_and_record(db, student_id=sid, competency=comp)
        db.commit()
        assert r4 is not None
        assert r4.level == "DEMONSTRATED"

        # Immutability: exactly 3 rows, never overwritten.
        history = crud.get_mastery_history(db, student_id=sid, competency_id=comp.id)
        assert [h.level for h in history] == [
            "NOT_DEMONSTRATED",
            "DEVELOPING",
            "DEMONSTRATED",
        ]

        # Derived snapshot reflects latest resolved level.
        from app.db.models import CompetencySnapshot

        ss = (
            db.query(CompetencySnapshot)
            .filter(
                CompetencySnapshot.student_id == sid,
                CompetencySnapshot.competency_id == comp.code,
            )
            .first()
        )
        assert ss is not None
        assert ss.status == "demonstrated"
        assert ss.progress == 100

        # Display-level helper agrees.
        view = mastery_engine.resolve_level_for_display(db, student_id=sid, competency_id=comp.id)
        assert view["level"] == "DEMONSTRATED"
        assert view["evidence_count"] == 4
    finally:
        db.close()


def test_no_evidence_no_mastery(client):
    """No evidence or no rubric -> no mastery assertion is written."""
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        student = _new_student("mastery_none", univ.id)
        comp = _mec271_pid_tuning(db)

        result = mastery_engine.resolve_and_record(
            db, student_id=student["student_id"], competency=comp
        )
        db.commit()
        assert result is None

        history = crud.get_mastery_history(
            db, student_id=student["student_id"], competency_id=comp.id
        )
        assert history == []

        view = mastery_engine.resolve_level_for_display(
            db, student_id=student["student_id"], competency_id=comp.id
        )
        assert view["level"] == "NOT_DEMONSTRATED"
        assert view["evidence_count"] == 0
    finally:
        db.close()


def test_unstable_missing_metric_is_not_proven(client):
    """Missing metric in evidence counts as failed (not proven)."""
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        student = _new_student("mastery_missing", univ.id)
        comp = _mec271_pid_tuning(db)

        # Best possible pid metrics but WITHOUT 'stable' field -> stable fails.
        _record_evidence(
            db,
            student_id=student["student_id"],
            comp=comp,
            metrics=_pid_metrics(overshoot=4.0, settling=1.2, sse=0.005),
            source_ref_id=1,
        )
        db.commit()
        rec = mastery_engine.resolve_and_record(
            db, student_id=student["student_id"], competency=comp
        )
        db.commit()
        assert rec is not None
        assert rec.level == "DEVELOPING"
    finally:
        db.close()


def test_evidence_ids_snapshot_in_record(client):
    """The MasteryRecord stashes its own rubric dump + driving evidence ids."""
    db = SessionLocal()
    try:
        univ = crud.get_university_by_code(db, "ARETE")
        student = _new_student("mastery_trail", univ.id)
        comp = _mec271_pid_tuning(db)

        ev = _record_evidence(
            db,
            student_id=student["student_id"],
            comp=comp,
            metrics=_pid_metrics(),
            source_ref_id=1,
        )
        db.commit()
        rec = mastery_engine.resolve_and_record(
            db, student_id=student["student_id"], competency=comp
        )
        db.commit()
        assert rec is not None
        assert rec.level == "NOT_DEMONSTRATED"

        rubric = json.loads(rec.rubric_json)
        assert len(rubric) == 4
        assert rec.evidence_ids_json == json.dumps([ev.id])
    finally:
        db.close()
