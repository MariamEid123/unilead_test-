"""SQLAlchemy ORM models for the Arete platform.

Schema overview:

  University            - tenant org (super_admin creates; users/students belong)
  Faculty               - university -> faculty
  Department            - faculty -> department
  Course                - department -> course
  Competency            - durable, course-scoped skill definition (graph node)
  CompetencyPrerequisite- directed edge in the competency graph (DAG per course)
  Assessment            - competency-scoped instrument (DIAGNOSTIC/MASTERY/RETRY)
  AssessmentTask        - one objective probe inside an assessment
  AssessmentRubricCriterion - one deterministic pass/fail threshold (the rubric)
  AssessmentAttempt     - one student attempt (immutable, numbered)
  AttemptItemResult     - per-task rubric verdict inside an attempt
  EvidenceRecord        - central, objective proof (simulation/assessment/...)
  MasteryRecord         - immutable level assertion (NOT_DEMONSTRATED/DEVELOPING/DEMONSTRATED)
  Section               - course -> section (one instructor)
  Enrollment            - student <-> section membership (access boundary)
  User                  - auth account (email + password hash + token version)
  Student              - one User → many Students (currently 1:1 in practice)
  CompetencySnapshot   - per-student, per-competency status + progress
  OnboardingAnswer     - one row per student (set once at onboarding)
  DiagnosticSubmission  - one row per diagnostic quiz submission (1-5 answers)
  DiagnosticAnswer     - one row per question answered in a submission
  SimulationRun        - one row per PID simulation run
  TransferEvaluation   - one row per transfer task submission
  RemediationPlan      - one row per remediation plan generated
  CoachConversation    - one row per coach session (group of turns)
  CoachMessage         - one row per message in a conversation
  EvidenceEvent        - chronological feed entry (one per notable event)
  AuditLog             - security-relevant actions (auth + org + instructor)
"""

from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import (
    JSON,
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


def _utcnow() -> datetime:
    """Timezone-naive UTC now — matches SQLite's default datetime format."""
    return datetime.now(UTC).replace(tzinfo=None)


class University(Base):
    """A tenant organization (university). Everything hangs off this."""

    __tablename__ = "universities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email_domains: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    faculties: Mapped[list[Faculty]] = relationship(
        "Faculty", back_populates="university", cascade="all, delete-orphan"
    )


