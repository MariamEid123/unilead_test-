"""Idempotent default-organization bootstrap (Sprint 3, Curriculum pivot).

The platform ships with one seeded tenant — the "Arete Academy" default
organization — so that existing accounts and the untouched frontend keep
working while universities are being provisioned. Any user/student with a
``NULL`` ``university_id`` is backfilled into it; new signups without a
tenant get auto-enrolled in its default section.

Curriculum pivot (Mar 2025):
  * The ACTIVE default course is PHY211 (Physics) — the fictional-payload
    replacement for the MEC271 robotics demo. Its Course→Module→Lesson→
    Content graph, competency graph, and practice items come from
    ``services.curriculum`` (the DB importer).
  * MEC271 (Automatic Control) remains in the DB **as historical data**
    alongside a single legacy MASTERY instrument, only so the retained
    simulation engine (reusable architecture — see SimulationRun, the
    /api/simulation route, and ``test_simulation``) can keep resolving its
    rubric. Everything else MEC271 is deactivated from the product surface:
    it is never the default course, never seeded from ``mock_data`` (which is
    now physics-only), and never reachable from the frontend navigation.
"""

from __future__ import annotations

import json
import logging

from sqlalchemy.orm import Session

from . import crud
from .models import Course, Department, Faculty, Section, Student, University, User

_log = logging.getLogger("arete.bootstrap")

# ---------------------------------------------------------------------------
# Default organization seed. Two departments / two courses: MEC271 kept for
# history (legacy), PHY211 the active default the platform enrolls into.
# ---------------------------------------------------------------------------

DEFAULT_UNIVERSITY = {
    "code": "ARETE",
    "name": "Arete Academy",
    "email_domains": ["university.edu.eg"],
}

DEFAULT_ORG = {
    "faculties": [
        {
            "code": "ENG",
            "name": "Faculty of Engineering",
            "departments": [
                {
                    "code": "MEC",
                    "name": "Mechanical Engineering",
                    "courses": [
                        {
                            "code": "MEC271",
                            "title": "Automatic Control",
                            "credits": 3,
                            "sections": [{"term": "2026-S1", "code": "01"}],
                        }
                    ],
                },
                {
                    "code": "PHYS",
                    "name": "Physics",
                    "courses": [
                        {
                            "code": "PHY211",
                            "title": "Physics",
                            "credits": 3,
                            "sections": [{"term": "2026-S1", "code": "01"}],
                            "is_default": True,
                        }
                    ],
                },
            ],
        }
    ]
}


def ensure_default_organization(db: Session) -> University:
    """Idempotently create the default university + org tree.

    Returns the default ``University`` row. Safe to call on every start /
    app import — uses get-or-create semantics throughout.
    """
    university = crud.get_university_by_code(db, DEFAULT_UNIVERSITY["code"])
    if university is None:
        university = crud.create_university(
            db,
            code=DEFAULT_UNIVERSITY["code"],
            name=DEFAULT_UNIVERSITY["name"],
            email_domains=DEFAULT_UNIVERSITY["email_domains"],
        )
        _log.info("created default university %s", university.code)

    for faculty_branch in DEFAULT_ORG["faculties"]:
        faculty = (
            db.query(Faculty)
            .filter(
                Faculty.university_id == university.id,
                Faculty.code == faculty_branch["code"],
            )
            .first()
        )
        if faculty is None:
            faculty = crud.create_faculty(
                db,
                university_id=university.id,
                code=faculty_branch["code"],
                name=faculty_branch["name"],
            )
        for dept_branch in faculty_branch["departments"]:
            department = (
                db.query(Department)
                .filter(Department.faculty_id == faculty.id, Department.code == dept_branch["code"])
                .first()
            )
            if department is None:
                department = crud.create_department(
                    db,
                    faculty_id=faculty.id,
                    code=dept_branch["code"],
                    name=dept_branch["name"],
                )
            for course_branch in dept_branch["courses"]:
                course = (
                    db.query(Course)
                    .filter(
                        Course.department_id == department.id,
                        Course.code == course_branch["code"],
                    )
                    .first()
                )
                if course is None:
                    course = crud.create_course(
                        db,
                        department_id=department.id,
                        code=course_branch["code"],
                        title=course_branch["title"],
                        credits=course_branch["credits"],
                    )
                for section_branch in course_branch.get("sections", []):
                    section = (
                        db.query(Section)
                        .filter(
                            Section.course_id == course.id,
                            Section.term == section_branch["term"],
                            Section.code == section_branch["code"],
                        )
                        .first()
                    )
                    if section is None:
                        section = crud.create_section(
                            db,
                            course_id=course.id,
                            term=section_branch["term"],
                            code=section_branch["code"],
                        )

    db.commit()
    return university


def get_default_section_id(db: Session) -> int | None:
    """Return the id of the default university's default section, if any.

    Prefers the active default course (``PHY211``); falls back to the oldest
    section so legacy MEC271 -era accounts keep an enrollment target.
    """
    from sqlalchemy import case

    university = crud.get_university_by_code(db, DEFAULT_UNIVERSITY["code"])
    if university is None:
        return None
    section = (
        db.query(Section)
        .join(Course, Section.course_id == Course.id)
        .join(Department, Course.department_id == Department.id)
        .join(Faculty, Department.faculty_id == Faculty.id)
        .filter(Faculty.university_id == university.id)
        .order_by(case((Course.code == "PHY211", 0), else_=1), Section.id)
        .first()
    )
    return section.id if section else None


