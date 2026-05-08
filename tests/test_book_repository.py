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