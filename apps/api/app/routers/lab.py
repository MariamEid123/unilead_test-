"""Code-lab API.

The lab is a first-class learning loop, not an LMS viewer: students run,
submit, get graded on *real* sandboxed execution, are coached with progressive
hints, and the progress endpoint reflects actual attempts. All grader answers
(solutions, test inputs, MCQ indexes) live server-side and never ship in the
manifest view.
"""

from __future__ import annotations

import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..auth.dependencies import get_current_student, get_current_user
from ..db import SessionLocal
from ..db.models import User
from ..schemas.lab import (
    LabAssistRequest,
    LabAssistResult,
    LabHintRequest,
    LabHintResult,
    LabLesson,
    LabManifest,
    LabProgressResponse,
    LabRunRequest,
    LabRunResult,
    LabRuntime,
    LabSubmitRequest,
    LabSubmitResult,
)
from ..services import code_executor, lab_assist, lab_content, lab_service

router = APIRouter(prefix="/api/lab", tags=["lab"])
_log = logging.getLogger("arete.lab")


def _with_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def _public_challenge(challenge: dict) -> dict:
    """Manifest view — client never sees solutions, tests, or answer indexes."""
    return {
        "id": challenge["id"],
        "lesson_code": challenge["lesson_code"],
        "type": challenge["type"],
        "topic": challenge["topic"],
        "difficulty": challenge["difficulty"],
        "title": challenge["title"],
        "prompt": challenge["prompt"],
        "starter_code": challenge.get("starter_code"),
        "code_text": challenge.get("code_text"),
        "options": challenge.get("options"),
        "lesson_title": lab_content.lesson_title(challenge["lesson_code"]),
    }


@router.get("/runtimes", response_model=list[LabRuntime])
def runtimes(_: User = Depends(get_current_user)):
    return [
        {
            "language": "python",
            "available": True,
            "label": code_executor.runtime_label(),
        }
    ]


@router.get("/lessons", response_model=list[LabLesson])
def lessons(_: User = Depends(get_current_user)):
    return lab_content.all_lessons()


@router.get("/manifest", response_model=LabManifest)
def manifest(_: User = Depends(get_current_user)):
    challenges = [_public_challenge(c) for c in lab_content.CHALLENGES]
    return {
        "course_code": lab_content.COURSE_CODE,
        "course_title": lab_content.COURSE_TITLE,
        "runtime": lab_content.RUNTIME,
        "runtime_label": code_executor.runtime_label(),
        "lessons": lab_content.all_lessons(),
        "challenges": challenges,
    }


@router.post("/run", response_model=LabRunResult)
def run(payload: LabRunRequest, current_user: User = Depends(get_current_user)):
    result = code_executor.execute_python(payload.source, stdin=payload.stdin)
    return result


