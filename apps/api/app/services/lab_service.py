"""Code-lab grading, feedback and progress aggregation.

Everything here is honest: a "passed" verdict means the *student's* code was
actually executed in the sandbox and satisfied every public test; an MCQ is
correct only when the selected option matches the a-priori answer. Feedback is
written to keep the student moving (never a flat "Wrong Answer").
"""

from __future__ import annotations

import re
from datetime import date, datetime, timezone, timedelta

from sqlalchemy.orm import Session

from . import code_executor, lab_content
from . import student_state

_TOPIC_LABELS = {
    "input_output": "input & output",
    "variables": "variables",
    "operators": "operators",
    "conditionals": "conditionals",
    "loops": "loops",
    "lists": "lists",
    "strings": "strings",
    "functions": "functions",
    "recursion": "recursion",
}

_PERFECT_FEEDBACK = [
    "Excellent work — your code passes every test.",
    "Perfect run. That's the kind of clean, working solution we're after.",
    "Well done! All tests green. Keep that momentum going.",
    "Great job — correct on the first try is always nice, but finishing it at all is what counts.",
]


def normalize_output(text: str) -> str:
    lines = [line.rstrip() for line in (text or "").splitlines()]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def _compile_error_line(stderr: str) -> int | None:
    match = re.search(r"line (\d+)", stderr or "")
    return int(match.group(1)) if match else None


def _first_stderr_line(stderr: str, max_len: int = 160) -> str:
    for line in (stderr or "").splitlines():
        if line.strip():
            return line.strip()[:max_len]
    return stderr[:max_len]


def grade_code_challenge(source: str, tests: list[dict]) -> dict:
    """Run the student's code against every test. Verdict is real."""
    reports: list[dict] = []
    compile_error: str | None = None
    all_passed = True
    for test in tests:
        run = code_executor.execute_python(source, stdin=test.get("input", ""))
        if run.status == "compile_error":
            compile_error = compile_error or run.stderr
            reports.append(
                {
                    "passed": False,
                    "input": test.get("input", ""),
                    "expected": test.get("expected", ""),
                    "got": "— program did not run (syntax error) —",
                    "note": "syntax_error",
                }
            )
            all_passed = False
            continue
        if run.status == "timeout":
            reports.append(
                {
                    "passed": False,
                    "input": test.get("input", ""),
                    "expected": test.get("expected", ""),
                    "got": "— timed out —",
                    "note": "timeout",
                }
            )
            all_passed = False
            continue
        got = normalize_output(run.stdout)
        expected = normalize_output(test.get("expected", ""))
        passed = run.status == "ok" and got == expected
        all_passed = all_passed and passed
        reports.append(
            {
                "passed": passed,
                "input": test.get("input", ""),
                "expected": test.get("expected", ""),
                "got": got,
                "note": None if passed else ("runtime_error" if run.status != "ok" else "mismatch"),
            }
        )

    status = "passed" if all_passed else ("compile_error" if compile_error else "failed")
    return {
        "verdict": status,
        "tests_passed": sum(1 for r in reports if r["passed"]),
        "tests_total": len(reports),
        "reports": reports,
        "compile_error": compile_error,
    }


def feedback_for(result: dict, challenge: dict, *, retried: int) -> str:
    verdict = result["verdict"]
    if verdict == "passed":
        template = _PERFECT_FEEDBACK[0]
        if retried > 0:
            template = "You got it! Debugging is normal — the important thing is you kept going and fixed it."
        if challenge["type"] == "debug":
            return "Nice catch — you spotted the bug and the program now behaves correctly."
        if challenge["type"] == "complete_code":
            return "Blanks filled correctly — the completed program runs and passes every test."
        if challenge["type"] == "challenge":
            return template
        return template
    if verdict == "compile_error":
        line = _compile_error_line(result["compile_error"])
        where = f" on line {line}" if line else ""
        tail = _first_stderr_line(result["compile_error"])
        return (
            f"Python couldn't run your code yet — there's a syntax problem{where}. "
            f"The error reads: “{tail}”. "
            "Check that every bracket and colon is closed and indentation is consistent "
            "inside blocks. Fix it and press Run again."
        )
    if verdict == "timeout":
        return (
            "Your program ran for too long and had to be stopped. This usually means a loop "
            "whose condition never becomes false — check your loop bounds and that you update "
            "the loop variable."
        )
    passed = result["tests_passed"]
    total = result["tests_total"]
    failed = next((r for r in result["reports"] if not r["passed"]), None)
    if failed is not None and failed.get("note") == "runtime_error":
        return (
            f"Almost there! {passed} of {total} tests pass, but your program crashes on one input. "
            "Read the runtime error on the right — it tells you the exact line and the reason. "
            "Often it's an index out of range, a type mix-up, or using a value before it exists."
        )
    return (
        f"Almost there! {passed} of {total} tests pass. "
        "Here's the first test that didn't match:\n\n"
        f"  input:    {failed['input'].strip()!r}\n"
        f"  expected: {failed['expected']!r}\n"
        f"  got:      {failed['got']!r}\n\n"
        "Compare the two lines closely — the difference is exactly what your program needs "
        "to fix. Ask the Coach if you'd like a nudge."
    )


def grade_mcq(challenge: dict, selected_index: int | None) -> dict:
    correct = selected_index == challenge.get("correct_index")
    return {
        "verdict": "correct" if correct else "wrong",
        "tests_passed": 1 if correct else 0,
        "tests_total": 1,
        "correct_index": challenge.get("correct_index"),
        "explanation": challenge.get("explanation", ""),
    }