class Faculty(Base):
    """A faculty within a university (e.g. Engineering)."""

    __tablename__ = "faculties"
    __table_args__ = (
        UniqueConstraint("university_id", "code", name="uq_faculties_university_code"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    university_id: Mapped[int] = mapped_column(
        ForeignKey("universities.id"), nullable=False, index=True
    )
    code: Mapped[str] = mapped_column(String(32), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    university: Mapped[University] = relationship("University", back_populates="faculties")
    departments: Mapped[list[Department]] = relationship(
        "Department", back_populates="faculty", cascade="all, delete-orphan"
    )


class Department(Base):
    """A department within a faculty (e.g. Mechanical Engineering)."""

    __tablename__ = "departments"
    __table_args__ = (UniqueConstraint("faculty_id", "code", name="uq_departments_faculty_code"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    faculty_id: Mapped[int] = mapped_column(ForeignKey("faculties.id"), nullable=False, index=True)
    code: Mapped[str] = mapped_column(String(32), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    faculty: Mapped[Faculty] = relationship("Faculty", back_populates="departments")
    courses: Mapped[list[Course]] = relationship(
        "Course", back_populates="department", cascade="all, delete-orphan"
    )


class Course(Base):
    """A course within a department (e.g. MEC271 Automatic Control)."""

    __tablename__ = "courses"
    __table_args__ = (UniqueConstraint("department_id", "code", name="uq_courses_department_code"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id"), nullable=False, index=True
    )
    code: Mapped[str] = mapped_column(String(32), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    credits: Mapped[int] = mapped_column(Integer, nullable=False, default=3)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    department: Mapped[Department] = relationship("Department", back_populates="courses")
    sections: Mapped[list[Section]] = relationship(
        "Section", back_populates="course", cascade="all, delete-orphan"
    )
    modules: Mapped[list[Module]] = relationship(
        "Module",
        back_populates="course",
        cascade="all, delete-orphan",
        order_by="Module.sort_order",
    )


class Competency(Base):
    """A durable, course-scoped competency definition (the graph of skills).

    This is the source of truth for *what* a learner must demonstrate. It is
    intentionally distinct from ``CompetencySnapshot``, which is a derived,
    per-student view of progress. A competency here defines the capability;
    assessment/evidence/mastery records prove whether any given student has
    it. For MEC271 the initial set comes from ``services.mock_data``.
    """

    __tablename__ = "competencies"
    __table_args__ = (UniqueConstraint("course_id", "code", name="uq_competencies_course_code"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False, index=True)
    code: Mapped[str] = mapped_column(String(64), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    # Bloom-style taxonomy level (e.g. recall / understand / apply / analyze /
    # evaluate / create). Informational for now — drives later pedagogy.
    taxonomy_level: Mapped[str | None] = mapped_column(String(32), nullable=True)
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    course: Mapped[Course | None] = relationship("Course")
    prerequisites: Mapped[list[CompetencyPrerequisite]] = relationship(
        "CompetencyPrerequisite",
        foreign_keys="CompetencyPrerequisite.post_competency_id",
        cascade="all, delete-orphan",
        back_populates="post",
    )


class CompetencyPrerequisite(Base):
    """A directed edge in the competency graph: ``pre`` must precede ``post``.

    Forms a DAG per course. The graph is honored for sequencing/remediation
    later; Sprint 4 only needs the reliable relationship data, not a graph
    traversal engine.
    """

    __tablename__ = "competency_prerequisites"
    __table_args__ = (
        UniqueConstraint(
            "course_id",
            "pre_competency_id",
            "post_competency_id",
            name="uq_competency_prereq_edge",
        ),
        Index("ix_cp_post", "course_id", "post_competency_id"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False, index=True)
    pre_competency_id: Mapped[int] = mapped_column(
        ForeignKey("competencies.id"), nullable=False, index=True
    )
    post_competency_id: Mapped[int] = mapped_column(
        ForeignKey("competencies.id"), nullable=False, index=True
    )

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    pre: Mapped[Competency] = relationship("Competency", foreign_keys=[pre_competency_id])
    post: Mapped[Competency] = relationship(
        "Competency",
        foreign_keys=[post_competency_id],
        back_populates="prerequisites",
    )


class Assessment(Base):
    """An assessment instrument probing one competency.

    ``kind`` distinguishes the instrument's role: DIAGNOSTIC (where the
    student starts), MASTERY (the rubric-gated attempt that can demonstrate
    the competency), RETRY (a fresh attempt after remediation). ``pass_rule``
    is a compact JSON blob describing *how many* mandatory rubric criteria
    are required — Sprint 4's Mastery engine enforces "ALL mandatory criteria
    on valid objective evidence → DEMONSTRATED".
    """

    __tablename__ = "assessments"
    __table_args__ = (
        UniqueConstraint("competency_id", "title", name="uq_assessments_competency_title"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    competency_id: Mapped[int] = mapped_column(
        ForeignKey("competencies.id"), nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    kind: Mapped[str] = mapped_column(String(16), nullable=False, default="MASTERY")
    # JSON: {"all_mandatory": true, "min_criteria": 4} — evaluated in 4D.
    pass_rule: Mapped[str] = mapped_column(Text, nullable=False, default="{}")
    # JSON list of {"criterion": "overshoot <= 10"} — human-readable spec.
    rubric_spec: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    competency: Mapped[Competency | None] = relationship("Competency")
    tasks: Mapped[list[AssessmentTask]] = relationship(
        "AssessmentTask",
        back_populates="assessment",
        cascade="all, delete-orphan",
        order_by="AssessmentTask.sort_order",
    )
    rubric_criteria: Mapped[list[AssessmentRubricCriterion]] = relationship(
        "AssessmentRubricCriterion",
        back_populates="assessment",
        cascade="all, delete-orphan",
    )


class AssessmentTask(Base):
    """One item/objective probe within an assessment.

    ``metric_field`` names the deterministic metric this task measures from
    the evidence (e.g. ``overshoot``, ``settling_time``, ``steady_state_error``,
    ``stable``) — this is what the rubric thresholds compare against.
    """

    __tablename__ = "assessment_tasks"
    __table_args__ = (
        UniqueConstraint("assessment_id", "code", name="uq_assessment_tasks_oq_code"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    assessment_id: Mapped[int] = mapped_column(
        ForeignKey("assessments.id"), nullable=False, index=True
    )
    code: Mapped[str] = mapped_column(String(64), nullable=False)
    prompt: Mapped[str] = mapped_column(Text, nullable=False)
    metric_field: Mapped[str | None] = mapped_column(String(64), nullable=True)
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    assessment: Mapped[Assessment] = relationship("Assessment", back_populates="tasks")


class AssessmentRubricCriterion(Base):
    """One deterministic pass/fail criterion for an assessment.

    Together the criteria of an assessment form its rubric. The Mastery engine
    (4D) evaluates each criterion against the ``metric_field`` value extracted
    from an EvidenceRecord, with no LLM involvement.
    """

    __tablename__ = "assessment_rubric_criteria"
    __table_args__ = (
        UniqueConstraint(
            "assessment_id",
            "metric_field",
            name="uq_assessment_rubric_metric",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    assessment_id: Mapped[int] = mapped_column(
        ForeignKey("assessments.id"), nullable=False, index=True
    )
    metric_field: Mapped[str] = mapped_column(String(64), nullable=False)
    # Comparison operator: <=, <, >=, >, == (applied to metric_value as number),
    # or "is_true" / "is_false" for boolean metrics like ``stable``.
    operator: Mapped[str] = mapped_column(String(16), nullable=False)
    threshold: Mapped[float | None] = mapped_column(Float, nullable=True)
    # True = this criterion is part of the mandatory gate for DEMONSTRATED.
    mandatory: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    assessment: Mapped[Assessment] = relationship("Assessment", back_populates="rubric_criteria")


class AssessmentAttempt(Base):
    """One student attempt at an assessment.

    ``attempt_number`` is per (assessment_id, student_id) and starts at 1.
    Attempts are written once, never overwritten — they are part of the
    immutable evidence timeline for a competency. Rubric evaluation (Sprint
    4D) fills ``score``, ``passed`` and the per-criterion ``results_json``.
    """

    __tablename__ = "assessment_attempts"
    __table_args__ = (
        UniqueConstraint(
            "assessment_id",
            "student_id",
            "attempt_number",
            name="uq_assessment_attempt_number",
        ),
        Index("ix_attempts_student", "student_id", "assessment_id"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    assessment_id: Mapped[int] = mapped_column(
        ForeignKey("assessments.id"), nullable=False, index=True
    )
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), nullable=False, index=True
    )
    attempt_number: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(
        String(16), nullable=False, default="SUBMITTED"
    )  # IN_PROGRESS / SUBMITTED
    score: Mapped[float | None] = mapped_column(Float, nullable=True)
    passed: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    # JSON list of {"metric": ..., "operator": ..., "threshold": ...,
    # "actual": ..., "passed": ...} — the full rubric evaluation snapshot.
    results_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    # JSON bool — overall resolution from the rubric pass_rule.
    resolution_json: Mapped[str] = mapped_column(Text, nullable=False, default="{}")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)
    submitted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    assessment: Mapped[Assessment] = relationship("Assessment")
    student: Mapped[Student] = relationship("Student")
    item_results: Mapped[list[AttemptItemResult]] = relationship(
        "AttemptItemResult",
        back_populates="attempt",
        cascade="all, delete-orphan",
    )


class AttemptItemResult(Base):
    """Per-task result within an assessment attempt.

    Links one submitted answer/task to its own rubric verdict. Stored
    immutably alongside the attempt — the detailed "why" behind the score.
    """

    __tablename__ = "attempt_item_results"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    attempt_id: Mapped[int] = mapped_column(
        ForeignKey("assessment_attempts.id"), nullable=False, index=True
    )
    task_code: Mapped[str] = mapped_column(String(64), nullable=False)
    metric_field: Mapped[str | None] = mapped_column(String(64), nullable=True)
    # JSON: a metric's current value may be a float (overshoot) *or* a
    # boolean (stable) — Postgres rejects bool into a FLOAT column, so store
    # the verdict faithfully in a type-flexible column instead.
    actual: Mapped[float | bool | None] = mapped_column(JSON, nullable=True)
    passed: Mapped[bool] = mapped_column(Boolean, nullable=False)
    misconception_tag: Mapped[str | None] = mapped_column(String(128), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    attempt: Mapped[AssessmentAttempt] = relationship(
        "AssessmentAttempt", back_populates="item_results"
    )


class EvidenceRecord(Base):
    """A single objective piece of proof about a student and competency.

    This is the *central* evidence table — every source type (simulation,
    assessment attempt, diagnostic, transfer task, future instructor
    evidence) writes one row with its deterministic metrics. The rubric
    engine (4D) reads only from here to decide mastery. ``metric_json``
    holds the objective, comparable numbers (e.g. overshoot, settling_time,
    stable, score/total); nothing in it is generated by an LLM.
    """

    __tablename__ = "evidence_records"
    __table_args__ = (
        Index("ix_evidence_student_competency", "student_id", "competency_id"),
        Index("ix_evidence_competency_created", "competency_id", "created_at"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), nullable=False, index=True
    )
    competency_id: Mapped[int] = mapped_column(
        ForeignKey("competencies.id"), nullable=False, index=True
    )
    # Source of the evidence: simulation / assessment / diagnostic / transfer /
    # instructor. Determines which metric fields to expect in metric_json.
    source_type: Mapped[str] = mapped_column(String(32), nullable=False)
    # PK of the source row (e.g. simulation_runs.id, assessment_attempts.id).
    source_ref_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    # JSON dict of deterministic metrics: {"overshoot": 6.2, "stable": true, ...}
    metric_json: Mapped[str] = mapped_column(Text, nullable=False, default="{}")
    # JSON dict of optional context (gains kp/ki/kd, answer ids, etc.).
    context_json: Mapped[str] = mapped_column(Text, nullable=False, default="{}")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    student: Mapped[Student] = relationship("Student")
    competency: Mapped[Competency | None] = relationship("Competency")


class MasteryRecord(Base):
    """An immutable assertion about a student's demonstrated level.

    One row per (student, competency) **state change** — never overwritten,
    always appended. History is the truth: Student A's PID Tuning journey
    (NOT_DEMONSTRATED -> DEVELOPING -> DEMONSTRATED) is three rows. The
    derived ``CompetencySnapshot`` is merely the latest resolved state for
    fast reads; the real answer to "what have we proven?" lives here.

    ``level`` is one of NOT_DEMONSTRATED / DEVELOPING / DEMONSTRATED.
    ``reason_codes`` is a JSON list of concise machine-readable reasons, e.g.
    ``["all_mandatory_passed"]`` for a demo, or
    ``["mandatory_failed:overshoot"]`` for a developing state.
    ``evidence_ids`` references the EvidenceRecords that drove this verdict —
    the proof trail stays fully auditable.
    """

    __tablename__ = "mastery_records"
    __table_args__ = (
        UniqueConstraint(
            "student_id",
            "competency_id",
            "level",
            "resolved_at",
            name="uq_mastery_state",
        ),
        Index("ix_mastery_student_level", "student_id", "level"),
        Index("ix_mastery_student_competency", "student_id", "competency_id"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), nullable=False, index=True
    )
    competency_id: Mapped[int] = mapped_column(
        ForeignKey("competencies.id"), nullable=False, index=True
    )
    level: Mapped[str] = mapped_column(String(32), nullable=False)
    # JSON dict of the rubric snapshot that produced this verdict.
    rubric_json: Mapped[str] = mapped_column(Text, nullable=False, default="{}")
    # JSON list of reason codes, e.g. ["all_mandatory_passed"].
    reason_codes_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    # JSON list of EvidenceRecord ids that drove the verdict.
    evidence_ids_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)
    resolved_at: Mapped[datetime] = mapped_column(
        DateTime, default=_utcnow, nullable=False, index=True
    )

    student: Mapped[Student] = relationship("Student")
    competency: Mapped[Competency | None] = relationship("Competency")


class Section(Base):
    """One teaching section of a course, taught by one instructor."""

    __tablename__ = "sections"
    __table_args__ = (
        UniqueConstraint("course_id", "term", "code", name="uq_sections_course_term_code"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False, index=True)
    term: Mapped[str] = mapped_column(String(32), nullable=False)
    code: Mapped[str] = mapped_column(String(32), nullable=False)
    instructor_user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"), nullable=True, index=True
    )

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    course: Mapped[Course] = relationship("Course", back_populates="sections")
    instructor: Mapped[User | None] = relationship("User", foreign_keys=[instructor_user_id])
    enrollments: Mapped[list[Enrollment]] = relationship(
        "Enrollment", back_populates="section", cascade="all, delete-orphan"
    )


class Enrollment(Base):
    """Student ↔ section membership — the access boundary for course data."""

    __tablename__ = "enrollments"
    __table_args__ = (
        UniqueConstraint("student_id", "section_id", name="uq_enrollments_student_section"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), nullable=False, index=True
    )
    section_id: Mapped[int] = mapped_column(ForeignKey("sections.id"), nullable=False, index=True)
    status: Mapped[str] = mapped_column(String(16), nullable=False, default="active")

    enrolled_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    student: Mapped[Student] = relationship("Student", back_populates="enrollments")
    section: Mapped[Section] = relationship("Section", back_populates="enrollments")


class User(Base):
    """Auth account — email + hashed password. One user can own many students."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(16), nullable=False, default="student")
    # "student" or "instructor" — gates access to instructor endpoints

    password_hash: Mapped[str | None] = mapped_column(String(255), nullable=True)
    # nullable so seeded demo accounts (without passwords) can exist for read-only views

    # Email verification — set once at signup via a confirmation code.
    # The plaintext code is never stored: only its SHA-256 hash, so a DB
    # leak can't be replayed without the code that was emailed to the user.
    email_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    email_verification_code_hash: Mapped[str | None] = mapped_column(String(64), nullable=True)
    email_verification_expires_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    email_verification_sent_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    # Password reset — same pattern as verification: a hashed, expiring code.
    password_reset_code_hash: Mapped[str | None] = mapped_column(String(64), nullable=True)
    password_reset_expires_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    password_reset_sent_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    last_password_change_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    # Session/token lifecycle: every JWT carries this number at issue time.
    # Bumping it (e.g. after a password reset) revokes every previously
    # issued token for the account in one step — no per-token blacklist.
    token_version: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # Tenant membership: the university this account belongs to (null until
    # the default organization backfill / explicit provisioning assigns one).
    university_id: Mapped[int | None] = mapped_column(
        ForeignKey("universities.id"), nullable=True, index=True
    )

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    students: Mapped[list[Student]] = relationship("Student", back_populates="user")


class Student(Base):
    """A learner record. ``student_id`` is the stable public identifier
    used by the AI Education engine (e.g. ``api-gateway-student``)."""

    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    display_name: Mapped[str] = mapped_column(String(255), nullable=False)
    course_code: Mapped[str] = mapped_column(String(32), nullable=False, default="PHY211")
    course_title: Mapped[str] = mapped_column(
        String(255), nullable=False, default="Physics"
    )
    overall_progress: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # Tenant membership: the university this learner belongs to.
    university_id: Mapped[int | None] = mapped_column(
        ForeignKey("universities.id"), nullable=True, index=True
    )

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    user: Mapped[User] = relationship("User", back_populates="students")
    enrollments: Mapped[list[Enrollment]] = relationship(
        "Enrollment", back_populates="student", cascade="all, delete-orphan"
    )
    sections: Mapped[list[Section]] = relationship(
        "Section",
        secondary="enrollments",
        primaryjoin="Enrollment.student_id == Student.student_id",
        secondaryjoin="Enrollment.section_id == Section.id",
        viewonly=True,
    )
    competencies: Mapped[list[CompetencySnapshot]] = relationship(
        "CompetencySnapshot", back_populates="student", cascade="all, delete-orphan"
    )
    onboarding: Mapped[OnboardingAnswer | None] = relationship(
        "OnboardingAnswer", back_populates="student", uselist=False, cascade="all, delete-orphan"
    )
    diagnostic_submissions: Mapped[list[DiagnosticSubmission]] = relationship(
        "DiagnosticSubmission", back_populates="student", cascade="all, delete-orphan"
    )
    simulation_runs: Mapped[list[SimulationRun]] = relationship(
        "SimulationRun", back_populates="student", cascade="all, delete-orphan"
    )
    transfer_evaluations: Mapped[list[TransferEvaluation]] = relationship(
        "TransferEvaluation", back_populates="student", cascade="all, delete-orphan"
    )
    remediation_plans: Mapped[list[RemediationPlan]] = relationship(
        "RemediationPlan", back_populates="student", cascade="all, delete-orphan"
    )
    coach_conversations: Mapped[list[CoachConversation]] = relationship(
        "CoachConversation", back_populates="student", cascade="all, delete-orphan"
    )
    evidence_events: Mapped[list[EvidenceEvent]] = relationship(
        "EvidenceEvent", back_populates="student", cascade="all, delete-orphan"
    )
    lesson_progress: Mapped[list[LessonProgress]] = relationship(
        "LessonProgress", back_populates="student", cascade="all, delete-orphan"
    )
    practice_results: Mapped[list[PracticeResult]] = relationship(
        "PracticeResult", back_populates="student", cascade="all, delete-orphan"
    )
    assessment_attempts: Mapped[list[AssessmentAttempt]] = relationship(
        "AssessmentAttempt", back_populates="student", cascade="all, delete-orphan"
    )
    evidence_records: Mapped[list[EvidenceRecord]] = relationship(
        "EvidenceRecord", back_populates="student", cascade="all, delete-orphan"
    )
    mastery_records: Mapped[list[MasteryRecord]] = relationship(
        "MasteryRecord", back_populates="student", cascade="all, delete-orphan"
    )


class CompetencySnapshot(Base):
    """Per-student, per-competency status + progress (current view)."""

    __tablename__ = "competency_snapshots"
    __table_args__ = (
        UniqueConstraint("student_id", "competency_id", name="uq_student_competency"),
        Index("ix_cs_student_status", "student_id", "status"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), nullable=False, index=True
    )
    competency_id: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    competency_name: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="not_started")
    progress: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=_utcnow, onupdate=_utcnow, nullable=False
    )

    student: Mapped[Student] = relationship("Student", back_populates="competencies")


class OnboardingAnswer(Base):
    """The four onboarding answers. One row per student."""

    __tablename__ = "onboarding_answers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), unique=True, nullable=False
    )
    learning_challenge: Mapped[str] = mapped_column(Text, nullable=False)
    preferred_method: Mapped[str] = mapped_column(Text, nullable=False)
    obstacle: Mapped[str] = mapped_column(Text, nullable=False)
    goal: Mapped[str] = mapped_column(Text, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    student: Mapped[Student] = relationship("Student", back_populates="onboarding")


class DiagnosticSubmission(Base):
    """One diagnostic quiz submission (1-5 answers)."""

    __tablename__ = "diagnostic_submissions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), nullable=False, index=True
    )
    score: Mapped[int] = mapped_column(Integer, nullable=False)  # correct count
    total: Mapped[int] = mapped_column(Integer, nullable=False)  # total questions
    misconceptions_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    student: Mapped[Student] = relationship("Student", back_populates="diagnostic_submissions")
    answers: Mapped[list[DiagnosticAnswer]] = relationship(
        "DiagnosticAnswer", back_populates="submission", cascade="all, delete-orphan"
    )


class DiagnosticAnswer(Base):
    """One answer within a diagnostic submission."""

    __tablename__ = "diagnostic_answers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    submission_id: Mapped[int] = mapped_column(
        ForeignKey("diagnostic_submissions.id"), nullable=False, index=True
    )
    question_id: Mapped[str] = mapped_column(String(32), nullable=False)
    competency_id: Mapped[str] = mapped_column(String(64), nullable=False)
    selected_option_id: Mapped[str] = mapped_column(String(32), nullable=False)
    correct: Mapped[bool] = mapped_column(Boolean, nullable=False)
    misconception_tag: Mapped[str | None] = mapped_column(String(128), nullable=True)

    submission: Mapped[DiagnosticSubmission] = relationship(
        "DiagnosticSubmission", back_populates="answers"
    )


class SimulationRun(Base):
    """One PID simulation run — gains, metrics, result, misconception."""

    __tablename__ = "simulation_runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), nullable=False, index=True
    )
    competency_id: Mapped[str] = mapped_column(String(64), nullable=False)
    task_id: Mapped[str] = mapped_column(String(64), nullable=False, default="pid-001")
    attempt: Mapped[int] = mapped_column(Integer, nullable=False)

    # Gains
    kp: Mapped[float] = mapped_column(Float, nullable=False)
    ki: Mapped[float] = mapped_column(Float, nullable=False)
    kd: Mapped[float] = mapped_column(Float, nullable=False)

    # Metrics
    stable: Mapped[bool] = mapped_column(Boolean, nullable=False)
    overshoot: Mapped[float] = mapped_column(Float, nullable=False)
    settling_time: Mapped[float] = mapped_column(Float, nullable=False)
    rise_time: Mapped[float] = mapped_column(Float, nullable=False)
    steady_state_error: Mapped[float] = mapped_column(Float, nullable=False)

    # Outcome
    requirements_met: Mapped[bool] = mapped_column(Boolean, nullable=False)
    result: Mapped[str] = mapped_column(String(8), nullable=False)  # PASS / FAIL
    misconception: Mapped[str | None] = mapped_column(String(128), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    student: Mapped[Student] = relationship("Student", back_populates="simulation_runs")


class TransferEvaluation(Base):
    """One transfer task submission — scenario + response + evaluation."""

    __tablename__ = "transfer_evaluations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), nullable=False, index=True
    )
    competency_id: Mapped[str] = mapped_column(String(64), nullable=False)
    scenario_id: Mapped[str] = mapped_column(String(64), nullable=False)
    response_text: Mapped[str] = mapped_column(Text, nullable=False)
    passed: Mapped[bool] = mapped_column(Boolean, nullable=False)
    matched_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    min_required: Mapped[int] = mapped_column(Integer, default=2, nullable=False)
    feedback: Mapped[str] = mapped_column(Text, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    student: Mapped[Student] = relationship("Student", back_populates="transfer_evaluations")


class RemediationPlan(Base):
    """One remediation plan generated for a failing competency.

    Sprint 4E: a plan is now *linked to the evidence that revealed the
    problem* (``evidence_id``), not just the student/competency. The plan's
    lifecycle is ``open -> completed`` (``completed_at``) and the reason
    codes explain *why* remediation was offered (failed rubric criteria).
    This makes every plan auditable: given a plan we can answer "which
    evidence triggered this, and which criteria missed?"
    """

    __tablename__ = "remediation_plans"
    __table_args__ = (
        Index("ix_remediation_plans_evidence_id", "evidence_id"),
        Index("ix_remediation_plans_status", "status"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), nullable=False, index=True
    )
    # Compass competency code (legacy naming: `competency_id` is the code).
    competency_id: Mapped[str] = mapped_column(String(64), nullable=False)
    # 4E: the exact EvidenceRecord that triggered this remediation.
    evidence_id: Mapped[int | None] = mapped_column(
        ForeignKey("evidence_records.id"), nullable=True
    )
    # JSON list of failed rubric criteria, e.g.
    # ["settling_time > 2.0", "stable != true"].
    reason_codes_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    # Plan lifecycle: open / completed / superseded.
    status: Mapped[str] = mapped_column(String(16), nullable=False, default="open")
    detected_misconception: Mapped[str | None] = mapped_column(String(128), nullable=True)
    recommended_action: Mapped[str] = mapped_column(String(64), nullable=False)
    conceptual_focus: Mapped[str] = mapped_column(Text, nullable=False)
    guided_question: Mapped[str] = mapped_column(Text, nullable=False)
    consecutive_failures: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    total_attempts: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    summary_text: Mapped[str] = mapped_column(Text, nullable=False, default="")
    remediation_steps_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    student: Mapped[Student] = relationship("Student", back_populates="remediation_plans")
    evidence: Mapped[EvidenceRecord | None] = relationship("EvidenceRecord")


class RemediationResource(Base):
    """Content catalog entry used by the deterministic adaptive controller.

    Sprint 5E: a resource is matched to a student's state by tags, so the
    adaptive controller can recommend specific practice material instead of
    a generic "study the concept" instruction. Matchers are deliberately
    nullable so a single row can target a competency, a misconception, or a
    specific rubric criterion. ``sort_order`` breaks ties deterministically.
    """

    __tablename__ = "remediation_resources"
    __table_args__ = (
        UniqueConstraint("resource_code", name="uq_remediation_resources_code"),
        Index("ix_remediation_resources_competency", "competency_code"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    resource_code: Mapped[str] = mapped_column(String(64), nullable=False)
    # Target selectors — at most one of these should match a given student.
    competency_code: Mapped[str | None] = mapped_column(String(64), nullable=True)
    misconception_tag: Mapped[str | None] = mapped_column(String(128), nullable=True)
    metric_field: Mapped[str | None] = mapped_column(String(64), nullable=True)
    # Content kind: lesson / video / worked_example / practice.
    kind: Mapped[str] = mapped_column(String(32), nullable=False, default="lesson")
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False, default="")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)


class CoachConversation(Base):
    """A coach conversation (group of turns). One student may have many."""

    __tablename__ = "coach_conversations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), nullable=False, index=True
    )
    competency_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    initial_mode: Mapped[str] = mapped_column(String(32), nullable=False, default="LEARN")
    finished: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=_utcnow, onupdate=_utcnow, nullable=False
    )

    student: Mapped[Student] = relationship("Student", back_populates="coach_conversations")
    messages: Mapped[list[CoachMessage]] = relationship(
        "CoachMessage",
        back_populates="conversation",
        cascade="all, delete-orphan",
        order_by="CoachMessage.id",
    )


class CoachMessage(Base):
    """One message in a coach conversation (student or coach)."""

    __tablename__ = "coach_messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("coach_conversations.id"), nullable=False, index=True
    )
    sender: Mapped[str] = mapped_column(String(16), nullable=False)  # "student" / "coach"
    text: Mapped[str] = mapped_column(Text, nullable=False)
    mode: Mapped[str | None] = mapped_column(String(32), nullable=True)
    scaffolding_level: Mapped[str | None] = mapped_column(String(16), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    conversation: Mapped[CoachConversation] = relationship(
        "CoachConversation", back_populates="messages"
    )


class EvidenceEvent(Base):
    """One event on a student's evidence timeline."""

    __tablename__ = "evidence_events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), nullable=False, index=True
    )
    timestamp: Mapped[datetime] = mapped_column(
        DateTime, default=_utcnow, nullable=False, index=True
    )
    event_type: Mapped[str] = mapped_column(String(64), nullable=False)
    competency_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    detail: Mapped[str] = mapped_column(Text, nullable=False)
    result: Mapped[str] = mapped_column(String(8), nullable=False, default="INFO")

    student: Mapped[Student] = relationship("Student", back_populates="evidence_events")


class LessonProgress(Base):
    """One real lesson marked complete by a student.

    This is the durable record that drives per-course progress (which lessons
    of a course have actually been finished). ``course_code`` is denormalised
    so per-course aggregation never needs a join through the curriculum tree.
    """

    __tablename__ = "lesson_progress"
    __table_args__ = (
        UniqueConstraint("student_id", "lesson_code", name="uq_lesson_progress_student"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), nullable=False, index=True
    )
    course_code: Mapped[str] = mapped_column(String(32), nullable=False, index=True)
    course_title: Mapped[str] = mapped_column(String(255), nullable=False, default="")
    lesson_code: Mapped[str] = mapped_column(String(64), nullable=False)
    lesson_title: Mapped[str] = mapped_column(String(255), nullable=False, default="")
    completed_at: Mapped[datetime] = mapped_column(
        DateTime, default=_utcnow, nullable=False, index=True
    )

    student: Mapped[Student] = relationship("Student", back_populates="lesson_progress")


class PracticeResult(Base):
    """The latest outcome of a practice item for a student.

    One row per (student, item); the row is upserted on every grade so the
    last attempt wins. ``correct`` drives the completed-quizzes counts in the
    progress summary. ``course_code`` is denormalised for the same reason as
    ``LessonProgress.course_code``.
    """

    __tablename__ = "practice_results"
    __table_args__ = (
        UniqueConstraint("student_id", "item_id", name="uq_practice_result_student_item"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), nullable=False, index=True
    )
    course_code: Mapped[str] = mapped_column(String(32), nullable=False, index=True)
    lesson_code: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    item_id: Mapped[int] = mapped_column(Integer, nullable=False)
    correct: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    answered_at: Mapped[datetime] = mapped_column(
        DateTime, default=_utcnow, nullable=False, index=True
    )

    student: Mapped[Student] = relationship("Student", back_populates="practice_results")


class LabAttempt(Base):
    """One code-lab submission by a student.

    Rows are appended (never upserted) so the lab can compute real attempt
    counts, streaks and weak-topic analysis from history. ``correct`` is the
    truth of the *final* attempt; ``passed_tests`` / ``total_tests`` carry
    the underlying test verdicts for code challenges.
    """

    __tablename__ = "lab_attempts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("students.student_id"), nullable=False, index=True
    )
    course_code: Mapped[str] = mapped_column(String(32), nullable=False, default="CSE014")
    lesson_code: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    challenge_id: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    challenge_type: Mapped[str] = mapped_column(String(24), nullable=False)
    difficulty: Mapped[str] = mapped_column(String(16), nullable=False, default="easy")
    topic: Mapped[str] = mapped_column(String(64), nullable=False, default="")
    correct: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    passed_tests: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    total_tests: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    hints_used: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=_utcnow, nullable=False, index=True
    )

    student: Mapped[Student] = relationship("Student")


class AuditLog(Base):
    """Security-relevant action log.

    Records who did what, when, and with what outcome, for auth and
    instructor-read events. ``actor_user_id`` is nullable because events
    like failed logins may not resolve to a known user.
    """

    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime, default=_utcnow, nullable=False, index=True
    )
    actor_user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"), nullable=True, index=True
    )
    actor_role: Mapped[str] = mapped_column(String(16), nullable=False, default="student")
    action: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    target_type: Mapped[str | None] = mapped_column(String(64), nullable=True)
    target_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    detail: Mapped[str] = mapped_column(Text, nullable=False, default="")
    ip_address: Mapped[str | None] = mapped_column(String(64), nullable=True)
    outcome: Mapped[str] = mapped_column(String(16), nullable=False, default="OK")

    # Org scope: the university within which the event occurred (nullable
    # for global/system events that have no tenant).
    university_id: Mapped[int | None] = mapped_column(
        ForeignKey("universities.id"), nullable=True, index=True
    )


# ---------------------------------------------------------------------------
# Curriculum hierarchy (course → module → lesson → content).
#
# This is the durable, DB-backed content backbone for first-year university
# courses. Modules/lessons partition a course; a lesson carries ordered
# LessonContent blocks (TEXT/FORMULA/EXAMPLE/KEY_POINT/WARNING/TABLE/IMAGE/
# VIDEO/SUMMARY/DIFFICULT_CONCEPT…), LessonResource attachments (video
# lectures are VIDEO resources hiding scripts), and LessonCompetency links that
# tie the lesson into the existing Competency graph (so lessons feed the
# existing mastery/adaptive/evidence pipeline).
# ---------------------------------------------------------------------------


class Module(Base):
    """A module (unit) within a course (e.g. 'Electrostatics')."""

    __tablename__ = "modules"
    __table_args__ = (UniqueConstraint("course_id", "code", name="uq_modules_course_code"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False, index=True)
    code: Mapped[str] = mapped_column(String(32), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    course: Mapped[Course | None] = relationship("Course", back_populates="modules")
    lessons: Mapped[list[Lesson]] = relationship(
        "Lesson",
        back_populates="module",
        cascade="all, delete-orphan",
        order_by="Lesson.sort_order",
    )


class Lesson(Base):
    """One deliverable session inside a module.

    ``objectives_json`` holds the intended learning outcomes for this lesson;
    ``prerequisites_json`` lists the lesson codes that should come before it.
    Both are JSON-stored to keep the schema stable while content evolves.
    """

    __tablename__ = "lessons"
    __table_args__ = (UniqueConstraint("module_id", "code", name="uq_lessons_module_code"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    module_id: Mapped[int] = mapped_column(ForeignKey("modules.id"), nullable=False, index=True)
    code: Mapped[str] = mapped_column(String(64), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    estimated_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    difficulty: Mapped[str] = mapped_column(String(16), nullable=False, default="beginner")
    objectives_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    prerequisites_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    module: Mapped[Module | None] = relationship("Module", back_populates="lessons")
    contents: Mapped[list[LessonContent]] = relationship(
        "LessonContent",
        back_populates="lesson",
        cascade="all, delete-orphan",
        order_by="LessonContent.sort_order",
    )
    resources: Mapped[list[LessonResource]] = relationship(
        "LessonResource",
        back_populates="lesson",
        cascade="all, delete-orphan",
        order_by="LessonResource.sort_order",
    )
    competencies: Mapped[list[LessonCompetency]] = relationship(
        "LessonCompetency", back_populates="lesson", cascade="all, delete-orphan"
    )
    practice_items: Mapped[list[PracticeItem]] = relationship(
        "PracticeItem",
        back_populates="lesson",
        cascade="all, delete-orphan",
        order_by="PracticeItem.sort_order",
    )


class LessonContent(Base):
    """One ordered content block of a lesson.

    ``section_type`` is one of TEXT / FORMULA / EXAMPLE / KEY_POINT / WARNING /
    TABLE / IMAGE / VIDEO / SUMMARY / DIFFICULT_CONCEPT. The API never renders
    the whole lesson on one page: lecture uses the teaching blocks, summary the
    SUMMARY + KEY_POINT blocks, videos the VIDEO resources, practice the
    ``practice_items``.
    """

    __tablename__ = "lesson_contents"
    __table_args__ = (
        UniqueConstraint("lesson_id", "sort_order", name="uq_lesson_contents_section"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"), nullable=False, index=True)
    section_type: Mapped[str] = mapped_column(String(32), nullable=False)
    title: Mapped[str | None] = mapped_column(String(255), nullable=True)
    body: Mapped[str] = mapped_column(Text, nullable=False, default="")
    metadata_json: Mapped[str] = mapped_column(Text, nullable=False, default="{}")
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    lesson: Mapped[Lesson | None] = relationship("Lesson", back_populates="contents")


class LessonResource(Base):
    """An attachment to a lesson (video lecture, PDF, external link, …).

    Video resources hide the script/check until the learner asks for them —
    the API returns scripts only on the explicit ``/videos`` detail view.
    """

    __tablename__ = "lesson_resources"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"), nullable=False, index=True)
    resource_type: Mapped[str] = mapped_column(String(32), nullable=False, default="LINK")
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    external_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    duration_seconds: Mapped[int | None] = mapped_column(Integer, nullable=True)
    metadata_json: Mapped[str] = mapped_column(Text, nullable=False, default="{}")
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    lesson: Mapped[Lesson | None] = relationship("Lesson", back_populates="resources")


class LessonCompetency(Base):
    """Link table mapping a lesson to the competencies it teaches.

    ``role`` distinguishes how the lesson relates to the competency
    (``teaches`` / ``reinforces`` / ``assesses``). Links let the adaptive and
    evidence engines route lessons through the existing competency graph.
    """

    __tablename__ = "lesson_competencies"
    __table_args__ = (
        UniqueConstraint("lesson_id", "competency_id", name="uq_lesson_competency_link"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"), nullable=False, index=True)
    competency_id: Mapped[int] = mapped_column(
        ForeignKey("competencies.id"), nullable=False, index=True
    )
    role: Mapped[str] = mapped_column(String(32), nullable=False, default="teaches")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    lesson: Mapped[Lesson | None] = relationship("Lesson", back_populates="competencies")
    competency: Mapped[Competency | None] = relationship("Competency")


class PracticeItem(Base):
    """One practice/check question for a lesson.

    ``level`` is UNDERSTAND (1) / APPLY (2) / TRANSFER (3). Answers live
    server-side only (``answer_json`` is never returned by the practice API);
    grading routes through the existing evidence pipeline via the linked
    competency, so practice feeds mastery/adaptive without a competing
    assessment system.
    """

    __tablename__ = "practice_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"), nullable=False, index=True)
    competency_id: Mapped[int | None] = mapped_column(
        ForeignKey("competencies.id"), nullable=True, index=True
    )
    level: Mapped[str] = mapped_column(String(16), nullable=False, default="UNDERSTAND")
    prompt: Mapped[str] = mapped_column(Text, nullable=False)
    options_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    answer_json: Mapped[str] = mapped_column(Text, nullable=False, default="{}")
    explanation: Mapped[str] = mapped_column(Text, nullable=False, default="")
    skill: Mapped[str | None] = mapped_column(String(64), nullable=True)
    difficulty: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, nullable=False)

    lesson: Mapped[Lesson | None] = relationship("Lesson", back_populates="practice_items")
