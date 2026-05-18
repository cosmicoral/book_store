from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM books")
    
        books = []
        for row in rows:
            books.append(Book(row["id"], row["title"], row["author_name"]))
        
        return books
    
    def create(self, book):
        self._connection.execute(
        "INSERT INTO books(title, author_name) VALUES (%s, %s)",
        [book.title, book.author_name])