"""CRUD operations for the Arete platform.

Each function takes a SQLAlchemy ``Session`` as the first argument so
callers control transaction boundaries. Functions don't commit — the
caller is responsible for committing (or rolling back on error).

This keeps the DB layer thin and testable: services call these functions
inside a ``with db:`` block (or use ``Depends(get_db)`` in routers).
"""

from __future__ import annotations

import json
from datetime import UTC, datetime

from sqlalchemy import func
from sqlalchemy.orm import Session

from . import models

# ---- User ----------------------------------------------------------------


def _normalize_email(email: str) -> str:
    return email.strip().lower()


def _normalize_username(username: str) -> str:
    return username.strip().lower()


def create_user(
    db: Session,
    *,
    email: str,
    username: str,
    name: str,
    password_hash: str | None = None,
    role: str = "student",
    university_id: int | None = None,
    email_verified: bool = False,
) -> models.User:
    user = models.User(
        email=_normalize_email(email),
        username=_normalize_username(username),
        name=name,
        password_hash=password_hash,
        role=role,
        university_id=university_id,
        email_verified=email_verified,
    )
    db.add(user)
    db.flush()
    return user


def get_user_by_email(db: Session, email: str) -> models.User | None:
    return (
        db.query(models.User)
        .filter(func.lower(models.User.email) == _normalize_email(email))
        .first()
    )


def get_user_by_username(db: Session, username: str) -> models.User | None:
    return (
        db.query(models.User)
        .filter(func.lower(models.User.username) == _normalize_username(username))
        .first()
    )


def get_user_by_id(db: Session, user_id: int) -> models.User | None:
    return db.query(models.User).filter(models.User.id == user_id).first()


def set_user_verification(
    db: Session,
    *,
    user: models.User,
    code_hash: str,
    expires_at: datetime,
    sent_at: datetime,
) -> None:
    """Store a fresh (unexpired) verification code for a user."""
    user.email_verified = False
    user.email_verification_code_hash = code_hash
    user.email_verification_expires_at = expires_at
    user.email_verification_sent_at = sent_at
    db.flush()


def mark_user_verified(db: Session, *, user: models.User) -> None:
    """Clear the verification code and mark the account as verified."""
    user.email_verified = True
    user.email_verification_code_hash = None
    user.email_verification_expires_at = None
    user.email_verification_sent_at = None
    db.flush()


def set_user_password_reset(
    db: Session,
    *,
    user: models.User,
    code_hash: str,
    expires_at: datetime,
    sent_at: datetime,
) -> None:
    """Store a fresh (unexpired) password-reset code for a user."""
    user.password_reset_code_hash = code_hash
    user.password_reset_expires_at = expires_at
    user.password_reset_sent_at = sent_at
    db.flush()


def clear_user_password_reset(db: Session, *, user: models.User) -> None:
    """Invalidate any pending password-reset code (after use/expiry)."""
    user.password_reset_code_hash = None
    user.password_reset_expires_at = None
    user.password_reset_sent_at = None
    db.flush()


def bump_token_version(db: Session, *, user: models.User) -> None:
    """Invalidate every previously issued JWT for this user."""
    user.token_version += 1
    db.flush()


# ---- Student --------------------------------------------------------------


def create_student(
    db: Session,
    *,
    student_id: str,
    user_id: int,
    display_name: str,
    course_code: str = "MEC271",
    course_title: str = "Automatic Control",
    overall_progress: int = 0,
    university_id: int | None = None,
) -> models.Student:
    student = models.Student(
        student_id=student_id,
        user_id=user_id,
        display_name=display_name,
        course_code=course_code,
        course_title=course_title,
        overall_progress=overall_progress,
        university_id=university_id,
    )
    db.add(student)
    db.flush()
    return student


def get_student_by_id(db: Session, student_id: str) -> models.Student | None:
    return db.query(models.Student).filter(models.Student.student_id == student_id).first()


def get_students_by_user_id(db: Session, user_id: int) -> list[models.Student]:
    return db.query(models.Student).filter(models.Student.user_id == user_id).all()


def list_all_students(db: Session) -> list[models.Student]:
    return db.query(models.Student).order_by(models.Student.display_name).all()


