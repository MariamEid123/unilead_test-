"""Sprint 4 — durable competency graph foundation.

Revision ID: 0004
Revises: 0003
Create Date: 2026-09-05

Creates the lasting competency *definitions* (the graph, not per-student
state):

  competencies            - durable, course-scoped skill definitions
  competency_prerequisites- directed DAG edges (pre -> post) per course
  assessments             - competency-scoped instruments (DIAGNOSTIC/MASTERY/RETRY)
  assessment_tasks        - objective probes inside an assessment
  assessment_rubric_criteria - deterministic pass/fail thresholds (the rubric)
  assessment_attempts     - immutable, numbered student attempts
  attempt_item_results    - per-task rubric verdicts inside an attempt
  evidence_records        - central objective proof (simulation/assessment/...)

Then backfills the MEC271 default course with the ``INITIAL_COMPETENCIES``
content (5 competencies + 4 prerequisite edges) and the PID Tuning Mastery
assessment + rubric — matching what ``bootstrap.backfill_competency_graph`` /
``bootstrap.backfill_assessments`` do for fresh SQLite DBs.

This deliberately does NOT create competency_snapshots (that table already
exists and holds derived per-student state) nor any evidence/mastery tables
(those arrive with the assessment/evidence/mastery sprints).

Run with::

    cd apps/api
    alembic upgrade head

Local SQLite dev DBs get these tables via ``Base.metadata.create_all`` +
``boot_default_organization`` (``app/db/database.py``); Alembic is the
PostgreSQL path.
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0004"
down_revision: str | None = "0003"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

# Same content as app/services/mock_data.py INITIAL_COMPETENCIES +
# COMPETENCY_PREREQUISITES. Duplicated here (not imported) so this migration
# stays a standalone snapshot — deterministic no matter what the service
# code says later.
_INITIAL_COMPETENCIES = [
    (
        "feedback-fundamentals",
        "Feedback Fundamentals",
        0,
        "understand",
        "Explain the purpose of feedback in a closed-loop system.",
    ),
    (
        "pid-fundamentals",
        "PID Fundamentals",
        1,
        "recall",
        "Identify the P, I, and D terms and what each responds to.",
    ),
    (
        "pid-reasoning",
        "PID Reasoning",
        2,
        "apply",
        "Reason about how changing PID gains alters system response.",
    ),
    (
        "pid-tuning",
        "PID Tuning",
        3,
        "apply",
        "Tune a PID controller to meet overshoot/settling/steady-state targets.",
    ),
    (
        "response-analysis",
        "Response Analysis",
        4,
        "analyze",
        "Analyze step-response metrics: rise time, overshoot, settling time, error.",
    ),
]

_PREREQUISITES = [
    ("feedback-fundamentals", "pid-fundamentals"),
    ("pid-fundamentals", "pid-reasoning"),
    ("pid-reasoning", "pid-tuning"),
    ("pid-reasoning", "response-analysis"),
]


_MEC271_MASTERY_PASS_RULE = '{"all_mandatory": true, "min_criteria": 4}'
_MEC271_MASTERY_RUBRIC_SPEC = (
    '["overshoot <= 10", "settling_time <= 2.0", "steady_state_error <= 0.01", "stable == true"]'
)


def upgrade() -> None:
    op.create_table(
        "competencies",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("course_id", sa.Integer, sa.ForeignKey("courses.id"), nullable=False),
        sa.Column("code", sa.String(64), nullable=False),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("description", sa.Text, nullable=False, server_default=""),
        sa.Column("taxonomy_level", sa.String(32), nullable=True),
        sa.Column("sort_order", sa.Integer, nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("course_id", "code", name="uq_competencies_course_code"),
    )
    op.create_index("ix_competencies_course_id", "competencies", ["course_id"])

    op.create_table(
        "competency_prerequisites",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("course_id", sa.Integer, sa.ForeignKey("courses.id"), nullable=False),
        sa.Column(
            "pre_competency_id", sa.Integer, sa.ForeignKey("competencies.id"), nullable=False
        ),
        sa.Column(
            "post_competency_id", sa.Integer, sa.ForeignKey("competencies.id"), nullable=False
        ),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint(
            "course_id",
            "pre_competency_id",
            "post_competency_id",
            name="uq_competency_prereq_edge",
        ),
    )
    op.create_index("ix_cp_post", "competency_prerequisites", ["course_id", "post_competency_id"])
    op.create_index(
        "ix_competency_prerequisites_pre_competency_id",
        "competency_prerequisites",
        ["pre_competency_id"],
    )
    op.create_index(
        "ix_competency_prerequisites_post_competency_id",
        "competency_prerequisites",
        ["post_competency_id"],
    )
    op.create_index(
        "ix_competency_prerequisites_course_id",
        "competency_prerequisites",
        ["course_id"],
    )

    op.create_table(
        "assessments",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("competency_id", sa.Integer, sa.ForeignKey("competencies.id"), nullable=False),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("kind", sa.String(16), nullable=False, server_default="MASTERY"),
        sa.Column("pass_rule", sa.Text, nullable=False, server_default="{}"),
        sa.Column("rubric_spec", sa.Text, nullable=False, server_default="[]"),
        sa.Column("is_active", sa.Boolean, nullable=False, server_default="true"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("competency_id", "title", name="uq_assessments_competency_title"),
    )
    op.create_index("ix_assessments_competency_id", "assessments", ["competency_id"])

    op.create_table(
        "assessment_tasks",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("assessment_id", sa.Integer, sa.ForeignKey("assessments.id"), nullable=False),
        sa.Column("code", sa.String(64), nullable=False),
        sa.Column("prompt", sa.Text, nullable=False),
        sa.Column("metric_field", sa.String(64), nullable=True),
        sa.Column("sort_order", sa.Integer, nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("assessment_id", "code", name="uq_assessment_tasks_oq_code"),
    )
    op.create_index("ix_assessment_tasks_assessment_id", "assessment_tasks", ["assessment_id"])

    op.create_table(
        "assessment_rubric_criteria",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("assessment_id", sa.Integer, sa.ForeignKey("assessments.id"), nullable=False),
        sa.Column("metric_field", sa.String(64), nullable=False),
        sa.Column("operator", sa.String(16), nullable=False),
        sa.Column("threshold", sa.Float, nullable=True),
        sa.Column("mandatory", sa.Boolean, nullable=False, server_default="true"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("assessment_id", "metric_field", name="uq_assessment_rubric_metric"),
    )
    op.create_index(
        "ix_assessment_rubric_criteria_assessment_id",
        "assessment_rubric_criteria",
        ["assessment_id"],
    )

    op.create_table(
        "assessment_attempts",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("assessment_id", sa.Integer, sa.ForeignKey("assessments.id"), nullable=False),
        sa.Column(
            "student_id", sa.String(64), sa.ForeignKey("students.student_id"), nullable=False
        ),
        sa.Column("attempt_number", sa.Integer, nullable=False),
        sa.Column("status", sa.String(16), nullable=False, server_default="SUBMITTED"),
        sa.Column("score", sa.Float, nullable=True),
        sa.Column("passed", sa.Boolean, nullable=True),
        sa.Column("results_json", sa.Text, nullable=False, server_default="[]"),
        sa.Column("resolution_json", sa.Text, nullable=False, server_default="{}"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column("submitted_at", sa.DateTime, nullable=True),
        sa.UniqueConstraint(
            "assessment_id",
            "student_id",
            "attempt_number",
            name="uq_assessment_attempt_number",
        ),
    )
    op.create_index("ix_assessment_attempts_student", "assessment_attempts", ["student_id"])
    op.create_index(
        "ix_assessment_attempts_assessment_id", "assessment_attempts", ["assessment_id"]
    )
    op.create_index("ix_attempts_student", "assessment_attempts", ["student_id", "assessment_id"])

    op.create_table(
        "attempt_item_results",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "attempt_id", sa.Integer, sa.ForeignKey("assessment_attempts.id"), nullable=False
        ),
        sa.Column("task_code", sa.String(64), nullable=False),
        sa.Column("metric_field", sa.String(64), nullable=True),
        sa.Column("actual", sa.Float, nullable=True),
        sa.Column("passed", sa.Boolean, nullable=False),
        sa.Column("misconception_tag", sa.String(128), nullable=True),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_attempt_item_results_attempt_id", "attempt_item_results", ["attempt_id"])

    op.create_table(
        "evidence_records",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "student_id", sa.String(64), sa.ForeignKey("students.student_id"), nullable=False
        ),
        sa.Column("competency_id", sa.Integer, sa.ForeignKey("competencies.id"), nullable=False),
        sa.Column("source_type", sa.String(32), nullable=False),
        sa.Column("source_ref_id", sa.Integer, nullable=True),
        sa.Column("metric_json", sa.Text, nullable=False, server_default="{}"),
        sa.Column("context_json", sa.Text, nullable=False, server_default="{}"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_evidence_records_student_id", "evidence_records", ["student_id"])
    op.create_index("ix_evidence_records_competency_id", "evidence_records", ["competency_id"])
    op.create_index(
        "ix_evidence_student_competency", "evidence_records", ["student_id", "competency_id"]
    )
    op.create_index(
        "ix_evidence_competency_created", "evidence_records", ["competency_id", "created_at"]
    )

    op.create_table(
        "mastery_records",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "student_id", sa.String(64), sa.ForeignKey("students.student_id"), nullable=False
        ),
        sa.Column("competency_id", sa.Integer, sa.ForeignKey("competencies.id"), nullable=False),
        sa.Column("level", sa.String(32), nullable=False),
        sa.Column("rubric_json", sa.Text, nullable=False, server_default="{}"),
        sa.Column("reason_codes_json", sa.Text, nullable=False, server_default="[]"),
        sa.Column("evidence_ids_json", sa.Text, nullable=False, server_default="[]"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column("resolved_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint(
            "student_id", "competency_id", "level", "resolved_at", name="uq_mastery_state"
        ),
    )
    op.create_index("ix_mastery_student_level", "mastery_records", ["student_id", "level"])
    op.create_index(
        "ix_mastery_student_competency", "mastery_records", ["student_id", "competency_id"]
    )
    op.create_index("ix_mastery_records_resolved_at", "mastery_records", ["resolved_at"])

    # 4E: remediation_plans now links to the triggering evidence + lifecycle.
    op.add_column("remediation_plans", sa.Column("evidence_id", sa.Integer, nullable=True))
    op.add_column(
        "remediation_plans",
        sa.Column("reason_codes_json", sa.Text, nullable=False, server_default="[]"),
    )
    op.add_column(
        "remediation_plans",
        sa.Column("status", sa.String(16), nullable=False, server_default="open"),
    )
    op.add_column(
        "remediation_plans", sa.Column("completed_at", sa.DateTime, nullable=True)
    )
    op.create_index(
        "ix_remediation_plans_evidence_id", "remediation_plans", ["evidence_id"]
    )
    op.create_index("ix_remediation_plans_status", "remediation_plans", ["status"])

    bind = op.get_bind()

    # Backfill the skill graph for the default MEC271 course (idempotent via
    # get-or-insert on (course_id, code) and (course_id, pre, post)).
    course_id = int(
        bind.execute(
            sa.text("SELECT id FROM courses WHERE code = 'MEC271' ORDER BY id LIMIT 1")
        ).fetchone()[0]
    )

    comp_ids: dict[str, int] = {}
    for code, title, sort_order, taxonomy_level, description in _INITIAL_COMPETENCIES:
        row = bind.execute(
            sa.text("SELECT id FROM competencies WHERE course_id = :cid AND code = :code"),
            {"cid": course_id, "code": code},
        ).fetchone()
        if row is not None:
            comp_ids[code] = int(row[0])
            continue
        cid = int(
            bind.execute(
                sa.text(
                    "INSERT INTO competencies "
                    "(course_id, code, title, description, taxonomy_level, sort_order, created_at) "
                    "VALUES (:cid, :code, :title, :desc, :tax, :sort, now()) RETURNING id"
                ),
                {
                    "cid": course_id,
                    "code": code,
                    "title": title,
                    "desc": description,
                    "tax": taxonomy_level,
                    "sort": sort_order,
                },
            ).fetchone()[0]
        )
        comp_ids[code] = cid

    for pre_code, post_code in _PREREQUISITES:
        pre_id, post_id = comp_ids.get(pre_code), comp_ids.get(post_code)
        if pre_id is None or post_id is None:
            continue
        exists = bind.execute(
            sa.text(
                "SELECT 1 FROM competency_prerequisites "
                "WHERE course_id = :cid AND pre_competency_id = :pre "
                "AND post_competency_id = :post"
            ),
            {"cid": course_id, "pre": pre_id, "post": post_id},
        ).fetchone()
        if exists is not None:
            continue
        bind.execute(
            sa.text(
                "INSERT INTO competency_prerequisites "
                "(course_id, pre_competency_id, post_competency_id, created_at) "
                "VALUES (:cid, :pre, :post, now())"
            ),
            {"cid": course_id, "pre": pre_id, "post": post_id},
        )

    # Backfill the MEC271 PID Tuning Mastery assessment + rubric.
    pid_tuning_id = comp_ids.get("pid-tuning")
    if pid_tuning_id is not None:
        assessment_row = bind.execute(
            sa.text("SELECT id FROM assessments WHERE competency_id = :cid AND title = :title"),
            {"cid": pid_tuning_id, "title": "PID Tuning — Mastery"},
        ).fetchone()
        if assessment_row is None:
            assessment_id = int(
                bind.execute(
                    sa.text(
                        "INSERT INTO assessments "
                        "(competency_id, title, kind, pass_rule, rubric_spec, is_active, created_at) "
                        "VALUES (:cid, :title, 'MASTERY', :rule, :rubric, true, now()) RETURNING id"
                    ),
                    {
                        "cid": pid_tuning_id,
                        "title": "PID Tuning — Mastery",
                        "rule": _MEC271_MASTERY_PASS_RULE,
                        "rubric": _MEC271_MASTERY_RUBRIC_SPEC,
                    },
                ).fetchone()[0]
            )
            for metric, operator, threshold in (
                ("overshoot", "<=", 10.0),
                ("settling_time", "<=", 2.0),
                ("steady_state_error", "<=", 0.01),
                ("stable", "is_true", None),
            ):
                exists = bind.execute(
                    sa.text(
                        "SELECT 1 FROM assessment_rubric_criteria "
                        "WHERE assessment_id = :aid AND metric_field = :m"
                    ),
                    {"aid": assessment_id, "m": metric},
                ).fetchone()
                if exists is not None:
                    continue
                bind.execute(
                    sa.text(
                        "INSERT INTO assessment_rubric_criteria "
                        "(assessment_id, metric_field, operator, threshold, mandatory, created_at) "
                        "VALUES (:aid, :m, :op, :thr, true, now())"
                    ),
                    {"aid": assessment_id, "m": metric, "op": operator, "thr": threshold},
                )


def downgrade() -> None:
    op.drop_index("ix_remediation_plans_evidence_id", table_name="remediation_plans")
    op.drop_index("ix_remediation_plans_status", table_name="remediation_plans")
    op.drop_column("remediation_plans", "completed_at")
    op.drop_column("remediation_plans", "status")
    op.drop_column("remediation_plans", "reason_codes_json")
    op.drop_column("remediation_plans", "evidence_id")
    # mastery_records references students + competencies.
    op.drop_table("mastery_records")
    # evidence_records references students + competencies.
    op.drop_table("evidence_records")
    # attempt_item_results references assessment_attempts.
    op.drop_table("attempt_item_results")
    # assessment_attempts references assessments + students.
    op.drop_table("assessment_attempts")
    # Drop rubric criteria and tasks first: they reference assessments.
    op.drop_table("assessment_rubric_criteria")
    op.drop_table("assessment_tasks")
    op.drop_table("assessments")
    # Drop prerequisites next: they reference competencies.
    op.drop_table("competency_prerequisites")
    op.drop_table("competencies")
