import sys 
import os 
from playwright.sync_api import Page, expect

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import * 

#1
"""
If we send a GET request through the index route
Status code 200 is returned 
"""
def test_index_returns_200():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200 
    assert b"Welcome to the music club!"

#2
"""
If we send a GET request through the films route
Status code 200 is returned 
"""
def test_films_returns_200():
    client = app.test_client()

    response = client.get("/films")

    assert response.status_code == 200 
    assert b"2025 best films"

#3
"""
If we send a GET request through the index route
the text is rendered as expected
"""

def test_text_in_index_route(page: Page):
    page.goto("http://127.0.0.1:5001/films")

    text = page.locator("h1")

    expect(text).to_have_text("2025 best films")