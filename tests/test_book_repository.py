from lib.book_repository import BookRepository
from lib.book import Book

def test_get_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")

    repository = BookRepository(db_connection)

    books = repository.all()

    assert books == [
    Book(1, "The Gruffalo", "Julia Donaldson"),
    Book(2, "Ada Twist, Scientist", "Andrea Beaty"),
    Book(3, "The Girl Who Drank the Moon", "Kelly Barnhill"),
    Book(4, "Dragons in a Bag", "Zetta Elliott"),
]
    
def test_create_new_book(page, test_web_address, db_connection):
    page.context.clear_cookies()
    page.goto(f"http://{test_web_address}/login")

    page.fill("input[name='username']", "test_user")
    page.fill("input[name='password']", "password123")
    page.click("input[type='submit']")
    page.wait_for_url(f"http://{test_web_address}/books", timeout=5000)

    page.goto(f"http://{test_web_address}/books/new")

    page.fill("input[name='title']", "Dune")
    page.fill("input[name='author_name']", "Frank Herbert")
    page.click("text=Add book")

    assert page.url == f"http://{test_web_address}/books"
    books = page.locator("li")
    assert "Dune" in books.all_inner_texts()[-1]
    # books = page.locator(".book")
    # assert "Dune" in books.all_inner_texts()[-1]