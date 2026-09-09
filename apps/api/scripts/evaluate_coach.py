"""Coach behavior evaluation harness (Sprint 6G).

Drives the Compass AI Coach through a scripted micro-conversation and scores
the observable guarantees of the Sprint 6 design:

  * intent determinism   — the LLM never chooses its own intent; the keyword
                           engine commits every turn to the expected intent.
  * guardrail integrity  — every coach reply passes ``validate_reply``
                           (no answer leaks, no invented mastery/evidence).
  * deterministic fallback on failure, with explicit flags.
  * context truthfulness — the CoachContext reflects the DB (the student is
                           prepped with a failed retry and an open plan, and
                           the focus must report ``complete_remediation``).

The default provider is ``mock`` (canned safe replies) → fully deterministic,
always-PASS regression evidence, no network. Run with ``--provider ollama``
to evaluate a real model on your machine.

Usage::

    python -m scripts.evaluate_coach                 # mock (CI-fast)
    python -m scripts.evaluate_coach --provider ollama

Exit code is 0 when every check passes, else 1.
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ai_education.llm.mock import MockLLMProvider  # noqa: E402

from app.auth.service import hash_password  # noqa: E402
from app.config import Settings  # noqa: E402
from app.db import crud  # noqa: E402
from app.db.database import SessionLocal, create_all_tables  # noqa: E402
from app.main import build_provider  # noqa: E402
from app.services import coach_context, coach_engine  # noqa: E402
from app.services.remediation_flow import submit_retry  # noqa: E402

_MOCK_REPLIES = [
    "Let's look at the steady-state error criterion first — what value did you measure?",
    "Small hint: the overshoot depends on how aggressively you raised the proportional gain.",
    "Your attempt shows the system did not stabilize — let's revisit the overshoot criterion.",
]
_VIOLATING_REPLY = "You already mastered PID — just set Kp to 2.0 and be done with it."

# (label, student message, expected intent)
_TURNS = [
    ("teach", "could you teach me what a PID controller does?", "TEACH"),
    ("hint", "give me a hint on the next step", "HINT"),
    ("diagnose", "why did my tuning attempt fail?", "DIAGNOSE"),
]

_FAIL = {"overshoot": 20.0, "settling_time": 3.0, "steady_state_error": 0.05, "stable": False}


def _prepare_student(db, want_student_id: str | None) -> str:
    """Prepare (or reuse) an evaluation student with a failed retry + open plan."""
    if want_student_id:
        if crud.get_student_by_id(db, want_student_id) is not None:
            return want_student_id
        owner = crud.get_user_by_id(db, want_student_id)
        if owner is not None:
            students = crud.get_students_by_user_id(db, owner.id)
            if students:
                return students[0].student_id

    univ = crud.get_university_by_code(db, "ARETE")
    if univ is None:
        raise SystemExit("ARETE university not found — bootstrap the app first.")

    email = "coach.eval@arete.edu.eg"
    user = crud.get_user_by_email(db, email)
    if user is None:
        user = crud.create_user(
            db,
            email=email,
            username="coach.eval",
            name="Coach Evaluation",
            password_hash=hash_password("Str0ng!Pass#word"),
            role="student",
            university_id=univ.id,
            email_verified=True,
        )
        db.commit()

    students = crud.get_students_by_user_id(db, user.id)
    if students:
        return students[0].student_id

    student = crud.create_student(
        db,
        student_id=f"u{user.id}-student",
        user_id=user.id,
        display_name=user.name,
        university_id=univ.id,
    )
    db.commit()
    return student.student_id


def _ensure_failing_context(student_id: str) -> bool:
    """Ensure the student has exactly one failed attempt and an open plan."""
    db = SessionLocal()
    try:
        open_plans = crud.get_open_remediation_plans(
            db, student_id=student_id, competency_id="pid-tuning"
        )
        if open_plans:
            return True
        submit_retry(
            db,
            student_id=student_id,
            competency_code="pid-tuning",
            metrics=_FAIL,
            context={},
        )
        db.commit()
        return True
    finally:
        db.close()


async def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=["mock", "ollama", "openai"], default="mock")
    parser.add_argument("--student-id", default=None, help="reuse an existing student")
    args = parser.parse_args()

    create_all_tables()

    settings = Settings(llm_provider_type=args.provider)
    factory = build_provider(settings)
    provider = factory
    if args.provider == "mock":
        # Canned safe replies + a canned violating reply for the block demo,
        # so the harness is deterministic and network-free (6F still holds —
        # it is a real MockLLMProvider constructed from the same factory).
        provider = MockLLMProvider(
            factory.config, responses=list(_MOCK_REPLIES) + [_VIOLATING_REPLY]
        )

    db = SessionLocal()
    try:
        student_id = _prepare_student(db, args.student_id)
        if not _ensure_failing_context(student_id):
            print("FAIL: could not prepare a failing context")
            return 1

        ctx = coach_context.build_coach_context(
            db, student_id=student_id, intent_code="DIAGNOSE", intent_mode="REMEDIATE"
        )
        focus = ctx["focus"]
        plan = crud.get_remediation_plan(db, plan_id=focus.get("plan_id"))
        plan_open = plan is not None and plan.status == "open"

        intent_ok = focus["action"] == "complete_remediation"
        comp_ok = focus["competency_code"] == "pid-tuning"
        print(f"Coach evaluation | provider={args.provider} student={student_id}")
        print(
            f"  context: focus={focus['action']} competency={focus['competency_code']} "
            f"plan_open={plan_open} evidence={ctx['evidence']['attempted_count']}"
        )

        if not (intent_ok and comp_ok and plan_open):
            print(
                f"FAIL context: focus={focus['action']}/{focus['competency_code']} plan_open={plan_open}"
            )
            return 1

        safe_passed = 0
        for label, message, expected in _TURNS:
            result = await coach_engine.run_coach_turn(
                db, student_id=student_id, message=message, provider=provider
            )
            intent_ok = result["intent"] == expected
            guardrail_ok = result["guardrail_blocked"] is False
            served_ok = result["fallback_used"] is False and bool(result["message"])
            ok = intent_ok and guardrail_ok and served_ok
            safe_passed += int(ok)
            print(
                f"  [{label:10}] intent={result['intent']:<9} expected={expected:<9} "
                f"guardrail_ok={guardrail_ok} fallback={result['fallback_used']} ok={ok}"
            )

        result = await coach_engine.run_coach_turn(
            db, student_id=student_id, message="test me", provider=provider
        )
        block_ok = (
            result["guardrail_blocked"] is True and "won't hand you the answer" in result["message"]
        )
        print(
            f"  [block-demo ] guardrail_blocked={result['guardrail_blocked']} "
            f"violations={result['violations']} served_deterministic={block_ok}"
        )

        overall = safe_passed == len(_TURNS) and block_ok
        print(
            f"RESULT: {'PASS' if overall else 'FAIL'} "
            f"({safe_passed}/{len(_TURNS)} safe turns, block-demo={block_ok}) "
            f"student={student_id}"
        )
        return 0 if overall else 1
    finally:
        db.close()


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
