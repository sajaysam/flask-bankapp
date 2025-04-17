import pytest
from app import create_app
from app.models import User, BankAccount, accounts_db, transactions_db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()

    # Setup users and accounts
    user1 = User('1', 'alice', 'pass123', 'a@x.com')
    user2 = User('2', 'bob', 'pass123', 'b@x.com')
    accounts_db['1'] = BankAccount(user_id='1', account_no='111111111111', balance=500.0)
    accounts_db['2'] = BankAccount(user_id='2', account_no='222222222222', balance=100.0)

    from flask_login import login_user

    @app.before_request
    def auto_login():
        login_user(user1)

    return client

def test_transfer_success(client):
    r = client.post('/transfer', data={'to_account': '222222222222', 'amount': '100'}, follow_redirects=True)
    assert b'Transfer successful' in r.data
    assert accounts_db['1'].balance == 400.0
    assert accounts_db['2'].balance == 200.0

def test_transfer_fail_insufficient(client):
    r = client.post('/transfer', data={'to_account': '222222222222', 'amount': '9999'}, follow_redirects=True)
    assert b'Insufficient funds' in r.data
