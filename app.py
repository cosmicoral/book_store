from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository

connection = DatabaseConnection()
connection.connect()

repository = BookRepository(connection)

books = repository.all()

for book in books:
    print(f"{book.id} - {book.title} - {book.author_name}")