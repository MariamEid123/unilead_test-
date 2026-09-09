from pydantic import BaseModel

from .common import CompetencyStatus


class ProgressCompetency(BaseModel):
    """The lightweight competency shape used in the progress summary."""

    name: str
    status: CompetencyStatus


class CourseProgress(BaseModel):
    """Per-course progress measured against the real curriculum."""

    course_id: str
    course_title: str
    progress_percentage: int | None = None
    completed_lectures: int | None = None
    total_lectures: int | None = None
    completed_quizzes: int | None = None
    total_quizzes: int | None = None
    completed_assignments: int | None = None
    total_assignments: int | None = None
    completed_lessons: list[str] = []


class ProgressResponse(BaseModel):
    overall_progress: int
    competencies: list[ProgressCompetency]
    recommended_next_activity: str
    course_code: str
    course_title: str
    courses: list[CourseProgress] = []
    last_active_course: str | None = None
    last_lecture: str | None = None