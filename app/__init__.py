# app/__init__.py

import os
from flask import Flask
from dotenv import load_dotenv

from .extensions import db, migrate, login_manager

def create_app():
    # Load environment variables from .env
    load_dotenv()

    # Initialize the Flask app
    app = Flask(__name__)

    # ---------------------------
    # Configuration
    # ---------------------------
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'devkey')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///bankapp.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ---------------------------
    # Initialize Extensions
    # ---------------------------
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # ---------------------------
    # Register Blueprints
    # ---------------------------
    from .routes import main as main_blueprint
    from .auth import auth as auth_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    # ---------------------------
    # User Loader for Flask-Login
    # ---------------------------
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app