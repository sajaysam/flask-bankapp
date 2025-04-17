import pytest
from app import create_app
from app.models import User, accounts_db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()

    # Mock user
    user = User('1', 'testuser', 'secret123', 'test@bank.com')

    from flask_login import login_user

    @app.before_request
    def auto_login():
        login_user(user)

    return client

def test_open_account_success(client):
    assert '1' not in accounts_db
    res = client.post('/open_account', follow_redirects=True)
    assert b'Account created successfully' in res.data
    assert '1' in accounts_db

def test_open_account_duplicate(client):
    from app.models import BankAccount
    accounts_db['1'] = BankAccount(user_id='1', account_no='999999999999')
    res = client.get('/open_account', follow_redirects=True)
    assert b'already have an account' in res.data