def backfill_tenant_membership(db: Session) -> None:
    """Assign the default university to every tenant-less account and learner.

    Runs after the default org exists: users with ``university_id IS NULL``
    and students with ``university_id IS NULL`` are pointed at the default
    university. Idempotent.
    """
    university = crud.get_university_by_code(db, DEFAULT_UNIVERSITY["code"])
    if university is None:
        return

    db.query(User).filter(User.university_id.is_(None)).update(
        {"university_id": university.id}, synchronize_session=False
    )
    db.query(Student).filter(Student.university_id.is_(None)).update(
        {"university_id": university.id}, synchronize_session=False
    )
    db.query(crud.models.AuditLog).filter(crud.models.AuditLog.university_id.is_(None)).update(
        {"university_id": university.id}, synchronize_session=False
    )
    db.commit()


def enroll_all_students_in_default_section(db: Session) -> None:
    """Enroll every student who isn't enrolled anywhere into the default
    section — preserving access to student-data and instructor endpoints.
    Idempotent."""
    section_id = get_default_section_id(db)
    if section_id is None:
        return
    orphan_students = (
        db.query(Student)
        .outerjoin(crud.models.Enrollment, crud.models.Enrollment.student_id == Student.student_id)
        .filter(crud.models.Enrollment.id.is_(None))
        .all()
    )
    for student in orphan_students:
        crud.enroll_student_in_section(db, student_id=student.student_id, section_id=section_id)
    db.commit()


def seed_physics_curriculum(db: Session, university: University) -> None:
    """Import the active PHY211 curriculum blueprint (course → module → lesson
    → content → resources → practice) via the DB importer.

    Idempotent: every entity is keyed on stable slugs. Competency definitions
    and prerequisite edges come from the same bundle, so the graph and the
    content never drift apart.
    """
    from ..services.curriculum.seed import ensure_curriculum_for_university

    ensure_curriculum_for_university(db, university_id=university.id)


def _legacy_simulation_footing(db: Session) -> None:
    """Fence the legacy robotics (PID) dashboard: keep enough MEC271 rows for
    the retained simulation engine to resolve its rubric.

    The simulation route/service (reusable architecture from Sprint 7) hard
    codes its course scope to MEC271 and requires a resolvable MASTERY
    assessment for ``pid-tuning``. We therefore:
      * keep the MEC271 course (seeded above as historical data),
      * ensure the ``pid-tuning`` competency exists under it,
      * deactivate any pre-existing MEC271 assessments (product surface),
      * retain exactly one ``PID Tuning — Mastery`` instrument — the engine's
        rubric contract. This single row is the only place the active PID
        assessment lives; it is deliberately inert everywhere else.
    """
    from ..services.simulation_contract import RUBRIC_CRITERIA

    course = db.query(Course).filter(Course.code == "MEC271").order_by(Course.id).first()
    if course is None:
        _log.warning("legacy simulation footing: MEC271 course missing; skipping")
        return

    comp = crud.ensure_competency(
        db,
        course_id=course.id,
        code="pid-tuning",
        title="PID Tuning (legacy)",
        description="Legacy robotics-tuning competency retained for the reusable simulation engine.",
        taxonomy_level="apply",
        sort_order=3,
    )

    for assessment in crud.get_assessments_for_competency(
        db, competency_id=comp.id, active_only=False
    ):
        assessment.is_active = False

    assessment = crud.ensure_assessment(
        db,
        competency_id=comp.id,
        title="PID Tuning — Mastery",
        kind="MASTERY",
        pass_rule=json.dumps({"all_mandatory": True, "min_criteria": 4}),
        rubric_spec=json.dumps(
            [
                "overshoot <= 10",
                "settling_time <= 2.0",
                "steady_state_error <= 0.01",
                "stable == true",
            ]
        ),
    )
    # The retained engine resolves this MASTERY instrument (active_only=True
    # lookups); it is the single legacy exception to the product pivot.
    assessment.is_active = True
    for crit in RUBRIC_CRITERIA:
        crud.ensure_rubric_criterion(
            db,
            assessment_id=assessment.id,
            metric_field=crit["metric_field"],
            operator=crit["operator"],
            threshold=crit["threshold"],
            mandatory=crit["mandatory"],
        )
    db.commit()


def backfill_remediation_resources(db: Session) -> None:
    """Seed the remediation content catalog from ``mock_data`` (physics).

    Idempotent: rows are keyed on the unique ``resource_code``. The adaptive
    controller later matches a student's state to these rows, so the catalog
    must exist from first boot.
    """
    from ..services.mock_data import REMEDIATION_RESOURCES

    for spec in REMEDIATION_RESOURCES:
        crud.ensure_remediation_resource(
            db,
            resource_code=spec["resource_code"],
            title=spec["title"],
            body=spec.get("body", ""),
            kind=spec.get("kind", "lesson"),
            competency_code=spec.get("competency_code"),
            misconception_tag=spec.get("misconception_tag"),
            metric_field=spec.get("metric_field"),
            sort_order=spec.get("sort_order", 0),
        )
    db.commit()


def boot_default_organization() -> University:
    """Run the full default-org bootstrap inside a fresh session.

    Called once after table creation at app startup.
    """
    from .database import SessionLocal

    with SessionLocal() as db:
        university = ensure_default_organization(db)
        seed_physics_curriculum(db, university)
        _legacy_simulation_footing(db)
        backfill_remediation_resources(db)
        backfill_tenant_membership(db)
        enroll_all_students_in_default_section(db)
        return university