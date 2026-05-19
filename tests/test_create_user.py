from app import app
from lib.database_connection import DatabaseConnection

def test_create_user_is_saved_to_database():

    # create test client
    client = app.test_client()

    # connect to database
    connection = DatabaseConnection()
    connection.connect()

    # clear users table
    connection.execute("TRUNCATE TABLE users;")

    # send POST request
    response = client.post('/users', data={
        'username': 'testuser',
        'password': 'password123'
    })

    # check redirect happened
    assert response.status_code == 302

    # read database
    result = connection.execute(
        "SELECT * FROM users WHERE username = 'testuser';"
    )

    # assert user exists
    assert len(result) == 1

    assert result[0]['username'] == 'testuser'