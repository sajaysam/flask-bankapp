
# -----------------------------------------------------
# Flask-WTF Forms for User Input and Validation, this shows the definitions for user input
# -----------------------------------------------------

# FlaskForm is the base class for creating web forms in Flask
from flask_wtf import FlaskForm
# Form field types
from wtforms import StringField, PasswordField, SubmitField
# Built-in validators to ensure clean and safe user input
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import DecimalField
from wtforms.validators import NumberRange

# ------------------------------
# Signup Form - fields for registration
# ------------------------------
class SignupForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6)]
    )
    confirm = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password', message='Passwords must match.')]
    )
    submit = SubmitField('Sign Up')


# ------------------------------
# Login Form - login form authenticates the users 
# ------------------------------
class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    submit = SubmitField('Login')


# ------------------------------
# Money Transfer Form - money transfer form is for sending money from one existing user to another. 
# ------------------------------

class TransferForm(FlaskForm):
    to_account = StringField('Receiver Account #', validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[DataRequired(), NumberRange(min=0.01)])
    submit = SubmitField('Send')
