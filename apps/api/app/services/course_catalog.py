"""The only courses and lecture identifiers supported by course progress."""

from __future__ import annotations

COURSES: dict[str, dict] = {
    "physics": {
        "title": "Physics Fundamentals",
        "lectures": ("introduction-to-physics", "motion-and-speed", "newtons-laws"),
    },
    "math-zero": {
        "title": "Math Zero: Foundations",
        "lectures": ("numbers-and-operations", "patterns-and-equations", "fractions-and-proportions"),
    },
}


def get_course(course_id: str) -> dict | None:
    return COURSES.get(course_id)


def find_lecture(lecture_id: str) -> tuple[str, dict] | None:
    for course_id, course in COURSES.items():
        if lecture_id in course["lectures"]:
            return course_id, course
    return None
