from .mock_data import LESSON_SECTIONS, PRACTICE_TASKS


def _fallback_lesson() -> str:
    # The default lesson/practice bundle when a competency has no dedicated
    # content yet — anchored on the primary apply competency of PHY211.
    return "charge-transfer"


def get_lesson(competency_id: str) -> list[dict]:
    return LESSON_SECTIONS.get(competency_id, LESSON_SECTIONS[_fallback_lesson()])


def get_practice_task(competency_id: str) -> dict:
    return PRACTICE_TASKS.get(competency_id, PRACTICE_TASKS[_fallback_lesson()])
