"""Add password reset code storage to users."""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0002"
down_revision: str | None = "0001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("users", sa.Column("password_reset_code_hash", sa.String(64), nullable=True))
    op.add_column("users", sa.Column("password_reset_expires_at", sa.DateTime, nullable=True))
    op.add_column("users", sa.Column("password_reset_sent_at", sa.DateTime, nullable=True))


def downgrade() -> None:
    op.drop_column("users", "password_reset_sent_at")
    op.drop_column("users", "password_reset_expires_at")
    op.drop_column("users", "password_reset_code_hash")