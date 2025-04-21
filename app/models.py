# app/models.py
#----------------------
# For the creation of the database models 
#----------------------
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from .extensions import db

# ------------------------------
# User Models - stores login and profile data
# ------------------------------
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email    = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    account = db.relationship('BankAccount', backref='user', uselist=False)

# ------------------------------
# BankAccount Model - created to hold the account number and balance info 
# ------------------------------
class BankAccount(db.Model):
    __tablename__ = 'bank_accounts'
    id         = db.Column(db.Integer, primary_key=True)
    account_no = db.Column(db.String(12), unique=True, nullable=False)
    balance    = db.Column(db.Float, default=0)
    user_id    = db.Column(db.Integer, db.ForeignKey('users.id'))

# ------------------------------
# Transaction Model - stores the fund transfer info
# ------------------------------
class Transaction(db.Model):
    __tablename__ = 'transactions'
    id          = db.Column(db.Integer, primary_key=True)
    sender_id   = db.Column(db.Integer, db.ForeignKey('bank_accounts.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('bank_accounts.id'))
    amount      = db.Column(db.Float, nullable=False)
    timestamp   = db.Column(db.DateTime, server_default=db.func.now())

    sender   = db.relationship('BankAccount', foreign_keys=[sender_id], backref='sent_txns')
    receiver = db.relationship('BankAccount', foreign_keys=[receiver_id], backref='received_txns')
