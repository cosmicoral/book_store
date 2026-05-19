from lib.database_connection import DatabaseConnection
from flask import Flask, render_template, request, redirect
from lib.book_repository import BookRepository
from lib.book import Book
from lib.film_repository import FilmRepository
from lib.film import Film
from lib.user import User
from lib.user_repository import UserRepository

# instantiate a Flask app object
app = Flask(__name__)
connection = DatabaseConnection()
connection.connect()

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"


@app.route('/users/new')
def get_new_user():
    return render_template('signup_form.html')

@app.route('/users', methods=['POST'])
def create_user():

    user_repository = UserRepository(connection)

    user_details = request.form

    user = User(
        username=user_details["username"],
        password=user_details["password"]
    )

    user_repository.create(user)

    return redirect("/books")

@app.route('/books', methods=['GET'])
def books():
    book_repository = BookRepository(connection)
    books = book_repository.all()
    return render_template("books.html", books=books)

@app.route("/books/new", methods =["GET"])
def new_book():
    return render_template("new_book.html")

@app.route("/books", methods = ["POST"])
def create_book():
    book_details = request.form
    title = book_details["title"]
    author_name = book_details["author_name"]
    repository = BookRepository(connection)
    book = Book(None, title, author_name)
    repository.create(book)
    print(book_details)
    return redirect("/books")

    
@app.route("/authors", methods=["GET"])
def authors():
    return [
        {"name": "Julia Donaldson", "dob": "1948-09-16"},
        {"name": "Andrea Beaty", "dob": "1961-10-08"},
        {"name": "Kelly Barnhill", "dob": "1973-01-01"},
        {"name": "Zetta Elliott", "dob": "1979-11-11"},
    ]

@app.route("/films", methods=["GET"])
def get_new_film():
    film_repository = FilmRepository(connection)
    films = film_repository.all()
    return render_template("films.html", films=films)

@app.route("/films", methods=["POST"])
def create_new_film():
    film_details = request.form
    title = film_details["title"]
    release_year = film_details["release_year"]
    director = film_details["director"]
    repository = FilmRepository(connection)
    film = Film(title, release_year, director)
    repository.create(film)
    print(film_details)
    return redirect("/films")

print(app.url_map)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
