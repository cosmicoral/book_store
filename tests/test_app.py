import sys
import os
from playwright.sync_api import Page
from lib.database_connection import DatabaseConnection

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_get_books_returns_a_200():
    client = app.test_client()
    response = client.get("/books")
    assert response.status_code == 200


def test_get_books_page_contains_books():
    client = app.test_client()
    response = client.get("/books")

    assert response.status_code == 200
    assert b"The Gruffalo" in response.data
    assert b"Ada Twist, Scientist" in response.data
    assert b"The Girl Who Drank the Moon" in response.data
    assert b"Dragons in a Bag" in response.data

def test_get_authors_returns_a_200():
    client = app.test_client()
    response = client.get("/authors")
    assert response.status_code == 200


def test_get_authors_returns_all_the_authors():
    client = app.test_client()
    response = client.get("/authors")
    assert response.json == [
        {"name": "Julia Donaldson", "dob": "1948-09-16"},
        {"name": "Andrea Beaty", "dob": "1961-10-08"},
        {"name": "Kelly Barnhill", "dob": "1973-01-01"},
        {"name": "Zetta Elliott", "dob": "1979-11-11"},
    ]

def test_can_create_new_book(page, test_web_address, db_connection):
    page.context.clear_cookies()
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name='username']", "test_user")
    page.fill("input[name='password']", "password123")
    page.click("input[type='submit']")
    page.wait_for_url(f"http://{test_web_address}/books")

    page.goto(f"http://{test_web_address}/books/new")
    page.fill("input[name='title']", "Dune")
    page.fill("input[name='author_name']", "Frank Herbert")
    page.click("input[type='submit']")

    page.wait_for_url(f"http://{test_web_address}/books", timeout=5000)

    assert page.locator("body").inner_text().__contains__("Dune")

    # connection = DatabaseConnection()
    # connection.connect()
    # connection.seed("seeds/books.sql")

    # page.goto("http://localhost:5001/books")

    # page.get_by_placeholder("Title").fill("Dune")

    # page.get_by_placeholder("Author").fill("Frank Herbert")

    # page.get_by_role("button", name="Submit").click()

    # books = page.locator("li")

    # actual_books = books.all_inner_texts()

    # assert "Dune - Frank Herbert" in actual_books