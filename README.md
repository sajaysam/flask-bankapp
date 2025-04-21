# 🏦 FINOVA Flask Banking App

This is a full-featured Flask web application simulating an online banking system. Users can register, log in, open accounts, transfer money, view transaction history, and get real-time cryptocurrency rates via API. The backend is powered by Flask and PostgreSQL (via AWS RDS), with full test coverage and cloud deployment support.

---

## 🔧 Features

- 🔐 User Authentication (Sign Up, Log In, Log Out)
- 🏦 Open Account with Unique Account Number
- 💸 Secure Money Transfers with Validation
- 📊 Transaction History for Each User
- 🌐 Crypto Ticker via WorldCoinIndex API
- 🧾 Balance API (JSON) for integrations
- ☁️ AWS RDS PostgreSQL Integration
- 📈 Unit Testing for all major modules
- 🚀 Deployed on [Render.com](https://render.com)

---

## 📁 Project Structure

```
flask-bankapp/
├── app/
│   ├── __init__.py         # App factory setup
│   ├── auth.py             # Auth routes
│   ├── routes.py           # Public routes, admin, API
│   ├── models.py           # User, BankAccount, Transaction models
│   ├── forms.py            # Flask-WTF form classes
│   ├── extensions.py       # DB, LoginManager, Migrate setup
│   └── templates/          # HTML templates
│       └── *.html
├── tests/                  # Pytest test scripts
├── run.py                  # App launcher
├── requirements.txt        # Dependencies
├── .env                    # Env vars (not committed)
├── .gitignore
├── README.md               # You are here 📄
```

---

## 🚀 Deployment (Render + AWS RDS)

### 1. Deploy PostgreSQL on AWS RDS
- Create PostgreSQL instance
- Set public access + security group
- Save the connection string as `DATABASE_URL` in `.env`

### 2. Push to GitHub & Deploy to Render
- Connect your GitHub repo to [Render](https://render.com)
- Use `gunicorn run:app` as start command
- Add `.env` variables:
  - `DATABASE_URL`
  - `SECRET_KEY`
  - `WCI_API_KEY`

---

## 🔑 Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret
DATABASE_URL=postgresql://user:pass@host/dbname
WCI_API_KEY=your_worldcoinindex_key
```

---

## ✅ Running Locally

```bash
git clone https://github.com/your-username/flask-bankapp.git
cd flask-bankapp
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
flask run
```

---

## 🧪 Running Tests

```bash
pytest -v
```

Or with coverage:

```bash
pytest --cov=app --cov-report=html
```

---

## 📡 API Endpoints

- `GET /api/balance` – Returns logged-in user's balance and account info

---

## 📌 Screenshots

![Dashboard](screenshots/dashboard.png)
![Transfer](screenshots/transfer.png)

---

## ✨ Credits

Built with Flask, PostgreSQL, WTForms, SQLAlchemy, and WorldCoinIndex API.  
Deployed via Render.com and AWS RDS.

---

Created by :
SAJAY OOMMEN - M01038036 - Masters Fintech, Middlesex University - 2024-25
FATOUMATA ZARA IBRAHIM - M01033558 - Masters Fintech, Middlesex Univesity - 2024-25
ESMAZILDA (ISABEL) LUEMBA - M01040555 - Masters Fintech, Middlesex University - 2024-25
TANZEEM A - M01033376 - Masters Fintech, Middlesex University - 2024-25

## 📜 License

MIT License
