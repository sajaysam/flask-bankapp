from app.models import User, BankAccount
from werkzeug.security import generate_password_hash
from app.extensions import db

def test_transfer_and_history(client, app):
    with app.app_context():
        u1 = User(username="u1", email="u1@mail.com", password=generate_password_hash("pass"))
        u2 = User(username="u2", email="u2@mail.com", password=generate_password_hash("pass"))
        db.session.add_all([u1, u2])
        db.session.commit()

        a1 = BankAccount(account_no="1001", balance=5000, user_id=u1.id)
        a2 = BankAccount(account_no="1002", balance=2000, user_id=u2.id)
        db.session.add_all([a1, a2])
        db.session.commit()

    client.post("/login", data={"username": "u1", "password": "pass"}, follow_redirects=True)
    client.post("/transfer", data={"to_account": "1002", "amount": 500}, follow_redirects=True)

    res = client.get("/transactions")
    assert b"1002" in res.data or b"500" in res.data