def update_student_progress(db: Session, student_id: str, overall_progress: int) -> None:
    db.query(models.Student).filter(models.Student.student_id == student_id).update(
        {"overall_progress": overall_progress}
    )


# ---- Organization (university identity / multi-tenant) ----------------------


def get_university_by_id(db: Session, university_id: int) -> models.University | None:
    return db.query(models.University).filter(models.University.id == university_id).first()


def get_university_by_code(db: Session, code: str) -> models.University | None:
    return (
        db.query(models.University).filter(models.University.code == code.strip().upper()).first()
    )


def list_universities(db: Session) -> list[models.University]:
    return db.query(models.University).order_by(models.University.name).all()


def create_university(
    db: Session, *, code: str, name: str, email_domains: list[str] | None = None
) -> models.University:
    import json

    university = models.University(
        code=code.strip().upper(),
        name=name.strip(),
        email_domains=json.dumps(email_domains or []),
        is_active=True,
    )
    db.add(university)
    db.flush()
    return university


def get_faculties_for_university(db: Session, university_id: int) -> list[models.Faculty]:
    return (
        db.query(models.Faculty)
        .filter(models.Faculty.university_id == university_id)
        .order_by(models.Faculty.name)
        .all()
    )


def create_faculty(db: Session, *, university_id: int, code: str, name: str) -> models.Faculty:
    faculty = models.Faculty(
        university_id=university_id, code=code.strip().upper(), name=name.strip()
    )
    db.add(faculty)
    db.flush()
    return faculty


def get_departments_for_faculty(db: Session, faculty_id: int) -> list[models.Department]:
    return (
        db.query(models.Department)
        .filter(models.Department.faculty_id == faculty_id)
        .order_by(models.Department.name)
        .all()
    )


def create_department(db: Session, *, faculty_id: int, code: str, name: str) -> models.Department:
    dept = models.Department(faculty_id=faculty_id, code=code.strip().upper(), name=name.strip())
    db.add(dept)
    db.flush()
    return dept


def get_courses_for_department(db: Session, department_id: int) -> list[models.Course]:
    return (
        db.query(models.Course)
        .filter(models.Course.department_id == department_id)
        .order_by(models.Course.code)
        .all()
    )


def create_course(
    db: Session,
    *,
    department_id: int,
    code: str,
    title: str,
    credits: int = 3,
) -> models.Course:
    course = models.Course(
        department_id=department_id,
        code=code.strip().upper(),
        title=title.strip(),
        credits=credits,
    )
    db.add(course)
    db.flush()
    return course


def get_sections_for_course(db: Session, course_id: int) -> list[models.Section]:
    return (
        db.query(models.Section)
        .filter(models.Section.course_id == course_id)
        .order_by(models.Section.term, models.Section.code)
        .all()
    )


def create_section(
    db: Session,
    *,
    course_id: int,
    term: str,
    code: str,
    instructor_user_id: int | None = None,
) -> models.Section:
    section = models.Section(
        course_id=course_id,
        term=term.strip().upper(),
        code=code.strip().upper(),
        instructor_user_id=instructor_user_id,
    )
    db.add(section)
    db.flush()
    return section


def get_section_by_id(db: Session, section_id: int) -> models.Section | None:
    return db.query(models.Section).filter(models.Section.id == section_id).first()


def enroll_student_in_section(
    db: Session, *, student_id: str, section_id: int
) -> models.Enrollment:
    existing = (
        db.query(models.Enrollment)
        .filter(
            models.Enrollment.student_id == student_id,
            models.Enrollment.section_id == section_id,
        )
        .first()
    )
    if existing is not None:
        return existing
    enrollment = models.Enrollment(student_id=student_id, section_id=section_id, status="active")
    db.add(enrollment)
    db.flush()
    return enrollment


def unenroll_student_from_section(db: Session, *, student_id: str, section_id: int) -> bool:
    deleted = (
        db.query(models.Enrollment)
        .filter(
            models.Enrollment.student_id == student_id,
            models.Enrollment.section_id == section_id,
        )
        .delete()
    )
    db.flush()
    return deleted > 0


