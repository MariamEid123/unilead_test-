"""Sprint 5 — remediation content catalog.

Revision ID: 0005
Revises: 0004
Create Date: 2026-09-05

Creates ``remediation_resources`` — the content catalog the deterministic
adaptive controller (Sprint 5E) matches against a student's state. Rows may
target a competency, a misconception tag, or a rubric criterion; the
controller scores them and recommends the best fit.

Deliberately a *new* table (no ALTER of existing tables): the SQLite dev
path picks it up automatically through ``Base.metadata.create_all``, and the
default MEC271 catalog is backfilled idempotently by
``bootstrap.backfill_remediation_resources``.

Run with::

    cd apps/api
    alembic upgrade head

Local SQLite dev DBs get the table via ``Base.metadata.create_all`` +
``boot_default_organization``; Alembic is the PostgreSQL path.
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0005"
down_revision: str | None = "0004"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "remediation_resources",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("resource_code", sa.String(64), nullable=False),
        sa.Column("competency_code", sa.String(64), nullable=True),
        sa.Column("misconception_tag", sa.String(128), nullable=True),
        sa.Column("metric_field", sa.String(64), nullable=True),
        sa.Column("kind", sa.String(32), nullable=False, server_default="lesson"),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("body", sa.Text, nullable=False, server_default=""),
        sa.Column("is_active", sa.Boolean, nullable=False, server_default="true"),
        sa.Column("sort_order", sa.Integer, nullable=False, server_default="0"),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
        sa.UniqueConstraint("resource_code", name="uq_remediation_resources_code"),
    )
    op.create_index(
        "ix_remediation_resources_competency",
        "remediation_resources",
        ["competency_code"],
    )


def downgrade() -> None:
    op.drop_index(
        "ix_remediation_resources_competency", table_name="remediation_resources"
    )
    op.drop_table("remediation_resources")
