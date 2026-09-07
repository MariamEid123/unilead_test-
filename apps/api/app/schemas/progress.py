from datetime import datetime

from pydantic import BaseModel, Field


class CourseProgressResponse(BaseModel):
    course_id: str
    course_title: str
    progress_percentage: int
    completed_lectures: int
    total_lectures: int
    completed_quizzes: int
    total_quizzes: int
    completed_assignments: int
    total_assignments: int
    simulation_status: str | None
    review_status: str | None
    last_lecture: str | None
    last_accessed_at: datetime | None


class ProgressResponse(BaseModel):
    overall_progress: int
    courses: list[CourseProgressResponse]
    last_active_course: str | None
    last_lecture: str | None


class LectureProgressUpdate(BaseModel):
    completed: bool = Field(default=True, description="Whether the lecture is complete.")