def get_students_in_section(db: Session, section_id: int) -> list[models.Student]:
    return (
        db.query(models.Student)
        .join(models.Enrollment, models.Enrollment.student_id == models.Student.student_id)
        .filter(models.Enrollment.section_id == section_id)
        .order_by(models.Student.display_name)
        .all()
    )


def get_sections_for_student(db: Session, student_id: str) -> list[models.Section]:
    return (
        db.query(models.Section)
        .join(models.Enrollment, models.Enrollment.section_id == models.Section.id)
        .filter(models.Enrollment.student_id == student_id)
        .all()
    )


def get_sections_for_instructor(db: Session, instructor_user_id: int) -> list[models.Section]:
    return (
        db.query(models.Section)
        .filter(models.Section.instructor_user_id == instructor_user_id)
        .order_by(models.Section.term, models.Section.code)
        .all()
    )


def get_students_for_instructor(db: Session, instructor_user_id: int) -> list[models.Student]:
    """All distinct students enrolled in any section the instructor teaches."""
    section_ids = [s.id for s in get_sections_for_instructor(db, instructor_user_id)]
    if not section_ids:
        return []
    return (
        db.query(models.Student)
        .join(models.Enrollment, models.Enrollment.student_id == models.Student.student_id)
        .filter(models.Enrollment.section_id.in_(section_ids))
        .distinct()
        .order_by(models.Student.display_name)
        .all()
    )


# ---- Competency snapshot --------------------------------------------------


def get_competencies(db: Session, student_id: str) -> list[models.CompetencySnapshot]:
    return (
        db.query(models.CompetencySnapshot)
        .filter(models.CompetencySnapshot.student_id == student_id)
        .order_by(models.CompetencySnapshot.id)
        .all()
    )


def get_all_competencies(db: Session) -> list[models.CompetencySnapshot]:
    return db.query(models.CompetencySnapshot).order_by(models.CompetencySnapshot.id).all()


def upsert_competency(
    db: Session,
    *,
    student_id: str,
    competency_id: str,
    competency_name: str,
    status: str,
    progress: int,
) -> models.CompetencySnapshot:
    existing = (
        db.query(models.CompetencySnapshot)
        .filter(
            models.CompetencySnapshot.student_id == student_id,
            models.CompetencySnapshot.competency_id == competency_id,
        )
        .first()
    )
    if existing is None:
        snap = models.CompetencySnapshot(
            student_id=student_id,
            competency_id=competency_id,
            competency_name=competency_name,
            status=status,
            progress=progress,
        )
        db.add(snap)
        db.flush()
        return snap
    existing.status = status
    existing.progress = progress
    existing.competency_name = competency_name
    db.flush()
    return existing


# ---- Competency (durable graph node) -------------------------------------


def get_competency_by_code(db: Session, *, course_id: int, code: str) -> models.Competency | None:
    """Fetch a durable competency definition by its stable course-scoped code."""
    return (
        db.query(models.Competency)
        .filter(models.Competency.course_id == course_id, models.Competency.code == code)
        .first()
    )


def ensure_competency(
    db: Session,
    *,
    course_id: int,
    code: str,
    title: str,
    description: str = "",
    taxonomy_level: str | None = None,
    sort_order: int = 0,
) -> models.Competency:
    """Get-or-create a durable competency definition for a course.

    Idempotent by ``(course_id, code)`` — the stable slug. Used for the
    initial competency backfill so every course gets its graph seeded exactly
    once. Does NOT touch ``CompetencySnapshot`` (that's the derived view).
    """
    existing = get_competency_by_code(db, course_id=course_id, code=code)
    if existing is not None:
        return existing
    comp = models.Competency(
        course_id=course_id,
        code=code,
        title=title,
        description=description,
        taxonomy_level=taxonomy_level,
        sort_order=sort_order,
    )
    db.add(comp)
    db.flush()
    return comp


def get_competencies_for_course(db: Session, course_id: int) -> list[models.Competency]:
    return (
        db.query(models.Competency)
        .filter(models.Competency.course_id == course_id)
        .order_by(models.Competency.sort_order, models.Competency.id)
        .all()
    )


