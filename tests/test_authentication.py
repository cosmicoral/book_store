from lib.database_connection import DatabaseConnection

def test_successful_login_redirects_to_books(web_client, db_connection):
    response = web_client.post("/sessions", data={
        "username": "test_user",
        "password": "password123"
    })

    assert response.status_code == 302
    assert response.headers["Location"] == "/books"

def test_failed_login_redirects_to_signup(web_client, db_connection):
    response = web_client.post("/sessions", data={
        "username": "wrong_user",
        "password": "wrong_password"
    })

    assert response.status_code == 302
    assert response.headers["Location"] == "/users/new"

def test_user_can_log_in(page, test_web_address, db_connection):
    page.context.clear_cookies()

    page.goto(f"http://{test_web_address}/login")

    page.fill("input[name='username']", "test_user")
    page.fill("input[name='password']", "password123")
    page.click("input[type='submit']")
    page.wait_for_url(f"http://{test_web_address}/books")

    assert page.url == f"http://{test_web_address}/books"