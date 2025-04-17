import pytest
from app import create_app
from app.models import User, accounts_db, BankAccount

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()

    # Create user + account
    user = User('1', 'john', 'secret123', 'john@bank.com')
    accounts_db['1'] = BankAccount(user_id='1', account_no='999999999999', balance=500)

    from flask_login import login_user

    @app.before_request
    def auto_login():
        login_user(user)

    return client

def test_api_balance(client):
    res = client.get('/api/balance')
    assert res.status_code == 200
    data = res.get_json()
    assert data['account_number'] == '999999999999'
    assert data['balance'] == 500
    assert data['email'] == 'john@bank.com'