def ensure_competency_prerequisite(
    db: Session,
    *,
    course_id: int,
    pre_competency_id: int,
    post_competency_id: int,
) -> models.CompetencyPrerequisite:
    """Get-or-create a directed graph edge ``pre -> post`` (idempotent).

    The (course_id, pre, post) tuple is unique, so repeated backfills never
    duplicate edges.
    """
    existing = (
        db.query(models.CompetencyPrerequisite)
        .filter(
            models.CompetencyPrerequisite.course_id == course_id,
            models.CompetencyPrerequisite.pre_competency_id == pre_competency_id,
            models.CompetencyPrerequisite.post_competency_id == post_competency_id,
        )
        .first()
    )
    if existing is not None:
        return existing
    edge = models.CompetencyPrerequisite(
        course_id=course_id,
        pre_competency_id=pre_competency_id,
        post_competency_id=post_competency_id,
    )
    db.add(edge)
    db.flush()
    return edge


# ---- Assessment + rubric --------------------------------------------------


def get_assessments_for_competency(
    db: Session, *, competency_id: int, active_only: bool = True
) -> list[models.Assessment]:
    q = db.query(models.Assessment).filter(models.Assessment.competency_id == competency_id)
    if active_only:
        q = q.filter(models.Assessment.is_active.is_(True))
    return q.order_by(models.Assessment.id).all()


def get_assessment(db: Session, *, assessment_id: int) -> models.Assessment | None:
    return db.query(models.Assessment).filter(models.Assessment.id == assessment_id).first()


def ensure_assessment(
    db: Session,
    *,
    competency_id: int,
    title: str,
    kind: str = "MASTERY",
    pass_rule: str = "{}",
    rubric_spec: str = "[]",
) -> models.Assessment:
    """Get-or-create an assessment for a competency (unique by title)."""
    existing = (
        db.query(models.Assessment)
        .filter(
            models.Assessment.competency_id == competency_id,
            models.Assessment.title == title,
        )
        .first()
    )
    if existing is not None:
        return existing
    assessment = models.Assessment(
        competency_id=competency_id,
        title=title,
        kind=kind,
        pass_rule=pass_rule,
        rubric_spec=rubric_spec,
    )
    db.add(assessment)
    db.flush()
    return assessment


def ensure_assessment_task(
    db: Session,
    *,
    assessment_id: int,
    code: str,
    prompt: str,
    metric_field: str | None = None,
    sort_order: int = 0,
) -> models.AssessmentTask:
    """Get-or-create an objective probe within an assessment."""
    existing = (
        db.query(models.AssessmentTask)
        .filter(
            models.AssessmentTask.assessment_id == assessment_id,
            models.AssessmentTask.code == code,
        )
        .first()
    )
    if existing is not None:
        return existing
    task = models.AssessmentTask(
        assessment_id=assessment_id,
        code=code,
        prompt=prompt,
        metric_field=metric_field,
        sort_order=sort_order,
    )
    db.add(task)
    db.flush()
    return task


def ensure_rubric_criterion(
    db: Session,
    *,
    assessment_id: int,
    metric_field: str,
    operator: str,
    threshold: float | None = None,
    mandatory: bool = True,
) -> models.AssessmentRubricCriterion:
    """Get-or-create one rubric criterion (unique by assessment+metric)."""
    existing = (
        db.query(models.AssessmentRubricCriterion)
        .filter(
            models.AssessmentRubricCriterion.assessment_id == assessment_id,
            models.AssessmentRubricCriterion.metric_field == metric_field,
        )
        .first()
    )
    if existing is not None:
        return existing
    criterion = models.AssessmentRubricCriterion(
        assessment_id=assessment_id,
        metric_field=metric_field,
        operator=operator,
        threshold=threshold,
        mandatory=mandatory,
    )
    db.add(criterion)
    db.flush()
    return criterion


def get_rubric(db: Session, *, assessment_id: int) -> list[models.AssessmentRubricCriterion]:
    return (
        db.query(models.AssessmentRubricCriterion)
        .filter(models.AssessmentRubricCriterion.assessment_id == assessment_id)
        .order_by(models.AssessmentRubricCriterion.id)
        .all()
    )


# ---- Assessment attempt ----------------------------------------------------


