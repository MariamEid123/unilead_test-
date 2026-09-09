"""Robotics Simulation end-to-end demo (Sprint 7G).

Runs the full proof loop for one student, deterministically:

    FAIL run  -> Assessments, evidence, SimulationRun, open remediation plan
    Coach turn-> reads the failed run facts (read-only; never mutates)
    PASS run  -> completes the plan, Mastery Engine records DEMONSTRATED,
                 pid-tuning leaves the transfer block list

Mirrors what ``tests/test_simulation.py`` asserts against the API, but
drives the service layer directly so it can be run headlessly. The default
provider is ``mock`` (deterministic, network-free); ``--provider ollama``
will coach the same loops with a real local model.

Usage::

    python -m scripts.demo_robotics_loop                 # mock (CI-fast)
    python -m scripts.demo_robotics_loop --provider ollama

Exit code is 0 when the whole loop proves, else 1.
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
from app.schemas.simulation import SimulationRequest  # noqa: E402
from app.services import (  # noqa: E402
    coach_context,
    coach_engine,
    simulation_service,  # noqa: E402
)
from app.services.simulation_contract import (  # noqa: E402
    SIM_FAILING_GAINS,
    SIM_PASSING_GAINS,
)

_MOCK_COACH_REPLIES = [
    "Your last run missed the settling-time and SSE criteria — let's revisit the "
    "integral gain. What would increasing Ki change in the response?",
]


def _prepare_student(db, want_student_id: str | None) -> str:
    """Prepare (or reuse) the demo student."""
    if want_student_id:
        students = crud.get_students_by_user_id(db, want_student_id)
        if students:
            return students[0].student_id

    univ = crud.get_university_by_code(db, "ARETE")
    if univ is None:
        raise SystemExit("ARETE university not found — bootstrap the app first.")

    email = "sim.demo@arete.edu.eg"
    user = crud.get_user_by_email(db, email)
    if user is None:
        user = crud.create_user(
            db,
            email=email,
            username="sim.demo",
            name="Simulation Demo",
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


def _run(db, student_id: str, **gains) -> dict:
    """One deterministic simulation run through the full evidence pipeline."""
    return simulation_service.run_simulation(SimulationRequest(**gains), student_id=student_id)


async def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=["mock", "ollama", "openai"], default="mock")
    parser.add_argument(
        "--student-id",
        default=None,
        help="reuse an existing student (user id or username)",
    )
    args = parser.parse_args()

    create_all_tables()

    settings = Settings(llm_provider_type=args.provider)
    factory = build_provider(settings)
    if args.provider == "mock":
        provider = MockLLMProvider(factory.config, responses=list(_MOCK_COACH_REPLIES))
    else:
        provider = factory

    db = SessionLocal()
    try:
        student_id = _prepare_student(db, args.student_id)
        print(f"Robotics simulation loop | provider={args.provider} student={student_id}")

        # 1) FAIL run — evidence, attempt, open plan.
        first = _run(db, student_id, **SIM_FAILING_GAINS)
        print(
            f"  [run#1 ] {first['result']:<4} Kp={first['kp']:.2f} Ki={first['ki']:.2f} "
            f"Kd={first['kd']:.2f} -> OS {first['overshoot']:.2f}% / "
            f"ST {first['settling_time']:.2f}s / SSE {first['steady_state_error']:.4f}"
        )
        print(
            f"          attempt={first['attempt']} misconception={first['misconception']} "
            f"remediation_plan_id={first['remediation_plan_id']}"
        )
        if first["result"] != "FAIL" or first["remediation_plan_id"] is None:
            print("FAIL: expected a failing run with an open remediation plan")
            return 1

        # 2) Coach turn — reads the failed run, writes nothing.
        result = await coach_engine.run_coach_turn(
            db,
            student_id=student_id,
            message="Why did my run fail? What should I try next?",
            provider=provider,
        )
        ctx = coach_context.build_coach_context(
            db, student_id=student_id, intent_code="DIAGNOSE", intent_mode="REMEDIATE"
        )
        latest_run = ctx["simulation"]["latest_run"]
        read_ok = (
            ctx["simulation"]["latest_result"] == "FAIL" and ctx["simulation"]["total_runs"] >= 1
        )
        coach_ok = (
            result["guardrail_blocked"] is False
            and bool(result["message"])
            and latest_run is not None
        )
        print(
            f"  [coach  ] reads total_runs={ctx['simulation']['total_runs']} "
            f"latest={ctx['simulation']['latest_result']} guardrail_ok={coach_ok}"
        )
        print(f"            coach: {result['message'][:96]}...")
        if not coach_ok or not read_ok:
            print("FAIL: coach did not read the simulation facts (or was blocked)")
            return 1

        # 3) PASS run — completes the plan and demonstrates mastery.
        second = _run(db, student_id, **SIM_PASSING_GAINS)
        print(
            f"  [run#2 ] {second['result']:<4} Kp={second['kp']:.2f} Ki={second['ki']:.2f} "
            f"Kd={second['kd']:.2f} -> OS {second['overshoot']:.2f}% / "
            f"ST {second['settling_time']:.2f}s / SSE {second['steady_state_error']:.4f}"
        )
        print(
            f"          attempt={second['attempt']} mastery_level={second['mastery_level']} "
            f"remediation_plan_id={second['remediation_plan_id']}"
        )
        pass_ok = second["result"] == "PASS" and second["mastery_level"] == "DEMONSTRATED"

        ctx = coach_context.build_coach_context(
            db, student_id=student_id, intent_code="PRACTICE", intent_mode="TRANSITION"
        )
        unblocked = all(
            b["competency_code"] != "pid-tuning" for b in ctx["transfer"]["blocked_competencies"]
        )
        transfer_ok = unblocked and ctx["simulation"]["latest_result"] == "PASS"
        print(
            f"  [transfer] ready={ctx['transfer']['ready']} progress={ctx['transfer']['progress']}"
        )

        overall = pass_ok and transfer_ok
        print(
            f"RESULT: {'PASS' if overall else 'FAIL'} "
            f"(fail->plan={first['result'] == 'FAIL'} coach_read={coach_ok} "
            f"pass->mastery={pass_ok} transfer_unblocked={transfer_ok})"
        )
        return 0 if overall else 1
    finally:
        db.close()


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
