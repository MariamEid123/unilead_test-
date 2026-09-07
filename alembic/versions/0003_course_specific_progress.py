"""Add independent course and lecture progress without touching auth tables.

Revision ID: 0003
Revises: 0002
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0003"
down_revision: str | None = "0002"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "course_progress",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("course_id", sa.String(64), nullable=False),
        sa.Column("progress_percentage", sa.Integer, nullable=False, server_default="0"),
        sa.Column("completed_lectures_count", sa.Integer, nullable=False, server_default="0"),
        sa.Column("total_lectures", sa.Integer, nullable=False, server_default="0"),
        sa.Column("completed_quizzes_count", sa.Integer, nullable=False, server_default="0"),
        sa.Column("total_quizzes", sa.Integer, nullable=False, server_default="0"),
        sa.Column("completed_assignments_count", sa.Integer, nullable=False, server_default="0"),
        sa.Column("total_assignments", sa.Integer, nullable=False, server_default="0"),
        sa.Column("simulation_status", sa.String(32)), sa.Column("review_status", sa.String(32)),
        sa.Column("last_lecture_id", sa.String(128)), sa.Column("last_accessed_at", sa.DateTime),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("user_id", "course_id", name="uq_course_progress_user_course"),
    )
    op.create_index("ix_course_progress_user_id", "course_progress", ["user_id"])
    op.create_index("ix_course_progress_last_accessed_at", "course_progress", ["last_accessed_at"])
    op.create_table(
        "lecture_progress",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("course_id", sa.String(64), nullable=False), sa.Column("lecture_id", sa.String(128), nullable=False),
        sa.Column("completed", sa.Boolean, nullable=False, server_default=sa.false()),
        sa.Column("completed_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("user_id", "lecture_id", name="uq_lecture_progress_user_lecture"),
    )
    op.create_index("ix_lecture_progress_user_id", "lecture_progress", ["user_id"])
    op.create_index("ix_lecture_progress_course_id", "lecture_progress", ["course_id"])


def downgrade() -> None:
    op.drop_table("lecture_progress")
    op.drop_table("course_progress")
