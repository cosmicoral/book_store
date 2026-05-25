# Book Store Web App

A full-stack Flask web application built during the Makers bootcamp, featuring:

- PostgreSQL database integration
- User authentication and sessions
- Protected routes with authorisation
- Repository pattern architecture
- Integration and end-to-end testing
- Docker deployment
- CI/CD with GitHub Actions
- EC2 deployment

---

# Features

## Authentication
- User signup
- User login
- Session-based authentication
- Protected routes using `@login_required`

## Books
- View all books
- Add new books
- Persistent PostgreSQL storage

## Films
- View films
- Add films

## Testing
- Pytest integration tests
- Playwright end-to-end browser tests
- Test database isolation with reseeding

## Deployment
- Dockerised Flask app
- PostgreSQL container
- Automated CI/CD pipeline
- Automatic deployment to AWS EC2

---

# Tech Stack

- Python 3.13
- Flask
- PostgreSQL
- Psycopg
- Pytest
- Playwright
- Docker
- GitHub Actions
- AWS EC2

---

# Project Structure

```text
book_store/
├── app.py
├── requirements.txt
├── Dockerfile
├── lib/
├── templates/
├── static/
├── tests/
├── seeds/
└── .github/workflows/

Setup Instructions
1. Clone the repository
git clone <YOUR_REPOSITORY_URL>
cd book_store
2. Create a virtual environment
python -m venv book_store_venv
3. Activate the virtual environment
Mac/Linux
source book_store_venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
Database Setup
1. Create development database
createdb book_store
2. Create test database
createdb book_store_test
3. Seed development database
psql book_store < seeds/book_store.sql
4. Seed test database
psql book_store_test < seeds/book_store.sql
Running the App
DATABASE_NAME=book_store python app.py

The app will run at:

http://127.0.0.1:5001
Running Tests
Run all tests
DATABASE_NAME=book_store_test python -m pytest tests -sv
Run a single test file
DATABASE_NAME=book_store_test python -m pytest tests/test_authentication.py -sv
Docker
Build image
docker build -t book_store .
Run PostgreSQL container
docker run \
  --name book_store_db \
  --network book_store_network \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=book_store \
  -d postgres:17
Run app container
docker run -p 5001:5001 book_store
CI/CD

This project uses GitHub Actions for:

Continuous Integration (CI)
Runs automated tests on every push and pull request
Sets up PostgreSQL test database
Runs Playwright and Pytest test suites
Continuous Deployment (CD)
Automatically deploys the app to AWS EC2 after pushing to main

Workflow files:

.github/workflows/ci.yml
.github/workflows/deploy.yml
Common Debugging Commands
Docker
docker container ls -a
docker logs <container_id>
docker exec -it <container_id> bash
docker inspect <container_id>
Database
psql book_store
psql book_store_test
GitHub Actions

Check logs in:

GitHub Repository → Actions
Learning Goals

This project was used to practice:

Flask web development
SQL and PostgreSQL
Authentication and sessions
Repository pattern
Integration testing
End-to-end testing
Docker
CI/CD pipelines
Cloud deployment workflows