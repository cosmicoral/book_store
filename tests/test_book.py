from lib.book import Book

def test_constructs():
    book = Book(1, "Nineteen Eight-Four", "George Orwell")

    assert book.id == 1
    assert book.title == "Nineteen Eight-Four"
    assert book.author_name == "George Orwell"

def test_format_nicely():
    book = Book(1, "Nineteen Eighty-Four", "George Orwell")

    assert str(book) == "Book(1, Nineteen Eighty-Four, George Orwell)"