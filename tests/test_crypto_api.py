def test_homepage_crypto_loads(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"BTC" in res.data or b"ETH" in res.data