
# -----------------------------------------
# Database Models for Flask Bank App
# -----------------------------------------
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from .extensions import db

# ------------------------------
#  User Model
# ------------------------------
class User(UserMixin, db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email    = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    account = db.relationship('BankAccount', backref='user', uselist=False)

# ------------------------------
# BankAccount Model
# ------------------------------
class BankAccount(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    account_no = db.Column(db.String(12), unique=True, nullable=False)
    balance    = db.Column(db.Float, default=0)
    user_id    = db.Column(db.Integer, db.ForeignKey('user.id'))

# ------------------------------
#  Transaction Model
# ------------------------------
class Transaction(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    sender_id   = db.Column(db.Integer, db.ForeignKey('bank_account.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('bank_account.id'))
    amount      = db.Column(db.Float, nullable=False)
    timestamp   = db.Column(db.DateTime, server_default=db.func.now())

    sender   = db.relationship('BankAccount', foreign_keys=[sender_id], backref='sent_txns')
    receiver = db.relationship('BankAccount', foreign_keys=[receiver_id], backref='received_txns')


# Simulate a basic user "database"
#users_db = {}

#class User(UserMixin):
 #   def __init__(self, id, username, password, email):
   #     self.id = id
    #    self.username = username
   #     self.password_hash = generate_password_hash(password)
    #    self.email = email
   #     self.is_admin = username == 'admin'  # Simple admin check
        
   # def check_password(self, password):
  #      return check_password_hash(self.password_hash, password)

   # def get_id(self):
      #  return str(self.id)
#
# Simulated bank accounts
#accounts_db = {}

#class BankAccount:
#    def __init__(self, user_id, account_no, balance=0.0):
#       self.user_id = user_id
 #       self.account_no = account_no
 #       self.balance = balance

#transactions account
#transactions_db = []

#class Transaction:
 #   def __init__(self, sender_id, receiver_id, amount):
  #      self.sender_id = sender_id
   #     self.receiver_id = receiver_id
 #       self.amount = amount
 #       self.timestamp = datetime.datetime.now(datetime.UTC)
#
#in-memory list to simulate logs 
#action_logs = []  # In-memory list to simulate logs

### ----- 