def next_attempt_number(db: Session, *, assessment_id: int, student_id: str) -> int:
    """Next attempt number for (assessment, student) — 1 + max existing."""
    last = (
        db.query(models.AssessmentAttempt)
        .filter(
            models.AssessmentAttempt.assessment_id == assessment_id,
            models.AssessmentAttempt.student_id == student_id,
        )
        .order_by(models.AssessmentAttempt.attempt_number.desc())
        .first()
    )
    return (last.attempt_number + 1) if last is not None else 1


def create_attempt_open(
    db: Session,
    *,
    assessment_id: int,
    student_id: str,
) -> models.AssessmentAttempt:
    """Open a new IN_PROGRESS attempt for (assessment, student)."""
    attempt_number = next_attempt_number(db, assessment_id=assessment_id, student_id=student_id)
    attempt = models.AssessmentAttempt(
        assessment_id=assessment_id,
        student_id=student_id,
        attempt_number=attempt_number,
        status="IN_PROGRESS",
    )
    db.add(attempt)
    db.flush()
    return attempt


def get_open_attempt(
    db: Session, *, assessment_id: int, student_id: str
) -> models.AssessmentAttempt | None:
    return (
        db.query(models.AssessmentAttempt)
        .filter(
            models.AssessmentAttempt.assessment_id == assessment_id,
            models.AssessmentAttempt.student_id == student_id,
            models.AssessmentAttempt.status == "IN_PROGRESS",
        )
        .order_by(models.AssessmentAttempt.id.desc())
        .first()
    )


def get_attempts_for_student(
    db: Session, *, assessment_id: int, student_id: str
) -> list[models.AssessmentAttempt]:
    return (
        db.query(models.AssessmentAttempt)
        .filter(
            models.AssessmentAttempt.assessment_id == assessment_id,
            models.AssessmentAttempt.student_id == student_id,
        )
        .order_by(models.AssessmentAttempt.attempt_number)
        .all()
    )


# ---- Evidence record -------------------------------------------------------


def add_evidence(
    db: Session,
    *,
    student_id: str,
    competency_id: int,
    source_type: str,
    metric_json: str,
    source_ref_id: int | None = None,
    context_json: str = "{}",
) -> models.EvidenceRecord:
    """Append one immutable piece of evidence to a student's timeline."""
    record = models.EvidenceRecord(
        student_id=student_id,
        competency_id=competency_id,
        source_type=source_type,
        source_ref_id=source_ref_id,
        metric_json=metric_json,
        context_json=context_json,
    )
    db.add(record)
    db.flush()
    return record


def get_evidence_for_competency(
    db: Session, *, student_id: str, competency_id: int
) -> list[models.EvidenceRecord]:
    return (
        db.query(models.EvidenceRecord)
        .filter(
            models.EvidenceRecord.student_id == student_id,
            models.EvidenceRecord.competency_id == competency_id,
        )
        .order_by(models.EvidenceRecord.created_at)
        .all()
    )


def get_all_evidence(db: Session, *, student_id: str) -> list[models.EvidenceRecord]:
    return (
        db.query(models.EvidenceRecord)
        .filter(models.EvidenceRecord.student_id == student_id)
        .order_by(models.EvidenceRecord.created_at)
        .all()
    )


# ---- Mastery record --------------------------------------------------------


def get_mastery_history(
    db: Session, *, student_id: str, competency_id: int
) -> list[models.MasteryRecord]:
    """Immutable mastery history for (student, competency), oldest first."""
    return (
        db.query(models.MasteryRecord)
        .filter(
            models.MasteryRecord.student_id == student_id,
            models.MasteryRecord.competency_id == competency_id,
        )
        .order_by(models.MasteryRecord.created_at, models.MasteryRecord.id)
        .all()
    )


def get_latest_mastery(
    db: Session, *, student_id: str, competency_id: int
) -> models.MasteryRecord | None:
    """Most recent mastery resolution for (student, competency)."""
    return (
        db.query(models.MasteryRecord)
        .filter(
            models.MasteryRecord.student_id == student_id,
            models.MasteryRecord.competency_id == competency_id,
        )
        .order_by(models.MasteryRecord.created_at.desc(), models.MasteryRecord.id.desc())
        .first()
    )


