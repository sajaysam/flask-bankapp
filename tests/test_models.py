from app.models import User, BankAccount, Transaction

def test_user_model(app):
    with app.app_context():
        user = User(username="test", email="test@mail.com", password="hash")
        assert user.username == "test"

def test_account_model(app):
    with app.app_context():
        acct = BankAccount(account_no="123456789012", balance=10000.0)
        assert acct.balance == 10000.0

def test_transaction_model(app):
    with app.app_context():
        tx = Transaction(sender_id=1, receiver_id=2, amount=500.0)
        assert tx.amount == 500.0
