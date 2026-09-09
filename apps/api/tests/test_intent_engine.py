"""Sprint 6B — deterministic intent engine contract.

The LLM never chooses the intent; a keyword table + the adaptive focus do.
This suite pins the mapping tables and the precedence order.
"""

from app.services import intent_engine as ie

# --- intent -> active coach mode -------------------------------------------------


def test_mode_mapping_exact():
    assert ie.MODE_BY_INTENT == {
        "TEACH": "LEARN",
        "HINT": "HINT",
        "DIAGNOSE": "REMEDIATE",
        "REMEDIATE": "REMEDIATE",
        "REFLECT": "REFLECT",
        "TEACH_BACK": "TRANSFER",
    }


def test_all_intents_are_covered():
    assert set(ie.MODE_BY_INTENT) == set(ie.INTENTS)


# --- explicit intent wins ---------------------------------------------------------


def test_explicit_intent_overrides_everything():
    focus = {"action": "complete_remediation"}
    assert ie.resolve_intent("just a hello", focus=focus, explicit_intent="REFLECT") == "REFLECT"
    assert ie.resolve_intent("hint please", explicit_intent="TEACH") == "TEACH"


# --- legacy mode hint -> intent --------------------------------------------------


def test_mode_hint_mapping():
    assert ie.intent_from_mode("LEARN") == "TEACH"
    assert ie.intent_from_mode("HINT") == "HINT"
    assert ie.intent_from_mode("REMEDIATE") == "REMEDIATE"
    assert ie.intent_from_mode("REFLECT") == "REFLECT"
    assert ie.intent_from_mode("TRANSFER") == "TEACH_BACK"
    assert ie.intent_from_mode("PRACTICE") == "TEACH"
    assert ie.intent_from_mode(None) is None
    assert ie.intent_from_mode("bogus") is None


# --- keyword classification -------------------------------------------------------


def test_teach_keywords():
    for msg in [
        "can you teach me about feedback?",
        "explain what a PID controller is",
        "what is steady state error?",
        "help me understand the concept",
    ]:
        assert ie.resolve_intent(msg) == "TEACH", msg


def test_hint_keywords():
    for msg in ["give me a hint", "i'm stuck on this", "any clue?"]:
        assert ie.resolve_intent(msg) == "HINT", msg


def test_diagnose_keywords():
    for msg in [
        "why did i fail the tuning attempt?",
        "diagnose my last answer",
        "what went wrong with my gains?",
    ]:
        assert ie.resolve_intent(msg) == "DIAGNOSE", msg


def test_remediate_keywords():
    for msg in [
        "i need to remediate this",
        "review the concept with me",
        "redo the basics",
    ]:
        assert ie.resolve_intent(msg) == "REMEDIATE", msg


def test_reflect_keywords():
    for msg in ["let's reflect on the session", "summarize what i learned", "recap"]:
        assert ie.resolve_intent(msg) == "REFLECT", msg


def test_teach_back_keywords():
    for msg in ["teach it back to me", "explain it in my own words", "verify i got it"]:
        assert ie.resolve_intent(msg) == "TEACH_BACK", msg


# --- focus fallback (deterministic) ------------------------------------------------


def test_focus_drives_fallback_when_no_keyword_matches():
    assert ie.resolve_intent("hello", focus={"action": "complete_remediation"}) == "DIAGNOSE"
    assert ie.resolve_intent("go on", focus={"action": "practice"}) == "DIAGNOSE"
    assert ie.resolve_intent("hi", focus={"action": "revalidate"}) == "DIAGNOSE"
    assert ie.resolve_intent("hi", focus={"action": "unlock_prerequisite"}) == "TEACH"
    assert ie.resolve_intent("hi", focus=None) == "TEACH"


# --- grep-invariant keyword order --------------------------------------------------


def test_diagnose_beats_remediate_for_mistake_question():
    # "what went wrong" contains neither remediate nor teach keywords first.
    assert ie.resolve_intent("what went wrong in my attempt") == "DIAGNOSE"
