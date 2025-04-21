def test_dashboard_requires_login(client):
    res = client.get("/dashboard", follow_redirects=True)
    assert b"Login" in res.data