from app.forms import LoginForm, SignupForm

def test_login_form_validation():
    form = LoginForm(data={"username": "john", "password": "secret123"})
    assert form.validate()

def test_signup_form_validation():
    form = SignupForm(data={
        "username": "jane",
        "email": "jane@example.com",
        "password": "secure456"
    })
    assert form.validate()