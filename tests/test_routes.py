def test_home_page(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Welcome" in res.data or b"Login" in res.data