import pytest
from app import create_app
from app.models import User, accounts_db, BankAccount

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()

    # Create test user + bank account
    user = User('1', 'alice', 'secret123', 'alice@example.com')
    accounts_db['1'] = BankAccount(user_id='1', account_no='123456789012', balance=1000)
    from flask_login import login_user

    @app.before_request
    def auto_login():
        login_user(user)

    return client

def test_dashboard_displays_account(client):
    response = client.get('/dashboard')
    assert b'Your Account' in response.data
    assert b'123456789012' in response.data
