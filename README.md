markdown
# 📊 Module 13: JWT Login/Registration with Client-Side Validation & Playwright E2E

## 🧩 Overview
This repository contains a FastAPI application that implements JWT‑based user registration and login, front‑end pages for registration and login, automated tests (unit, integration, and Playwright E2E), and a GitHub Actions CI/CD pipeline that runs tests and builds/pushes a Docker image.

## ⚙️ Features
- JWT‑based registration and login endpoints (`/users/register`, `/users/login`)
- Secure password hashing with bcrypt and JWT token creation/verification
- Pydantic schemas for input validation (email format, password length, etc.)
- Static front‑end pages (`static/register.html`, `static/login.html`) with client‑side validation
- Playwright browser E2E tests covering positive and negative flows
- GitHub Actions workflow to run tests and build/push Docker images to Docker Hub
# Module 14 — Calculations BREAD (Browse, Read, Edit, Add, Delete)

This repository contains a FastAPI application for user registration/login and a calculations API with full BREAD functionality for authenticated users. It includes unit, integration, and Playwright E2E tests and a GitHub Actions CI workflow that runs tests and builds/pushes a Docker image.

Contents
- `app/` — FastAPI application
- `static/` — static pages including `calculations.html` (BREAD demo)
- `tests/` — unit, integration, and E2E tests (Playwright)
- `.github/workflows/ci.yml` — CI pipeline (tests + Docker build/push)
- `create_tables.py` — helper to create DB tables

Quick start (local)
1. Clone and enter repo

```bash
git clone https://github.com/dmartino74/module14_is601.git
cd module14_is601
```

2. Create and activate a virtual environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
python -m playwright install --with-deps
```

4. Start the application

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/static/calculations.html` to try the BREAD demo UI.

Running tests
- Unit & Integration tests (fast, use in-memory DB for integration tests where configured):

```bash
pytest tests/unit tests/integration -q
```

- Full test suite (includes E2E / Playwright). Playwright tests need browsers installed (done above) and a running DB for certain E2E flows. To run all tests locally you can set `DATABASE_URL` to a Postgres instance, or run the full test suite in CI where Postgres service is provided.

```bash
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_db
pytest -q
```

CI (GitHub Actions)
- The workflow at `.github/workflows/ci.yml` runs on push/PR to `main`. It:
   - Starts a Postgres service
   - Installs Python deps and Playwright browsers
   - Runs `create_tables.py` to create DB schema
   - Runs `pytest`
   - Builds and pushes a Docker image when tests pass

GitHub Secrets required for Docker push
- `DOCKER_USERNAME` — your Docker Hub username
- `DOCKER_PASSWORD` — your Docker Hub password or access token

Add those in the repository Settings → Secrets before pushing to enable Docker push.

Docker (local)

```bash
docker build -t <your-docker-username>/module14_is601:latest .
docker run -p 8000:8000 --env DATABASE_URL="postgresql://..." <your-docker-username>/module14_is601:latest
```

Playwright E2E
- Install browsers once (done above): `python -m playwright install --with-deps`
- Run E2E tests:

```bash
pytest -q tests/e2e -k calculations
```

Notes about environment and tests
- Integration tests in `tests/integration` were updated to register and use temporary users (JWT) before calling `/calculations`. This scopes calculations to the authenticated user.
- CI uses Postgres service and runs `create_tables.py` to ensure tables exist (we added that step to the workflow).
- If you prefer to run CI without Playwright browser installation, I can make Playwright optional in the workflow.

Reflection & Submission Checklist
- Implemented: BREAD endpoints for calculations (user-scoped), frontend demo page, integration & Playwright tests, CI workflow that runs tests and builds Docker image.
- Still to collect: screenshots of a successful GitHub Actions run and a Docker Hub image push (these require the workflow to run with `DOCKER_*` secrets configured).

If you want, I can now:
- Update `reflection.md` with a narrative reflection (I will add that next),
- Add placeholders for screenshots and guidance on how to capture them,
- Or trigger additional changes you prefer.