import pytest

def test_signup_login_logout(client):
    res = client.post("/signup", data={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    }, follow_redirects=True)
    assert b"Account created" in res.data or b"Please log in" in res.data

    res = client.post("/login", data={
        "username": "testuser",
        "password": "password123"
    }, follow_redirects=True)
    assert b"Dashboard" in res.data or b"Transfer" in res.data

    res = client.get("/logout", follow_redirects=True)
    assert b"Login" in res.data