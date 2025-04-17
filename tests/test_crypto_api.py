import pytest
from app.routes import get_crypto_prices

def test_crypto_mock_response(monkeypatch):
    class MockResponse:
        def json(self):
            return {"Markets": [{"Label": "BTC/USD", "Price": 30000}]}

    monkeypatch.setattr("requests.get", lambda url: MockResponse())
    data = get_crypto_prices()
    assert data[0][0] == "BTC/USD"
    assert data[0][1] == 30000