def add_mastery_record(
    db: Session,
    *,
    student_id: str,
    competency_id: int,
    level: str,
    rubric_json: str = "{}",
    reason_codes_json: str = "[]",
    evidence_ids_json: str = "[]",
) -> models.MasteryRecord:
    """Append an immutable mastery assertion (never update in place)."""
    record = models.MasteryRecord(
        student_id=student_id,
        competency_id=competency_id,
        level=level,
        rubric_json=rubric_json,
        reason_codes_json=reason_codes_json,
        evidence_ids_json=evidence_ids_json,
    )
    db.add(record)
    db.flush()
    return record


# ---- Onboarding -----------------------------------------------------------


def save_onboarding(
    db: Session,
    *,
    student_id: str,
    learning_challenge: str,
    preferred_method: str,
    obstacle: str,
    goal: str,
) -> models.OnboardingAnswer:
    existing = (
        db.query(models.OnboardingAnswer)
        .filter(models.OnboardingAnswer.student_id == student_id)
        .first()
    )
    if existing is not None:
        existing.learning_challenge = learning_challenge
        existing.preferred_method = preferred_method
        existing.obstacle = obstacle
        existing.goal = goal
        db.flush()
        return existing
    ans = models.OnboardingAnswer(
        student_id=student_id,
        learning_challenge=learning_challenge,
        preferred_method=preferred_method,
        obstacle=obstacle,
        goal=goal,
    )
    db.add(ans)
    db.flush()
    return ans


# ---- Diagnostic -----------------------------------------------------------


def save_diagnostic_submission(
    db: Session,
    *,
    student_id: str,
    score: int,
    total: int,
    misconceptions_count: int,
    answers: list[dict],
) -> models.DiagnosticSubmission:
    sub = models.DiagnosticSubmission(
        student_id=student_id,
        score=score,
        total=total,
        misconceptions_count=misconceptions_count,
    )
    db.add(sub)
    db.flush()
    for a in answers:
        db.add(
            models.DiagnosticAnswer(
                submission_id=sub.id,
                question_id=a["question_id"],
                competency_id=a["competency_id"],
                selected_option_id=a["selected_option_id"],
                correct=a["correct"],
                misconception_tag=a.get("misconception_tag"),
            )
        )
    db.flush()
    return sub


# ---- Simulation -----------------------------------------------------------


def save_simulation_run(
    db: Session,
    *,
    student_id: str,
    competency_id: str,
    task_id: str,
    attempt: int,
    kp: float,
    ki: float,
    kd: float,
    stable: bool,
    overshoot: float,
    settling_time: float,
    rise_time: float,
    steady_state_error: float,
    requirements_met: bool,
    result: str,
    misconception: str | None,
) -> models.SimulationRun:
    run = models.SimulationRun(
        student_id=student_id,
        competency_id=competency_id,
        task_id=task_id,
        attempt=attempt,
        kp=kp,
        ki=ki,
        kd=kd,
        stable=stable,
        overshoot=overshoot,
        settling_time=settling_time,
        rise_time=rise_time,
        steady_state_error=steady_state_error,
        requirements_met=requirements_met,
        result=result,
        misconception=misconception,
    )
    db.add(run)
    db.flush()
    return run


def list_simulation_runs(
    db: Session, student_id: str, competency_id: str | None = None
) -> list[models.SimulationRun]:
    q = db.query(models.SimulationRun).filter(models.SimulationRun.student_id == student_id)
    if competency_id:
        q = q.filter(models.SimulationRun.competency_id == competency_id)
    return q.order_by(models.SimulationRun.id.desc()).all()


# ---- Transfer -------------------------------------------------------------


def save_transfer_evaluation(
    db: Session,
    *,
    student_id: str,
    competency_id: str,
    scenario_id: str,
    response_text: str,
    passed: bool,
    matched_count: int,
    min_required: int,
    feedback: str,
) -> models.TransferEvaluation:
    ev = models.TransferEvaluation(
        student_id=student_id,
        competency_id=competency_id,
        scenario_id=scenario_id,
        response_text=response_text,
        passed=passed,
        matched_count=matched_count,
        min_required=min_required,
        feedback=feedback,
    )
    db.add(ev)
    db.flush()
    return ev