@router.post("/submit", response_model=LabSubmitResult)
def submit(
    payload: LabSubmitRequest,
    current_student=Depends(get_current_student),
    db: Session = Depends(_with_db),
):
    challenge = lab_content.challenge_by_id(payload.challenge_id)
    if challenge is None:
        raise HTTPException(status_code=404, detail="Challenge not found.")

    retried = _attempt_count(db, current_student.student_id, challenge["id"])
    hints_used = _hints_used(db, current_student.student_id, challenge["id"])
    passed_before = _best_for(db, current_student.student_id, challenge["id"])

    if challenge["type"] == "output_prediction":
        result = lab_service.grade_mcq(challenge, payload.selected_index)
        correct = result["verdict"] == "correct"
        lab_service.record_attempt(
            db,
            current_student.student_id,
            challenge,
            correct=correct,
            passed_tests=result["tests_passed"],
            total_tests=result["tests_total"],
            hints_used=hints_used,
        )
        return {
            "verdict": result["verdict"],
            "tests_passed": result["tests_passed"],
            "tests_total": result["tests_total"],
            "correct_index": result["correct_index"],
            "explanation": result["explanation"],
            "feedback": lab_service.mcq_feedback(challenge, payload.selected_index, correct),
            "newly_passed": correct and not passed_before,
        }

    source = payload.source
    if not source or not source.strip():
        return {
            "verdict": "rejected",
            "tests_passed": 0,
            "tests_total": len(challenge.get("public_tests", []) or []),
            "feedback": "Your program is empty — write your solution in the editor, then press Submit.",
        }

    result = lab_service.grade_code_challenge(source, challenge.get("public_tests", []) or [])
    verdict = result["verdict"]
    correct = verdict == "passed"
    lab_service.record_attempt(
        db,
        current_student.student_id,
        challenge,
        correct=correct,
        passed_tests=result["tests_passed"],
        total_tests=result["tests_total"],
        hints_used=hints_used,
    )
    return {
        "verdict": verdict,
        "tests_passed": result["tests_passed"],
        "tests_total": result["tests_total"],
        "reports": result["reports"],
        "compile_error": result.get("compile_error"),
        "feedback": lab_service.feedback_for(result, challenge, retried=retried),
        "newly_passed": correct and not passed_before,
    }


@router.post("/hint", response_model=LabHintResult)
def hint(
    payload: LabHintRequest,
    current_student=Depends(get_current_student),
):
    challenge = lab_content.challenge_by_id(payload.challenge_id)
    if challenge is None:
        raise HTTPException(status_code=404, detail="Challenge not found.")

    level = payload.level if payload.level in ("general", "specific", "solution") else "general"
    used = max(0, min(int(payload.hints_used), 3))

    if level == "general":
        rank = max(used, 1)
    elif level == "specific":
        rank = max(used, 2)
        level = "specific"
    else:
        rank = max(used, 3)
        level = "solution"

    result = lab_service.hint_for(challenge, level)
    return {
        "challenge_id": challenge["id"],
        "level": level,
        "text": result["text"],
        "hints_used": rank,
        "remaining": max(0, 3 - rank),
    }


@router.post("/assist", response_model=LabAssistResult)
def assist(
    payload: LabAssistRequest,
    current_student=Depends(get_current_student),
):
    result = lab_assist.tutor_response(
        question=payload.question,
        code=payload.code or "",
        error=payload.error or "",
        depth=payload.depth,
        challenge_id=payload.challenge_id or "",
    )
    return {
        "depth": result["depth"],
        "text": result["text"],
        "suggestions": result["suggestions"],
    }


@router.get("/progress", response_model=LabProgressResponse)
def progress(
    current_student=Depends(get_current_student),
    db: Session = Depends(_with_db),
):
    return lab_service.lab_progress(db, current_student.student_id)


# --- persistence helpers ---------------------------------------------------

def _attempt_count(db: Session, student_id: str, challenge_id: str) -> int:
    from ..db import models

    return (
        db.query(models.LabAttempt)
        .filter(
            models.LabAttempt.student_id == student_id,
            models.LabAttempt.challenge_id == challenge_id,
        )
        .count()
    )


def _best_for(db: Session, student_id: str, challenge_id: str) -> bool:
    """True if this student already has a passing attempt for the challenge."""
    from ..db import models

    return (
        db.query(models.LabAttempt)
        .filter(
            models.LabAttempt.student_id == student_id,
            models.LabAttempt.challenge_id == challenge_id,
            models.LabAttempt.correct.is_(True),
        )
        .first()
        is not None
    )


def _hints_used(db: Session, student_id: str, challenge_id: str) -> int:
    from ..db import models

    rows = (
        db.query(models.LabAttempt)
        .filter(
            models.LabAttempt.student_id == student_id,
            models.LabAttempt.challenge_id == challenge_id,
        )
        .order_by(models.LabAttempt.created_at.desc())
        .all()
    )
    return max((int(r.hints_used) for r in rows), default=0)