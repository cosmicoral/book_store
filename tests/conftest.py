import pytest
import threading
import time
from lib.database_connection import DatabaseConnection
from app import app
from werkzeug.serving import make_server

@pytest.fixture(scope="session")
def test_web_address():
    server = make_server("127.0.0.1", 5001, app)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    time.sleep(0.5)
    return "127.0.0.1:5001"

@pytest.fixture
def db_connection():
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/book_store.sql")
    yield connection
    connection.connection.close()  # 测试结束后关闭连接
    
@pytest.fixture
def web_client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client
# import os
# import pytest
# from lib.database_connection import DatabaseConnection
# from app import app
# import threading

# # This is a Pytest fixture.
# # A fixture is a reusable function that provides setup 
# # logic for tests, supplying data or state before a test 
# # runs and cleaning up afterward.
# #
# # In our project, it creates an object that we can use in our tests.
# # We will use it to create a database connection.

# @pytest.fixture(scope="session")
# def test_web_address():
#     app.config["TESTING"] = True
#     thread = threading.Thread(target=lambda: app.run(port=5001, use_reloader=False))
#     thread.daemon = True
#     thread.start()
#     return "127.0.0.1:5001"

# @pytest.fixture
# def db_connection():
#     connection = DatabaseConnection()
#     connection.connect()
#     connection.seed("seeds/book_store.sql")

#     return connection


# @pytest.fixture
# def web_client():
#     app.config["TESTING"] = True

#     with app.test_client() as test_client:
#         yield test_client


# @pytest.fixture
# def test_web_address():
#     return "127.0.0.1:5001"

# # Now, when a test includes a parameter named `db_connection`, Pytest automatically
# # calls this fixture before the test runs and passes in its return value instead 
# # of the function itself.
# # We don’t need to call `db_connection()` or `db_connection.connect()` manually.

# # For example:

# # def test_something(db_connection):
# #     # db_connection's return value is now available to us in this test.

# # More information on Pytest fixtures: https://www.tutorialspoint.com/pytest/pytest_fixtures.htm
