# app/auth.py

from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, BankAccount, Transaction
from .forms import SignupForm, LoginForm, TransferForm
from .extensions import db
import random

auth = Blueprint('auth', __name__)

# -------------------------------
# Signup Route
# -------------------------------
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash("Username already exists.", "error")
            return redirect(url_for('auth.signup'))
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
            is_admin=(form.username.data == "admin")
        )
        db.session.add(user)
        db.session.commit()
        flash('Account created! Please log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)

# -------------------------------
# Login Route
# -------------------------------
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('auth.dashboard'))
        flash("Invalid credentials", "error")
    return render_template('login.html', form=form)

# -------------------------------
# Logout Route
# -------------------------------
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

# -------------------------------
# Dashboard
# -------------------------------
@auth.route('/dashboard')
@login_required
def dashboard():
    account = BankAccount.query.filter_by(user_id=current_user.id).first()
    if not account:
        return redirect(url_for('auth.open_account'))
    return render_template('dashboard.html', account=account)

# -------------------------------
# Open Bank Account
# -------------------------------
@auth.route('/open_account', methods=['GET', 'POST'])
@login_required
def open_account():
    if BankAccount.query.filter_by(user_id=current_user.id).first():
        flash("You already have an account.", "info")
        return redirect(url_for('auth.dashboard'))
    if request.method == 'POST':
        acct_no = str(random.randint(10**11, 10**12 - 1))
        account = BankAccount(account_no=acct_no, balance=0.0, user_id=current_user.id)
        db.session.add(account)
        db.session.commit()
        flash("Account created!", "success")
        return redirect(url_for('auth.dashboard'))
    return render_template('open_account.html')

# -------------------------------
# Transfer Money
# -------------------------------
@auth.route('/transfer', methods=['GET', 'POST'])
@login_required
def transfer():
    sender = BankAccount.query.filter_by(user_id=current_user.id).first()
    form = TransferForm()
    if form.validate_on_submit():
        receiver = BankAccount.query.filter_by(account_no=form.to_account.data).first()
        if not receiver:
            flash("Receiver not found", "error")
        elif sender.account_no == receiver.account_no:
            flash("Cannot transfer to your own account", "error")
        elif sender.balance < form.amount.data:
            flash("Insufficient funds", "error")
        else:
            sender.balance -= float(form.amount.data)
            receiver.balance += float(form.amount.data)
            txn = Transaction(sender=sender, receiver=receiver, amount=form.amount.data)
            db.session.add(txn)
            db.session.commit()
            flash("Transfer successful", "success")
            return redirect(url_for('auth.dashboard'))
    return render_template('transfer.html', form=form, balance=sender.balance)

# -------------------------------
# Transaction History
# -------------------------------
@auth.route('/transactions')
@login_required
def transactions():
    account = BankAccount.query.filter_by(user_id=current_user.id).first()
    sent = Transaction.query.filter_by(sender_id=account.id)
    received = Transaction.query.filter_by(receiver_id=account.id)
    all_txns = sent.union(received).order_by(Transaction.timestamp.desc())
    return render_template('transactions.html', history=all_txns, acct=account)

# -------------------------------
# Admin Panel
# -------------------------------
@auth.route('/admin')
@login_required
def admin_panel():
    if not current_user.is_admin:
        flash("Access denied", "error")
        return redirect(url_for('main.home'))
    users = User.query.all()
    accounts = BankAccount.query.all()
    return render_template('admin_panel.html', users=users, logs=[])

# -------------------------------
# API: Balance
# -------------------------------
@auth.route('/api/balance')
@login_required
def api_balance():
    account = BankAccount.query.filter_by(user_id=current_user.id).first()
    if not account:
        return jsonify({"error": "Account not found"}), 404
    return jsonify({
        "account_number": account.account_no,
        "balance": account.balance,
        "email": current_user.email
    })