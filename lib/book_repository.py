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