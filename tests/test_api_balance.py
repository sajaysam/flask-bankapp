from app.models import User, BankAccount
from werkzeug.security import generate_password_hash
from app.extensions import db

def test_api_balance(client, app):
    with app.app_context():
        user = User(username="sajay", email="sajaysam@hotmail.com", password=generate_password_hash("pass"))
        db.session.add(user)
        db.session.commit()

        acct = BankAccount(account_no="9999", balance=3000, user_id=user.id)
        db.session.add(acct)
        db.session.commit()

    client.post("/login", data={"username": "apiuser", "password": "pass"}, follow_redirects=True)
    res = client.get("/api/balance")
    assert res.status_code == 200
    assert b"balance" in res.data