# ---- Remediation ----------------------------------------------------------


def save_remediation_plan(
    db: Session,
    *,
    student_id: str,
    competency_id: str,
    detected_misconception: str | None,
    recommended_action: str,
    conceptual_focus: str,
    guided_question: str,
    consecutive_failures: int,
    total_attempts: int,
    summary_text: str,
    remediation_steps: list[str],
    evidence_id: int | None = None,
    reason_codes_json: str = "[]",
    status: str = "open",
    completed_at=None,
) -> models.RemediationPlan:
    plan = models.RemediationPlan(
        student_id=student_id,
        competency_id=competency_id,
        detected_misconception=detected_misconception,
        recommended_action=recommended_action,
        conceptual_focus=conceptual_focus,
        guided_question=guided_question,
        consecutive_failures=consecutive_failures,
        total_attempts=total_attempts,
        summary_text=summary_text,
        remediation_steps_json=json.dumps(remediation_steps),
        evidence_id=evidence_id,
        reason_codes_json=reason_codes_json,
        status=status,
        completed_at=completed_at,
    )
    db.add(plan)
    db.flush()
    return plan


# ---- Remediation plan (4E) lifecycle queries ---------------------------------


def get_remediation_plan(db: Session, *, plan_id: int) -> models.RemediationPlan | None:
    return db.query(models.RemediationPlan).filter(models.RemediationPlan.id == plan_id).first()


def get_open_remediation_plans(
    db: Session, *, student_id: str, competency_id: str
) -> list[models.RemediationPlan]:
    """Open (not-yet-completed) plans for (student, competency), newest first."""
    return (
        db.query(models.RemediationPlan)
        .filter(
            models.RemediationPlan.student_id == student_id,
            models.RemediationPlan.competency_id == competency_id,
            models.RemediationPlan.status == "open",
        )
        .order_by(models.RemediationPlan.created_at.desc())
        .all()
    )


def get_remediation_plans_for_student(
    db: Session, *, student_id: str, include_completed: bool = True
) -> list[models.RemediationPlan]:
    q = db.query(models.RemediationPlan).filter(models.RemediationPlan.student_id == student_id)
    if not include_completed:
        q = q.filter(models.RemediationPlan.status == "open")
    return q.order_by(models.RemediationPlan.created_at.desc()).all()


def get_remediation_plan_for_evidence(
    db: Session, *, evidence_id: int
) -> models.RemediationPlan | None:
    """The latest plan tied to a specific evidence record (if any)."""
    return (
        db.query(models.RemediationPlan)
        .filter(models.RemediationPlan.evidence_id == evidence_id)
        .order_by(models.RemediationPlan.created_at.desc())
        .first()
    )


def complete_remediation_plan(db: Session, *, plan_id: int) -> models.RemediationPlan | None:
    """Mark an open plan as completed (used when the retry succeeds)."""
    plan = db.query(models.RemediationPlan).filter(models.RemediationPlan.id == plan_id).first()
    if plan is None:
        return None
    plan.status = "completed"
    plan.completed_at = datetime.now(UTC)
    db.flush()
    return plan


# ---- Remediation resource catalog (5E) --------------------------------------


def ensure_remediation_resource(
    db: Session,
    *,
    resource_code: str,
    title: str,
    body: str = "",
    kind: str = "lesson",
    competency_code: str | None = None,
    misconception_tag: str | None = None,
    metric_field: str | None = None,
    sort_order: int = 0,
    is_active: bool = True,
) -> models.RemediationResource:
    """Get-or-insert one catalog row, keyed on ``resource_code``.

    Idempotent, so the bootstrap backfill can run on every DB seed without
    duplicating content.
    """
    existing = (
        db.query(models.RemediationResource)
        .filter(models.RemediationResource.resource_code == resource_code)
        .first()
    )
    if existing is not None:
        return existing
    row = models.RemediationResource(
        resource_code=resource_code,
        title=title,
        body=body,
        kind=kind,
        competency_code=competency_code,
        misconception_tag=misconception_tag,
        metric_field=metric_field,
        sort_order=sort_order,
        is_active=is_active,
    )
    db.add(row)
    db.flush()
    return row


