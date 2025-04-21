# 💳 FINOVA BANK – Flask-Based Banking App

FINOVA BANK is a full-featured web-based banking application built with Python, Flask, and PostgreSQL. It provides secure user authentication, transaction handling, balance management, an admin panel, and real-time cryptocurrency integration.

---

## 🚀 Features

### 👤 User
- Secure sign-up & login (with password hashing)
- Create a bank account with initial ₹10,000 balance
- Dashboard showing account details & balance
- Transfer money to another account
- View transaction history

### ⚙️ Admin
- Access to all user accounts
- View balances and logs

### 🌐 API
- `/api/balance`: JSON response with account balance

### 💱 Crypto Integration
- Real-time crypto prices displayed on the homepage using CoinGecko

---

## 🛠️ Tech Stack

| Layer        | Technology                     |
|-------------|----------------------------------|
| Backend      | Flask (Blueprints, Jinja2)      |
| Frontend     | Tailwind CSS                    |
| Database     | PostgreSQL (via AWS RDS)        |
| ORM          | SQLAlchemy                      |
| Forms        | Flask-WTF, WTForms              |
| Testing      | pytest, Flask-Testing           |
| DevOps       | Docker, Git, GitHub             |

----------------------------------------------------------

## ⚙️ Getting Started

### 🔧 Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/flask-bankapp.git
cd flask-bankapp
------------------------------------------------------------
📦 Set up virtual environment
in bash
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
------------------------------------------------------------
🧪 Set up environment variables (.env)
env
SECRET_KEY=your-secret
DATABASE_URL=your-postgres-url
WCI_API_KEY=your-worldcoinindex-or-coingecko-key
------------------------------------------------------------
🧪 Running the App
📌 Run Flask
bash
flask run
Visit: http://127.0.0.1:5000
------------------------------------------------------------
🧪 Testing
✅ Run Unit Tests
bash
pytest
------------------------------------------------------------
🧾 Generate HTML Coverage Report
bash
pytest --cov=app --cov-report=html
open htmlcov/index.html  # or use your system's file opener
------------------------------------------------------------

📂 Project Structure
bash
Copy
Edit
flask-bankapp/
├── app/               # Core application
├── tests/             # Unit tests
├── migrations/        # Flask-Migrate scripts
├── static/            # Images, styles, JS
├── templates/         # Jinja2 HTML templates
├── run.py             # Entry point
├── .env               # Environment variables
└── requirements.txt   # Dependencies

--------------------------------------------------------------
📈 Future potential enhancements 
1. SMS alerts for account activity (via Twilio or 2Factor)
2. Two-factor authentication
3. PDF bank statements
4. Graphs for transaction summaries
--------------------------------------------------------------
🧠 Authors
1. Sajay Oommen - M01038036 , Middlesex Uni, Dubai - CST4160 - 2024-25
2. Fatoumata - M01038036 , Middlesex Uni, Dubai - CST4160 - 2024-25
3. Isabel Britto - M01038036 , Middlesex Uni, Dubai - CST4160 - 2024-25
4. Tanzeem - M01038036 , Middlesex Uni, Dubai - CST4160 - 2024-25

📜 License
This project is licensed under the MIT License.