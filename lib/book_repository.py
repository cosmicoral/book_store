from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM books")

        rows = cursor.fetchall()
    
        books = []
        for row in rows:
            books.append(Book(row["id"], row["title"], row["author_name"]))
        
        return books
    
    def create(self, book):
        cursor = self._connection.cursor()
        cursor.execute(
        "INSERT INTO books(title, author_name) VALUES (%s, %s)",
        [book.title, book.author_name])