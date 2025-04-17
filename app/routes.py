from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from .models import BankAccount, Transaction
from .forms import TransferForm
import random
import requests
import os

main = Blueprint('main', __name__)

def get_crypto_prices():
    try:
        api_key = os.getenv('WCI_API_KEY')
        url = f"https://www.worldcoinindex.com/apiservice/json?key={api_key}&fiat=USD&label=btcusd-ethusd"
        res = requests.get(url)
        data = res.json().get("Markets", [])
        return [(item["Label"], item["Price"]) for item in data]
    except:
        return [("BTC/USD", 30500), ("ETH/USD", 1900)]  # fallback

@main.route('/')
def home():
    cryptos = get_crypto_prices()
    return render_template('home.html', cryptos=cryptos)

@main.route('/dashboard')
@login_required
def dashboard():
    account = BankAccount.query.filter_by(user_id=current_user.get_id()).first()
    if not account:
        return redirect(url_for('main.open_account'))
    return render_template('dashboard.html', account=account)

@main.route('/transfer', methods=['GET', 'POST'])
@login_required
def transfer():
    account = BankAccount.query.filter_by(user_id=current_user.get_id()).first()
    form = TransferForm()
    if form.validate_on_submit():
        receiver = BankAccount.query.filter_by(account_no=form.to_account.data).first()
        if not receiver:
            flash("Receiver not found", 'error')
        elif account.account_no == form.to_account.data:
            flash("Cannot transfer to your own account", 'error')
        elif account.balance < form.amount.data:
            flash("Insufficient funds", 'error')
        else:
            account.balance -= float(form.amount.data)
            receiver.balance += float(form.amount.data)
            new_tx = Transaction(
                sender_id=account.id,
                receiver_id=receiver.id,
                amount=float(form.amount.data)
            )
            from .extensions import db
            db.session.add(new_tx)
            db.session.commit()
            flash("Transfer successful!", 'success')
            return redirect(url_for('main.dashboard'))
    return render_template('transfer.html', form=form, balance=account.balance)

@main.route('/transactions')
@login_required
def transactions():
    user_id = current_user.get_id()
    account = BankAccount.query.filter_by(user_id=user_id).first()
    history = Transaction.query.filter(
        (Transaction.sender_id == account.id) | (Transaction.receiver_id == account.id)
    ).order_by(Transaction.timestamp.desc()).all()
    return render_template('transactions.html', history=history, user_id=user_id)

#@main.route('/open_account', methods=['GET', 'POST'])
#@login_required
#def open_account():
 #   user_id = current_user.get_id()
  #  existing = BankAccount.query.filter_by(user_id=user_id).first()
   # if existing:
    #    flash("You already have an account.", "info")
     #   return redirect(url_for('main.dashboard'))

    #if request.method == 'POST':
     #   account_no = str(random.randint(10**11, 10**12 - 1))
      #  new_account = BankAccount(user_id=user_id, account_no=account_no, balance=0.0)
       # from .extensions import db
        #db.session.add(new_account)
        #db.session.commit()
        #flash("Account created successfully!", "success")
        #return redirect(url_for('main.dashboard'))
#
 #   return render_template('open_account.html')

@main.route('/admin')
@login_required
def admin_panel():
    if not current_user.is_admin:
        flash("Access denied", "error")
        return redirect(url_for('main.home'))

    users = BankAccount.query.all()
    return render_template('admin_panel.html', users=users)

@main.route('/api/balance')
@login_required
def api_balance():
    account = BankAccount.query.filter_by(user_id=current_user.get_id()).first()
    if not account:
        return jsonify({"error": "Account not found"}), 404

    return jsonify({
        "account_number": account.account_no,
        "balance": float(account.balance),
        "email": current_user.email
    })
