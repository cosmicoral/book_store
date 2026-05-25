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

<!-- # Database Project Starter

This is a starter project for you to use to start your Python database projects.

There are two videos to support:

* [A demonstration of setting up the project](https://www.youtube.com/watch?v=KMEt4GgWJXc)
* [A walkthrough of the project codebase](https://youtu.be/KMEt4GgWJXc?t=460)

## Setup

### 1. Clone the repository to your local machine
```
; git clone git@github.com:makersacademy/databases-in-python-project-starter.git YOUR_PROJECT_NAME
```

> Or, if you don't have SSH keys set up
```
; git clone https://github.com/makersacademy/databases-in-python-project-starter.git YOUR_PROJECT_NAME
```

### 2. Enter the directory
```
; cd YOUR_PROJECT_NAME
```

### 3. Set up the virtual environment
```
; python -m venv databases-starter-venv
```

### 4. Activate the virtual environment
```
; source databases-starter-venv/bin/activate 
```


### 5. Install dependencies
```
(databases-starter-venv); pip install -r requirements.txt
```

> Read below if you see an error with `python_full_version`

### 6. Create the database
```
(databases-starter-venv); createdb YOUR_PROJECT_NAME
```

> `YOUR_PROJECT_NAME` can be anything you want it to be

### 7. Change `DATABASE_NAME` to equal `YOUR_PROJECT_NAME`

On line 11 of `lib/database_connection.py` you'll find this...

```
DATABASE_NAME = "DEFAULT_MAKERS_PROJECT" # <-- CHANGE THIS!
```

Change `DEFAULT_MAKERS_PROJECT` to whatever you chose for `YOUR_PROJECT_NAME`

### 8. Run the tests - see below if you have any issues
```
(databases-starter-venv); pytest
```
> If the tests fail, see below

### 9. Run the app
```
(databases-starter-venv); python app.py
```

<br>
<details>
  <summary>I get a <code>ModuleNotFoundError: No module named 'psycopg'</code></summary>
  <br>
If, after activating your <code>venv</code> and installing dependencies, you see this error when running <code>pytest</code>, please deactivate and reactivate your <code>venv</code>. This should solve the problem - if not, contact your coach.
</details>
<br>
<details>
  <summary>The tests fails and I see <code>Exception: Couldn't connect to the database DEFAULT_MAKERS_PROJECT!</code></summary>
  <br>
This error most likely means you need to edit line 11 in <code>lib/database_connection.py</code>. Go there and change <code>"DEFAULT_MAKERS_PROJECT"</code> to the name of the database you created in step 6.
</details> -->
