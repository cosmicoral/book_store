from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        self._connection.connect()

        rows = self._connection.connection.execute(
            "SELECT * FROM books"
        ).fetchall()

        books = []

        for row in rows:
            books.append(
                Book(
                    row["id"],
                    row["title"],
                    row["author_name"]
                )
            )

        return books

    def create(self, book):
        self._connection.connect()

        self._connection.connection.execute(
            "INSERT INTO books(title, author_name) VALUES (%s, %s)",
            [book.title, book.author_name]
        )

        self._connection.connection.commit()



# old one：
# from lib.book import Book

# class BookRepository:
#     def __init__(self, connection):
#         self._connection = connection

#     def all(self):
#         cursor = self._connection.cursor()
#         cursor.execute("SELECT * FROM books")

#         rows = cursor.fetchall()
    
#         books = []
#         for row in rows:
#             books.append(Book(row["id"], row["title"], row["author_name"]))
        
#         return books
    
#     def create(self, book):
#         cursor = self._connection.cursor()
#         cursor.execute(
#         "INSERT INTO books(title, author_name) VALUES (%s, %s)",
#         [book.title, book.author_name])