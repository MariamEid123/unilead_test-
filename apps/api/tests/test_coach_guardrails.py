"""Sprint 6C — coach guardrail contract.

The prompt layer forbids cheating/invention; the mechanical layer
(``validate_reply``) re-checks any LLM output against the verified facts and
refuses to pass a violation through to the student.
"""

from app.services import coach_guardrails as cg

# --- prompt layer ----------------------------------------------------------------


def _context(*, competencies=None, focus=None):
    return {
        "version": "1",
        "student_id": "s1",
        "course": {"code": "MEC271", "title": "Control Systems"},
        "intent": {"code": "TEACH", "mode": "LEARN"},
        "focus": focus,
        "competencies": competencies
        or [
            {
                "competency_code": "pid-tuning",
                "competency_title": "PID Tuning",
                "mastery_level": "NOT_DEMONSTRATED",
                "confidence": 0.4,
                "evidence_count": 1,
                "weak_criteria": ["overshoot"],
                "misconceptions": [],
            }
        ],
        "learning_path": {},
        "remediation": {"open_plans": [], "open_count": 0},
        "evidence": {"recent_events": [], "attempted_count": 1, "demonstrated_count": 0},
        "transfer": {},
        "generated_at": "2026-01-01T00:00:00Z",
    }


def test_system_prompt_embeds_facts_and_guardrails():
    prompt = cg.build_system_prompt(_context())
    assert "VERIFIED FACTS" in prompt
    assert "pid-tuning" in prompt
    assert "Never give away the answer" in prompt
    assert "Never claim the student has mastered" in prompt
    assert "Never fabricate attempt history" in prompt


# --- mechanical layer: allowed reples -------------------------------------------------


def test_safe_coaching_passes():
    verdict = cg.validate_reply(
        "Good try! What would change if you lowered the overshoot next time?",
        context=_context(),
    )
    assert verdict["ok"] is True
    assert verdict["violations"] == []
    assert verdict["action"] == "allow"


def test_praise_without_mastery_claim_passes():
    verdict = cg.validate_reply(
        "You're asking the right questions. Keep going!", context=_context()
    )
    assert verdict["ok"] is True


# --- violation detections -------------------------------------------------------------


def test_assessment_answer_leak_blocked():
    verdict = cg.validate_reply("Don't worry — the correct gain is Kp = 2.0.", context=_context())
    assert "assessment_answer_leak" in verdict["violations"]


def test_engineered_leak_phrase_blocked():
    verdict = cg.validate_reply("final answer: set P high", context=_context())
    assert "assessment_answer_leak" in verdict["violations"]


def test_unearned_mastery_claim_blocked():
    verdict = cg.validate_reply("Awesome — you have mastered PID tuning!", context=_context())
    assert "unearned_mastery_claim" in verdict["violations"]


def test_mastery_claim_allowed_when_actually_demonstrated():
    ctx = _context(
        competencies=[
            {
                "competency_code": "pid-tuning",
                "competency_title": "PID Tuning",
                "mastery_level": "DEMONSTRATED",
                "confidence": 0.9,
                "evidence_count": 2,
                "weak_criteria": [],
                "misconceptions": [],
            }
        ]
    )
    verdict = cg.validate_reply("You demonstrated PID Tuning — great work!", context=ctx)
    assert verdict["ok"] is True


def test_fabricated_attempt_count_blocked():
    at_dict = {"action": "practice", "competency_code": "pid-tuning"}
    verdict = cg.validate_reply(
        "You've made 7 attempts today; that's a lot.", context=_context(focus=at_dict)
    )
    assert "fabricated_evidence_claim" in verdict["violations"]


def test_accurate_attempt_mention_passes():
    at_dict = {"action": "practice", "competency_code": "pid-tuning"}
    verdict = cg.validate_reply(
        "This is your 1 attempt so far — nice start.", context=_context(focus=at_dict)
    )
    assert verdict["ok"] is True


# --- fallback message ----------------------------------------------------------------


def test_fallback_message_points_at_focus():
    msg = cg.fallback_message(
        _context(focus={"action": "complete_remediation", "competency_code": "pid-tuning", "competency_title": "PID Tuning"})
    )
    assert "won't hand you the answer" in msg
    # Talks in curriculum terms — never the internal engine code.
    assert "PID Tuning" in msg
    assert "pid-tuning" not in msg


def test_fallback_message_prereq_focus():
    msg = cg.fallback_message(
        _context(
            competencies=[
                {
                    "competency_code": "pid-tuning",
                    "competency_title": "PID Tuning",
                    "mastery_level": "NOT_DEMONSTRATED",
                    "confidence": 0.4,
                    "evidence_count": 1,
                    "weak_criteria": ["overshoot"],
                    "misconceptions": [],
                },
                {
                    "competency_code": "pid-reasoning",
                    "competency_title": "PID Reasoning",
                    "mastery_level": "DEMONSTRATED",
                    "confidence": 0.9,
                    "evidence_count": 2,
                    "weak_criteria": [],
                    "misconceptions": [],
                },
            ],
            focus={
                "action": "unlock_prerequisite",
                "competency_code": "pid-tuning",
                "competency_title": "PID Tuning",
                "missing_prerequisites": ["pid-reasoning"],
            },
        )
    )
    assert "PID Tuning" in msg
    assert "PID Reasoning" in msg
    assert "pid-reasoning" not in msg
