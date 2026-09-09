# Phase 16 — Arete Platform Pivot: Final Report

**Date:** 2026-09-07
**Branch:** arete-V-1.0.1
**Scope:** Full strip of the PID/MEC271 robotics prototype → first-year university physics curriculum platform.

---

## 1. Outcome

Arete is now a **competency-based first-year physics platform**. The default and only student-facing course is **PHY211 General Physics**, starting with **Lecture L1 — Electric Charge** (module M1, 4 learning competencies). MEC271 Automatic Control continues to exist in the database as history: the legacy assessment instruments are deactivated, The MEC course is no longer defaulted or linked from the product surface, and the simulation engine remains as dormant retained infrastructure (one legacy instrument stays active only to honor the existing engine contract).

**Test state (all green):**
- Backend API: **212 passed** (`python -m pytest -q`, ~60s)
- Frontend unit tests: **15 passed** (vitest)
- Frontend lint: **0 warnings / 0 errors** (oxlint)
- Frontend production build: **passes** (`tsc -b && vite build`)

---

## 2. Backend Curriculum Pivot

### New curriculum catalog service (PHY211)
| File | Purpose |
|---|---|
| `apps/api/app/services/curriculum/content.py` | Physics learning content: competencies, lessons, sections, practice items, video scripts, course description |
| `apps/api/app/services/curriculum/seed.py` | DB import of the curriculum content |
| `apps/api/app/services/curriculum/catalog.py` | Read + practice-grading query logic |
| `apps/api/app/schemas/curriculum.py` | Response schemas (CourseListItem, CourseDetail, ModuleCard, LessonCard, LessonDetail, ContentSection, VideoResource, PracticeItemView, PracticeGradeResult, CompetencyLink) |

### Curriculum API (`/api/curriculum`, auth required)
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/curriculum/courses` | Course list (code, title, description, credits, lesson count) |
| GET | `/api/curriculum/courses/{code}` | Course detail with module → lesson tree |
| GET | `/api/curriculum/lessons/{code}` | Lesson detail (title, minutes, prerequisites, competencies) |
| GET | `/api/curriculum/lessons/{code}/lecture` | Lecture content sections |
| GET | `/api/curriculum/lessons/{code}/summary` | Summary sections |
| GET | `/api/curriculum/lessons/{code}/videos` | Video resources (with scripts) |
| GET | `/api/curriculum/lessons/{code}/practice` | Practice items (answers never exposed) |
| POST | `/api/curriculum/lessons/{code}/practice/grade` | Server-side grading of an answer |

Registered in `apps/api/app/main.py`.

### Pivot changes to existing services
- `mock_data.py` — physics-only seed data; MEC271 no longer default/seedable
- `diagnostic_service.py`, `learning_service.py` — physics competencies; learning fallback competency is `charge-transfer`
- `student_model.py` — default course `PHY211`
- `bootstrap.py` — physics curriculum + legacy simulation footing backfill
- `simulation_contract.py` — `RUBRIC_CRITERIA` obligates the retained engine contract
- `db/models.py` — added `Course.description` column and `LessonCompetency.competency` relationship
- `db/database.py` — `_LIGHTWEIGHT_COLUMNS` for dev SQLite schema drift (courses.description)
- Fixed `seed.py` relative-import bug (`from ..db import …` → `from app.db import …`)

### Migration
- `alembic/versions/0007_curriculum_tables.py` — adds `courses.description` (upgrade `op.add_column`, downgrade `op.drop_column`). Dev SQLite `arete.db` is stamped at `0007`.

---

## 3. Frontend Curriculum UI

| File | Change |
|---|---|
| `apps/web/src/data/curriculum.ts` | **New.** Typed fetchers for every `/api/curriculum` endpoint |
| `apps/web/src/pages/Lecture.tsx` + `Lecture.css` | **Rewritten.** Curriculum lesson viewer — tabs: Lecture / Summary / Videos / Practice; server-side practice grading; markdown tables & bold rendered |
| `apps/web/src/pages/CourseDetail.tsx` | **Rewritten.** Fetches course from API; hero + overview stats (Modules / Lessons / Credits); module-grouped lesson tree linking to the lesson viewer; Continue-learning via first lesson; 404 + loading + error/retry states |
| `apps/web/src/pages/Courses.tsx` | **Rewritten.** Course list from `/api/curriculum/courses` with static-catalog fallback; per-card progress |

---

## 4. PID/MEC271 Product-Surface Strip

Removed from the user-visible product (infrastructure retained):

- **`Navbar.tsx`** — "Apply & Review" dropdown no longer lists Simulation or Transfer
- **`App.tsx`** — Simulation & Transfer routes and imports removed
- **`ApplyReview.tsx`** — Simulation tile removed; hub now offers Evidence Timeline + Review
- **Deleted** `pages/Simulation.tsx`, `pages/Simulation.css`, `pages/Transfer.tsx`, `pages/Transfer.css`
- **`index.html`** — titles/descriptions rebranded from MEC271 Automatic Control → PHY211 General Physics
- **Home copy** — `HomeFooter.tsx` (MEC271 → PHY211), `JourneySection.tsx`, `ValueProps.tsx` (simulation references made generic)

**Intentionally retained (legacy/infra):**
- `data/mockApi.ts` `runSimulation` + `types/index.ts` simulation types (required by `studentModel.test.ts`)
- Simulation engine, Mastery evidence, and `/api/simulation` endpoints (kept as dormant history)
- MEC271 course + deactivated instruments in the database (history)

---

## 5. Verification

- `apps/api/tests/test_curriculum_api.py` — 10 tests (courses list, course tree, lesson prerequisites, lecture/summary/video/practice views incl. answer-hiding, grade correct/wrong, 404s, 401 auth)
- `apps/api/tests/test_smoke.py` — updated to physics keys; `test_competencies` asserts the 5 physics competencies are a subset (legit legacy simulation side-effect may add a `pid-tuning` snapshot)
- Full backend suite 212 passed; frontend vitest 15 passed; lint clean; build clean

---

## 6. Tech Debt / Follow-ups

- `arete.db` uses `_LIGHTWEIGHT_COLUMNS` drift shim instead of a live alembic migration — acceptable for dev, but fresh environments should run `alembic upgrade head` from the last production stamp.
- GitHub repo deletion of `DevNinja00/unilead` still blocked: token lacks `delete_repo` scope (`gh auth refresh -h github.com -s delete_repo`) — owner action needed.
- Practice items, grading, and lesson content are single-lesson depth (L1 only). Expanding PHY211 to more lessons/modules is content work via `content.py`/`seed.py`.