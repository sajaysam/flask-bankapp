from app.models import User, BankAccount

def test_user_model():
    user = User(username="alice", email="alice@example.com", password="test123")
    assert user.username == "alice"
    assert user.email == "alice@example.com"

def test_bank_account_model():
    account = BankAccount(account_no="123456789012", balance=5000)
    assert account.account_type == "savings"
    assert account.balance == 5000