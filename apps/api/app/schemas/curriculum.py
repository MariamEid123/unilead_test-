"""Response schemas for the curriculum catalog API.

Shapes mirror how the frontend lesson/course views consume them: catalog
cards, a module tree, lesson detail, content/summary/video/practice views.
"""

from pydantic import BaseModel


class CourseListItem(BaseModel):
    id: int
    code: str
    title: str
    description: str
    credits: int
    module_count: int
    lesson_count: int


class LessonCard(BaseModel):
    code: str
    title: str
    description: str
    difficulty: str
    estimated_minutes: int | None
    sort_order: int
    section_count: int
    video_count: int
    practice_count: int


class ModuleCard(BaseModel):
    code: str
    title: str
    description: str
    sort_order: int
    lessons: list[LessonCard]


class CourseDetail(BaseModel):
    id: int
    code: str
    title: str
    description: str
    credits: int
    modules: list[ModuleCard]


class CompetencyLink(BaseModel):
    code: str
    title: str
    role: str


class LessonDetail(BaseModel):
    code: str
    title: str
    description: str
    difficulty: str
    estimated_minutes: int | None
    objectives: list[str]
    prerequisites: list[str]
    course_code: str
    course_title: str
    module_code: str
    module_title: str
    competencies: list[CompetencyLink]
    section_count: int
    video_count: int
    practice_count: int


class ContentSection(BaseModel):
    section_type: str
    title: str | None
    body: str
    sort_order: int
    metadata: dict


class VideoResource(BaseModel):
    title: str
    description: str
    external_url: str | None
    duration_seconds: int | None
    sort_order: int
    metadata: dict


class CourseLessonMaterials(BaseModel):
    lesson_code: str
    lesson_title: str
    module_code: str
    module_title: str
    resources: list[VideoResource]


class PracticeItemView(BaseModel):
    id: int
    level: str
    prompt: str
    options: list[str]
    skill: str | None
    difficulty: int
    sort_order: int


class PracticeGradeResult(BaseModel):
    item_id: int
    correct: bool
    correct_index: int
    explanation: str