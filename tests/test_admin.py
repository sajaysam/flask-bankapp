import pytest
from app import create_app
from app.models import User, accounts_db, BankAccount

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()

    # Admin + test user
    admin = User('1', 'admin', 'adminpass', 'admin@bank.com')
    user = User('2', 'jane', 'password', 'jane@bank.com')
    accounts_db['2'] = BankAccount(user_id='2', account_no='888888888888', balance=900.0)

    from flask_login import login_user

    @app.before_request
    def auto_login():
        login_user(admin)

    return client

def test_admin_access(client):
    res = client.get('/admin')
    assert b'Admin Panel' in res.data
    assert b'888888888888' in res.data

def test_non_admin_blocked():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()

    non_admin = User('3', 'notadmin', 'pass', 'x@x.com')
    from flask_login import login_user

    @app.before_request
    def auto_login():
        login_user(non_admin)

    res = client.get('/admin', follow_redirects=True)
    assert b'Access denied' in res.data