def mcq_feedback(challenge: dict, selected_index: int | None, correct: bool) -> str:
    chosen = (
        challenge["options"][selected_index] if selected_index is not None and 0 <= selected_index < len(challenge["options"]) else None
    )
    if correct:
        return "Exactly right — you traced the program correctly."
    return (
        f"Hmm, \"{chosen}\" isn't what this program prints. That's fine — predicting output is a skill "
        "that improves fast. Here's the walkthrough:\n\n" + challenge.get("explanation", "")
    )


def hint_for(challenge: dict, level: str) -> dict:
    hints = challenge.get("hints", {})
    level = level if level in ("general", "specific", "solution") else "general"
    text = hints.get(level, "")
    if level == "solution" and challenge["type"] == "output_prediction":
        text = hints.get("solution", challenge.get("explanation", ""))
    return {"level": level, "text": text}


def record_attempt(
    db: Session,
    student_id: str,
    challenge: dict,
    *,
    correct: bool,
    passed_tests: int,
    total_tests: int,
    hints_used: int,
) -> None:
    from ..db import models

    row = models.LabAttempt(
        student_id=student_id,
        course_code=lab_content.COURSE_CODE,
        lesson_code=challenge.get("lesson_code", ""),
        challenge_id=challenge["id"],
        challenge_type=challenge["type"],
        difficulty=challenge.get("difficulty", "easy"),
        topic=challenge.get("topic", ""),
        correct=correct,
        passed_tests=passed_tests,
        total_tests=total_tests,
        hints_used=hints_used,
    )
    db.add(row)
    # Commit before student_state opens its own connections (SQLite = one writer).
    db.commit()

    lesson_title = lab_content.lesson_title(challenge.get("lesson_code", ""))
    student_state.append_evidence_event(
        student_id,
        event_type="lab_attempt",
        title=f"Code lab: {'solved' if correct else 'in progress'} — {challenge['title']}",
        detail=f"{lab_content.COURSE_CODE} · {challenge['type'].replace('_', ' ')} · {lesson_title}",
        result="PASS" if correct else "FAIL",
        competency_id=None,
    )
    if correct:
        student_state.bump_overall_progress(2, student_id)


def lab_progress(db: Session, student_id: str) -> dict:
    from ..db import models

    rows = (
        db.query(models.LabAttempt)
        .filter(models.LabAttempt.student_id == student_id)
        .order_by(models.LabAttempt.created_at.asc())
        .all()
    )
    total_challenges = len(lab_content.CHALLENGES) or 1

    attempted_ids = {r.challenge_id for r in rows}
    passed_ids = {r.challenge_id for r in rows if r.correct}
    attempts = len(rows)
    correct_attempts = sum(1 for r in rows if r.correct)

    accuracy_pct = round(100 * correct_attempts / attempts) if attempts else 0
    progress_pct = round(100 * len(passed_ids) / total_challenges)

    current_difficulty = "easy"
    if rows:
        current_difficulty = rows[-1].difficulty

    # Streak: consecutive calendar days ending at the most recent day with a pass.
    streak_days = _streak_days(rows)

    # Weak topics: topics whose most recent attempt across challenges still needs work.
    last_by_topic: dict[str, dict] = {}
    topic_fail: dict[str, int] = {}
    topic_total: dict[str, int] = {}
    for r in rows:
        last_by_topic[r.topic] = {"correct": r.correct}
        topic_total[r.topic] = topic_total.get(r.topic, 0) + 1
        if not r.correct:
            topic_fail[r.topic] = topic_fail.get(r.topic, 0) + 1
    weak = sorted(
        (
            (topic, topic_fail.get(topic, 0) / topic_total.get(topic, 1))
            for topic in last_by_topic
        ),
        key=lambda item: (-item[1], item[0]),
    )
    weak_topics = [_TOPIC_LABELS.get(t, t) for t, _ratio in weak[:3]]

    recent = []
    for r in rows[-5:]:
        recent.append(
            {
                "challenge_id": r.challenge_id,
                "title": (lab_content.challenge_by_id(r.challenge_id) or {}).get("title", r.challenge_id),
                "type": r.challenge_type,
                "difficulty": r.difficulty,
                "correct": r.correct,
                "passed_tests": r.passed_tests,
                "total_tests": r.total_tests,
                "at": r.created_at.isoformat() + "Z",
            }
        )

    return {
        "total_challenges": len(lab_content.CHALLENGES),
        "attempted": len(attempted_ids),
        "passed": len(passed_ids),
        "attempts": attempts,
        "accuracy_pct": accuracy_pct,
        "current_difficulty": current_difficulty,
        "streak_days": streak_days,
        "progress_pct": progress_pct,
        "weak_topics": weak_topics,
        "recent": recent,
    }


def _streak_days(rows) -> int:
    passing_days = {
        r.created_at.date()
        if hasattr(r.created_at, "date")
        else datetime.now(timezone.utc).date()
        for r in rows
        if r.correct
    }
    if not passing_days:
        return 0
    streak = 0
    cursor = max(passing_days)
    today = datetime.now(timezone.utc).date()
    # A streak is alive if the most recent passing day is today or yesterday.
    if cursor < today - timedelta(days=1):
        return 0
    while cursor in passing_days:
        streak += 1
        cursor -= timedelta(days=1)
    return streak