def get_active_remediation_resources(
    db: Session, *, competency_code: str | None = None
) -> list[models.RemediationResource]:
    """Active catalog rows, deterministic order: sort_order then id.

    When ``competency_code`` is given, competency-scoped rows are promoted
    first; generic (null competency) rows follow. The selector scoring in
    ``adaptive_engine`` sits on top of this.
    """
    q = db.query(models.RemediationResource).filter(models.RemediationResource.is_active.is_(True))
    if competency_code is not None:
        q = q.filter(
            (models.RemediationResource.competency_code == competency_code)
            | (models.RemediationResource.competency_code.is_(None))
        )
    return q.order_by(
        models.RemediationResource.sort_order.asc(), models.RemediationResource.id.asc()
    ).all()


# ---- Coach conversations --------------------------------------------------


def create_conversation(
    db: Session,
    *,
    student_id: str,
    competency_id: str | None,
    initial_mode: str,
) -> models.CoachConversation:
    conv = models.CoachConversation(
        student_id=student_id,
        competency_id=competency_id,
        initial_mode=initial_mode,
    )
    db.add(conv)
    db.flush()
    return conv


def add_message(
    db: Session,
    *,
    conversation_id: int,
    sender: str,
    text: str,
    mode: str | None = None,
    scaffolding_level: str | None = None,
) -> models.CoachMessage:
    msg = models.CoachMessage(
        conversation_id=conversation_id,
        sender=sender,
        text=text,
        mode=mode,
        scaffolding_level=scaffolding_level,
    )
    db.add(msg)
    db.flush()
    return msg


def get_latest_conversation(db: Session, student_id: str) -> models.CoachConversation | None:
    return (
        db.query(models.CoachConversation)
        .filter(models.CoachConversation.student_id == student_id)
        .order_by(models.CoachConversation.id.desc())
        .first()
    )


def list_conversations(db: Session, student_id: str) -> list[models.CoachConversation]:
    return (
        db.query(models.CoachConversation)
        .filter(models.CoachConversation.student_id == student_id)
        .order_by(models.CoachConversation.id.desc())
        .all()
    )


# ---- Evidence events ------------------------------------------------------


def append_evidence_event(
    db: Session,
    *,
    student_id: str,
    event_type: str,
    title: str,
    detail: str,
    result: str = "INFO",
    competency_id: str | None = None,
    timestamp: datetime | None = None,
) -> models.EvidenceEvent:
    ev = models.EvidenceEvent(
        student_id=student_id,
        event_type=event_type,
        title=title,
        detail=detail,
        result=result,
        competency_id=competency_id,
        timestamp=timestamp or datetime.now(UTC).replace(tzinfo=None),
    )
    db.add(ev)
    db.flush()
    return ev


def list_evidence_events(
    db: Session, student_id: str, newest_first: bool = True
) -> list[models.EvidenceEvent]:
    q = db.query(models.EvidenceEvent).filter(models.EvidenceEvent.student_id == student_id)
    if newest_first:
        q = q.order_by(models.EvidenceEvent.id.desc())
    else:
        q = q.order_by(models.EvidenceEvent.id.asc())
    return q.all()


# ---- Audit log -------------------------------------------------------------

_MAX_DETAIL_LENGTH = 2000


def add_audit_log(
    db: Session,
    *,
    actor_user_id: int | None,
    actor_role: str,
    action: str,
    target_type: str | None = None,
    target_id: str | None = None,
    detail: str = "",
    ip_address: str | None = None,
    outcome: str = "OK",
    university_id: int | None = None,
) -> models.AuditLog:
    """Record one security-relevant event in the audit trail.

    Caller commits (the callers that write audit rows already own a
    transaction). ``detail`` is truncated to keep the log bounded.
    """
    entry = models.AuditLog(
        actor_user_id=actor_user_id,
        actor_role=actor_role,
        action=action,
        target_type=target_type,
        target_id=target_id,
        detail=detail[:_MAX_DETAIL_LENGTH],
        ip_address=ip_address,
        outcome=outcome,
        university_id=university_id,
    )
    db.add(entry)
    db.flush()
    return entry
