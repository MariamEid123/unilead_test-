"""One-click launcher DB bootstrap.

Dev/demo convention on SQLite: the schema is created from the ORM metadata
(``create_all_tables``, which also runs the idempotent default-org +
curriculum bootstrap) and the alembic revision is then stamped to ``head``.
The alembic migration chain is PostgreSQL-flavoured (raw ``now()`` and
``RETURNING id`` data migrations) and is only exercised on production
Postgres, so a fresh SQLite file is built from metadata, not by replaying
every migration.

Idempotent — safe to run every start: existing DBs keep their rows and just
get their revision re-stamped to the app's current head.

Usage::

    python -m scripts.bootstrap_db
"""

from __future__ import annotations

import sys
from pathlib import Path

# Make the app package importable when run from apps/api/.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from alembic import command  # noqa: E402
from alembic.config import Config  # noqa: E402

from app.db import create_all_tables  # noqa: E402  (also seeds default org)


def main() -> int:
    create_all_tables()

    cfg = Config("alembic.ini")
    command.stamp(cfg, "head")
    print("DB schema created/verified from app metadata; alembic revision stamped to head.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
