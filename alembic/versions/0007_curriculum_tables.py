"""Curriculum structure: course → module → lesson → content.

Revision ID: 0007
Revises: 0006
Create Date: 2026-09-07

Adds the DB-backed content backbone for first-year university courses:

  modules            - units inside a course (e.g. 'Electrostatics')
  lessons            - deliverable sessions inside a module
  lesson_contents    - ordered content blocks (TEXT/FORMULA/EXAMPLE/KEY_POINT/
                       WARNING/TABLE/IMAGE/VIDEO/SUMMARY/DIFFICULT_CONCEPT)
  lesson_resources   - attachments (video lectures, PDFs, links)
  lesson_competencies- link table tying a lesson to the competencies it teaches
  practice_items     - practice/check questions (answers server-side only)

Also deactivates the MEC271 PID assessments backfilled by ``0004`` — the
course stays in the DB as historical data (the retained simulation engine
re-resolves its single MASTERY instrument at startup via
``bootstrap._legacy_simulation_footing``), but its assessments are turned off
from the product surface.

Content (the PHY211 physics blueprint) is NOT seeded here: the runtime
bootstrap imports it idempotently on both backends (``create_all``-managed
dev DBs and Alembic-managed PostgreSQL) via ``services.curriculum.seed``.

Local SQLite dev DBs reach the same schema through
``Base.metadata.create_all`` + ``boot_default_organization``.

Run with::

    cd apps/api
    alembic upgrade head
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0007"
down_revision: str | None = "0006"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # Course cards and lesson views show a description; the model exposes it
    # from day one so the catalog API has a stable column.
    op.add_column(
        "courses",
        sa.Column("description", sa.Text(), nullable=False, server_default=""),
    )

    op.create_table(
        "modules",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("course_id", sa.Integer, sa.ForeignKey("courses.id"), nullable=False),
        sa.Column("code", sa.String(32), nullable=False),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("description", sa.Text, nullable=False, server_default=""),
        sa.Column("sort_order", sa.Integer, nullable=False, server_default="0"),
        sa.Column("is_active", sa.Boolean, nullable=False, server_default="true"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("course_id", "code", name="uq_modules_course_code"),
    )
    op.create_index("ix_modules_course_id", "modules", ["course_id"])

    op.create_table(
        "lessons",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("module_id", sa.Integer, sa.ForeignKey("modules.id"), nullable=False),
        sa.Column("code", sa.String(64), nullable=False),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("description", sa.Text, nullable=False, server_default=""),
        sa.Column("estimated_minutes", sa.Integer, nullable=True),
        sa.Column("difficulty", sa.String(16), nullable=False, server_default="beginner"),
        sa.Column("objectives_json", sa.Text, nullable=False, server_default="[]"),
        sa.Column("prerequisites_json", sa.Text, nullable=False, server_default="[]"),
        sa.Column("sort_order", sa.Integer, nullable=False, server_default="0"),
        sa.Column("is_active", sa.Boolean, nullable=False, server_default="true"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("module_id", "code", name="uq_lessons_module_code"),
    )
    op.create_index("ix_lessons_module_id", "lessons", ["module_id"])

    op.create_table(
        "lesson_contents",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("lesson_id", sa.Integer, sa.ForeignKey("lessons.id"), nullable=False),
        sa.Column("section_type", sa.String(32), nullable=False),
        sa.Column("title", sa.String(255), nullable=True),
        sa.Column("body", sa.Text, nullable=False, server_default=""),
        sa.Column("metadata_json", sa.Text, nullable=False, server_default="{}"),
        sa.Column("sort_order", sa.Integer, nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("lesson_id", "sort_order", name="uq_lesson_contents_section"),
    )
    op.create_index("ix_lesson_contents_lesson_id", "lesson_contents", ["lesson_id"])

    op.create_table(
        "lesson_resources",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("lesson_id", sa.Integer, sa.ForeignKey("lessons.id"), nullable=False),
        sa.Column("resource_type", sa.String(32), nullable=False, server_default="LINK"),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("description", sa.Text, nullable=False, server_default=""),
        sa.Column("external_url", sa.String(2048), nullable=True),
        sa.Column("duration_seconds", sa.Integer, nullable=True),
        sa.Column("metadata_json", sa.Text, nullable=False, server_default="{}"),
        sa.Column("sort_order", sa.Integer, nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_lesson_resources_lesson_id", "lesson_resources", ["lesson_id"])

    op.create_table(
        "lesson_competencies",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("lesson_id", sa.Integer, sa.ForeignKey("lessons.id"), nullable=False),
        sa.Column(
            "competency_id", sa.Integer, sa.ForeignKey("competencies.id"), nullable=False
        ),
        sa.Column("role", sa.String(32), nullable=False, server_default="teaches"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("lesson_id", "competency_id", name="uq_lesson_competency_link"),
    )
    op.create_index("ix_lesson_competencies_lesson_id", "lesson_competencies", ["lesson_id"])
    op.create_index(
        "ix_lesson_competencies_competency_id", "lesson_competencies", ["competency_id"]
    )

    op.create_table(
        "practice_items",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("lesson_id", sa.Integer, sa.ForeignKey("lessons.id"), nullable=False),
        sa.Column("competency_id", sa.Integer, sa.ForeignKey("competencies.id"), nullable=True),
        sa.Column("level", sa.String(16), nullable=False, server_default="UNDERSTAND"),
        sa.Column("prompt", sa.Text, nullable=False),
        sa.Column("options_json", sa.Text, nullable=False, server_default="[]"),
        sa.Column("answer_json", sa.Text, nullable=False, server_default="{}"),
        sa.Column("explanation", sa.Text, nullable=False, server_default=""),
        sa.Column("skill", sa.String(64), nullable=True),
        sa.Column("difficulty", sa.Integer, nullable=False, server_default="1"),
        sa.Column("sort_order", sa.Integer, nullable=False, server_default="0"),
        sa.Column("is_active", sa.Boolean, nullable=False, server_default="true"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_practice_items_lesson_id", "practice_items", ["lesson_id"])
    op.create_index("ix_practice_items_competency_id", "practice_items", ["competency_id"])

    # Product-surface deactivation of the historical MEC271 assessments.
    bind = op.get_bind()
    bind.execute(
        sa.text(
            "UPDATE assessments SET is_active = false "
            "WHERE competency_id IN ("
            "  SELECT c.id FROM competencies c "
            "  JOIN courses co ON co.id = c.course_id AND co.code = 'MEC271'"
            ")"
        )
    )


def downgrade() -> None:
    op.drop_column("courses", "description")
    op.drop_index("ix_practice_items_competency_id", table_name="practice_items")
    op.drop_index("ix_practice_items_lesson_id", table_name="practice_items")
    op.drop_table("practice_items")
    op.drop_index("ix_lesson_competencies_competency_id", table_name="lesson_competencies")
    op.drop_index("ix_lesson_competencies_lesson_id", table_name="lesson_competencies")
    op.drop_table("lesson_competencies")
    op.drop_index("ix_lesson_resources_lesson_id", table_name="lesson_resources")
    op.drop_table("lesson_resources")
    op.drop_index("ix_lesson_contents_lesson_id", table_name="lesson_contents")
    op.drop_table("lesson_contents")
    op.drop_index("ix_lessons_module_id", table_name="lessons")
    op.drop_table("lessons")
    op.drop_index("ix_modules_course_id", table_name="modules")
    op.drop_table("modules")