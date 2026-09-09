# 🚀 Quick Start — One Click

Double-click **`start.bat`** in this folder. That's it.

The script will:

1. ✅ Check Python + Node.js are installed (and tell you if not)
2. ✅ Create a Python virtual environment (first run only)
3. ✅ Install all backend dependencies (first run only)
4. ✅ Install all frontend npm dependencies (first run only)
5. ✅ Prepare the local dev database (creates `arete.db`, SQLite)
6. ✅ Start the backend in a new window (port 8000)
7. ✅ Wait for it to come up
8. ✅ Start the frontend in a new window (port 5173)
9. ✅ Wait for it to come up
10. ✅ Open your browser at `http://localhost:5173`

> **SQLite here is a local dev convenience only.** Production runs on
> PostgreSQL — see **Production (PostgreSQL)** below.

## On subsequent runs

The script detects that dependencies are already installed and skips steps
2-5, so it launches in a few seconds.

## Production (PostgreSQL)

The one-click local start uses SQLite (zero-config). For production we run
PostgreSQL: concurrent writes, reliable persistence, proper backups
(`pg_dump`) and real Alembic migrations.

```powershell
# 1. Start Postgres + API + web
docker compose up -d --build

# The api container automatically runs `alembic upgrade head` before boot.
```

- Postgres persists in the `postgres-data` volume (delete it to reset).
- `DATABASE_URL` defaults to `postgresql+psycopg://arete:arete_dev@postgres:5432/arete`
  and can be overridden in `docker-compose.yml`.
- **Migrating an existing dev database** (SQLite → Postgres):

  ```powershell
  # a) point a terminal at apps/api and create the Postgres schema
  $env:DEST_URL = "postgresql+psycopg://arete:arete_dev@localhost:5432/arete"
  alembic upgrade head
  # b) copy every row (source stays untouched), verifying counts
  $env:SOURCE_URL = "sqlite:///./arete.db"
  python -m scripts.migrate
  ```

- **Backup / restore** on the Postgres volume:

  ```powershell
  # backup (write into the container, then copy out on Windows)
  docker compose exec postgres pg_dump -U arete -d arete -F c -f /tmp/arete.dump
  docker compose cp postgres:/tmp/arete.dump ./backup-arete.dump

  # restore
  docker compose cp ./backup-arete.dump postgres:/tmp/arete.dump
  docker compose exec postgres pg_restore -U arete --clean -d arete /tmp/arete.dump
  ```

## Login

Once the browser opens, you have two options:

- **Demo account** (if `arete.db` was created before the no-demo refactor):
  ```
  Email:    mariam@student.aiu.edu.eg
  Password: demo1234
  ```
- **Fresh account** (recommended): click "Create your account" on the signup
  page and use any email + 8-character password you like.

## Stopping the servers

Close the two windows that the script opened (their titles start with
`Arete Backend` and `Arete Frontend`).

## Troubleshooting

| Problem | Fix |
|---|---|
| `Python is not installed` | Install from https://www.python.org/downloads/ (check "Add to PATH") |
| `Node.js is not installed` | Install from https://nodejs.org/ (LTS version) |
| `ExecutionPolicy` error on PowerShell | Run as admin: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| Port 8000 or 5173 already in use | Edit `start.bat` and change `BACKEND_PORT` / `FRONTEND_PORT` at the top |
| Backend doesn't come up | Look at the backend window for the error message |
| Frontend can't reach backend | Make sure both windows are still open |

## Manual alternative

If you prefer to run things by hand:

```powershell
# Terminal 1 — Backend
cd apps\api
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload

# Terminal 2 — Frontend
cd apps\web
npm run dev
```

Then open `http://localhost:5173` in your browser.
