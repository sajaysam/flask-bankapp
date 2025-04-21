from app.models import User, BankAccount
from werkzeug.security import generate_password_hash
from app.extensions import db

def test_transfer(client, app):
    with app.app_context():
        user1 = User(username="alice", email="alice@mail.com", password=generate_password_hash("pass"))
        user2 = User(username="bob", email="bob@mail.com", password=generate_password_hash("pass"))
        db.session.add_all([user1, user2])
        db.session.commit()

        acc1 = BankAccount(user_id=user1.id, account_no="100001", balance=5000)
        acc2 = BankAccount(user_id=user2.id, account_no="100002", balance=1000)
        db.session.add_all([acc1, acc2])
        db.session.commit()

    client.post("/login", data={"username": "alice", "password": "pass"}, follow_redirects=True)

    res = client.post("/transfer", data={
        "to_account": "100002",
        "amount": 500
    }, follow_redirects=True)

    assert b"Transfer successful" in res.data
