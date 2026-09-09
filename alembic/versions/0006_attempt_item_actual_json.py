"""Sprint 7 — AttemptItemResult.actual becomes a JSON column.

Revision ID: 0006
Revises: 0005
Create Date: 2026-09-06

``attempt_item_results.actual`` holds the live value of a rubric metric for
one task. Most metrics are floats (overshoot, settling_time), but the
``stable`` metric is a boolean. SQLite tolerates a bool inside a FLOAT
column; PostgreSQL rejects it at insert time
(``DatatypeMismatch: VALUES types double precision and boolean cannot be
matched``). Store the verdict type-flexibly in a JSON column instead so the
DB schema is honest on both backends.

Note on SQLite dev DBs: ``Base.metadata.create_all`` (the local/test path)
does not ALTER existing columns, so an existing local ``attempt_item_results``
still carries the old FLOAT type and keeps working (dynamic typing); fresh
dev DBs and the PostgreSQL path pick up the JSON type via this migration.

Run with::

    cd apps/api
    alembic upgrade head
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0006"
down_revision: str | None = "0005"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    with op.batch_alter_table("attempt_item_results") as batch_op:
        batch_op.alter_column(
            "actual",
            existing_type=sa.Float(),
            type_=sa.JSON(),
            existing_nullable=True,
            postgresql_using="actual::text::json",
        )


def downgrade() -> None:
    # A FLOAT column cannot hold the JSON booleans written since the upgrade,
    # and PostgreSQL has no implicit json -> float cast, so map booleans to
    # 0/1 then cast the remaining JSON values explicitly.
    op.execute(
        "UPDATE attempt_item_results "
        "SET actual = '1'::json WHERE actual::text = 'true'"
    )
    op.execute(
        "UPDATE attempt_item_results "
        "SET actual = '0'::json WHERE actual::text = 'false'"
    )
    with op.batch_alter_table("attempt_item_results") as batch_op:
        batch_op.alter_column(
            "actual",
            existing_type=sa.JSON(),
            type_=sa.Float(),
            existing_nullable=True,
            postgresql_using="actual::text::double precision",
        )
