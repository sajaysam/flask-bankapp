# ----------------------------------------------------
# Main Blueprint - Handles UI Routes and General Pages
# ----------------------------------------------------
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from .models import BankAccount, Transaction
import os
import requests

main = Blueprint('main', __name__)

# -------------------------------------------
# Fetch Crypto Prices from WorldCoinIndex
# -------------------------------------------
def get_crypto_prices():
    try:
        api_key = os.getenv('WCI_API_KEY')
        url = f"https://www.worldcoinindex.com/apiservice/json?key={api_key}&fiat=USD&label=btcusd-ethusd"
        res = requests.get(url)
        data = res.json().get("Markets", [])
        return [(item["Label"], item["Price"]) for item in data]
    except:
        return [("BTC/USD", 30500), ("ETH/USD", 1900)]

# -------------------------------------------
# Home Page
# -------------------------------------------
@main.route('/')
def home():
    cryptos = get_crypto_prices()
    return render_template('home.html', cryptos=cryptos)

# -------------------------------------------
# Dashboard
# -------------------------------------------
@main.route('/dashboard')
@login_required
def dashboard():
    account = BankAccount.query.filter_by(user_id=current_user.id).first()
    if not account:
        return redirect(url_for('auth.open_account'))
    return render_template('dashboard.html', account=account)

# -------------------------------------------
# Admin Panel
# -------------------------------------------
@main.route('/admin')
@login_required
def admin_panel():
    if not current_user.is_admin:
        flash("Access denied", "error")
        return redirect(url_for('main.home'))
    users = BankAccount.query.all()
    return render_template('admin_panel.html', users=users)

# -------------------------------------------
# API: Get Balance
# -------------------------------------------
@main.route('/api/balance')
@login_required
def api_balance():
    account = BankAccount.query.filter_by(user_id=current_user.id).first()
    if not account:
        return jsonify({"error": "Account not found"}), 404

    return jsonify({
        "account_number": account.account_no,
        "balance": float(account.balance),
        "email": current_user.email
    })