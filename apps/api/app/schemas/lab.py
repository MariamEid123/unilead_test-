"""Pydantic schemas for the code-lab API."""

from __future__ import annotations

from pydantic import BaseModel, Field


# --- runtime -------------------------------------------------------------

class LabRuntime(BaseModel):
    language: str
    available: bool
    label: str


class LabRunRequest(BaseModel):
    language: str = Field(default="python", pattern="^(python)$")
    source: str = Field(..., max_length=40_000)
    stdin: str = Field(default="", max_length=2_048)


class LabRunResult(BaseModel):
    status: str  # ok | compile_error | runtime_error | timeout | rejected | internal_error
    stdout: str = ""
    stderr: str = ""
    exit_code: int | None = None
    duration_ms: int = 0
    detail: str = ""


# --- manifest ------------------------------------------------------------

class LabLesson(BaseModel):
    code: str
    title: str


class LabChallengeView(BaseModel):
    id: str
    lesson_code: str
    type: str  # complete_code | debug | output_prediction | challenge
    topic: str
    difficulty: str
    title: str
    prompt: str
    starter_code: str | None = None
    code_text: str | None = None
    options: list[str] | None = None
    lesson_title: str = ""


class LabManifest(BaseModel):
    course_code: str
    course_title: str
    runtime: str
    runtime_label: str
    lessons: list[LabLesson]
    challenges: list[LabChallengeView]


# --- grading -------------------------------------------------------------

class LabSubmitRequest(BaseModel):
    challenge_id: str = Field(..., max_length=64)
    source: str | None = Field(default=None, max_length=40_000)
    selected_index: int | None = None


class LabTestReport(BaseModel):
    passed: bool
    input: str = ""
    expected: str = ""
    got: str = ""
    note: str | None = None


class LabSubmitResult(BaseModel):
    verdict: str  # passed | failed | compile_error | timeout | rejected | correct | wrong
    tests_passed: int = 0
    tests_total: int = 0
    reports: list[LabTestReport] = []
    compile_error: str | None = None
    correct_index: int | None = None
    explanation: str = ""
    feedback: str = ""
    newly_passed: bool = False


# --- hints ---------------------------------------------------------------

class LabHintRequest(BaseModel):
    challenge_id: str = Field(..., max_length=64)
    level: str = "general"  # general | specific | solution
    hints_used: int = 0


class LabHintResult(BaseModel):
    challenge_id: str
    level: str
    text: str
    hints_used: int
    remaining: int


# --- coach ---------------------------------------------------------------

class LabAssistRequest(BaseModel):
    question: str = Field(..., max_length=2_000)
    code: str = Field(default="", max_length=40_000)
    error: str = Field(default="", max_length=4_000)
    depth: str = Field(default="explain", pattern="^(hint|explain|deeper|solution)$")
    challenge_id: str = ""


class LabAssistResult(BaseModel):
    depth: str
    text: str
    suggestions: list[str] = []


# --- progress ------------------------------------------------------------

class LabRecentAttempt(BaseModel):
    challenge_id: str
    title: str
    type: str
    difficulty: str
    correct: bool
    passed_tests: int = 0
    total_tests: int = 0
    at: str = ""


class LabProgressResponse(BaseModel):
    total_challenges: int
    attempted: int
    passed: int
    attempts: int
    accuracy_pct: int
    current_difficulty: str
    streak_days: int
    progress_pct: int
    weak_topics: list[str] = []
    recent: list[LabRecentAttempt] = []