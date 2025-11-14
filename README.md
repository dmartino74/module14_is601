📊 Module 12: Calculation Model with Factory Pattern & CI/CD
🧩 Overview
This module implements a robust Calculation service using FastAPI, SQLAlchemy, and Pydantic. It supports basic arithmetic operations via a factory pattern and integrates automated testing and Docker deployment through GitHub Actions.

⚙️ Features
SQLAlchemy model for storing calculations (id, a, b, type, result, timestamps)

Pydantic schemas for input validation and output serialization

Factory pattern for extensible operation logic (add, sub, mul, div)

Unit and integration tests using pytest

CI/CD pipeline with GitHub Actions

Dockerized FastAPI app with PostgreSQL backend

🚀 How to Run Locally
1. Clone the Repository
bash
git clone https://github.com/dmartino74/module12_is601.git
cd module12_is601
2. Create and Activate Virtual Environment
bash
python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate.bat  # Windows
3. Install Dependencies
bash
pip install -r requirements.txt
4. Run the App
bash
uvicorn app.main:app --reload
Visit http://localhost:8000/docs for Swagger UI.

🧪 Testing
Run All Tests
bash
pytest
Check Coverage
bash
pytest --cov=app --cov-report=html
Tests include:

✅ Unit tests for operation classes and schema validation

✅ Integration tests for database CRUD and FastAPI routes

✅ Edge cases: divide-by-zero, invalid operation types

🐳 Docker Setup
Build Image
bash
docker build -t module12_is601:latest .
Run Container
bash
docker run -d -p 8000:8000 --name module12_container module12_is601:latest
Or use Docker Compose:

bash
docker-compose build
docker-compose up -d
Access app: http://localhost:8000 Access pgAdmin: http://localhost:5050

🔁 CI/CD Pipeline
GitHub Actions automates:

🧪 Test job: runs pytest on push/PR

🐳 Docker job: builds and pushes image to Docker Hub

Docker Hub Repo
[Your Docker Hub Link Here]

🧠 Reflection
This module reinforced key backend development skills:

Implemented a clean service layer using SQLAlchemy and Pydantic

Applied the factory pattern to decouple operation logic

Used GitHub Actions to automate testing and deployment

Dockerized the app for reproducible deployment

Challenges included refactoring from functions to classes, ensuring test coverage, and debugging CI/CD workflows.

📎 Submission Checklist
[x] SQLAlchemy model and Pydantic schemas

[x] Factory pattern implemented

[x] Unit and integration tests passing

[x] GitHub Actions workflow configured

[x] Docker image pushed to Docker Hub

[x] README and reflection included

[x] GitHub repo link submitted