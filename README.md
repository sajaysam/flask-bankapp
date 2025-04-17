# 💰 Flask Bank App

A secure, full-featured banking web application built with **Flask**, styled with **Tailwind CSS**, and powered by a **PostgreSQL** database on **AWS RDS**.

---

## 🚀 Features

- 🔐 User Authentication (Signup, Login, Logout)
- 💼 Open a Bank Account
- 💸 Transfer Funds Between Accounts
- 📄 View Transaction History
- 📊 API: Account Balance in JSON
- 👨‍💼 Admin Panel for Managing Users
- 🌐 WorldCoinIndex API Ticker Integration
- ☁️ AWS RDS PostgreSQL Integration
- 🧪 Unit Testing for Core Features

---

## 🛠 Tech Stack

- **Backend**: Flask, SQLAlchemy
- **Frontend**: Jinja2 + Tailwind CSS
- **Database**: PostgreSQL (hosted on AWS RDS)
- **Auth**: Flask-Login
- **APIs**: WorldCoinIndex
- **Testing**: unittest
- **Deployment**: GitHub + Docker

---

## 📦 Installation (Local)

1. **Clone the repository**
   ```bash
   git clone https://github.com/sajaysam/flask-bankapp.git
   cd flask-bankapp

---------------------------------------------------------

1. **Clone the repository**
   ```bash
   git clone https://github.com/sajaysam/flask-bankapp.git
   cd flask-bankapp
-----------------------------------------------------------
2. **Create virtual environment**
bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
---------------------------------------------------------------
3. **Install requirements**
bash
pip install -r requirements.txt
---------------------------------------------------------------
4. **Create .env file**
env
SECRET_KEY=your-secret-key
DATABASE_URL=your-postgres-connection-url
WCI_API_KEY=your-worldcoinindex-key
---------------------------------------------------------------
5. **Run the app**
bash
python run.py
---------------------------------------------------------------
6. **🧪 Running Tests**
bash
python -m unittest discover tests
---------------------------------------------------------------
