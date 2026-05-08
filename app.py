from lib.database_connection import DatabaseConnection
from flask import Flask, render_template
from lib.book_repository import BookRepository

# instantiate a Flask app object
app = Flask(__name__)

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

@app.route('/hello', methods=['GET'])
def hello_again():
    return "Hello, hello and hello again!"

@app.route('/books', methods=['GET'])
def books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    return render_template("books.html", books=books)
    
@app.route("/authors", methods=["GET"])
def authors():
    return [
        {"name": "Julia Donaldson", "dob": "1948-09-16"},
        {"name": "Andrea Beaty", "dob": "1961-10-08"},
        {"name": "Kelly Barnhill", "dob": "1973-01-01"},
        {"name": "Zetta Elliott", "dob": "1979-11-11"},
    ]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
