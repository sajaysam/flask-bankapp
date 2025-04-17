import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

from flask import Flask
from flask_login import LoginManager
from .extensions import db, migrate, login_manager

def create_app():

    # Creating a Flask app instance
    app = Flask(__name__)
    #----------------------------------
    # Load configuration
    #----------------------------------
    # Secret key for session management and CSRF protection
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'devkey')
    # Database URL (PostgreSQL from .env, or fallback to local SQLite)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql:///bankapp.db')
    # Turns off modification tracking (saves memory)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #---------------------------
    # Initialize extensions
    #---------------------------
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Set login view (optional but recommended)
    login_manager.login_view = 'auth.login'

    # Import and register blueprints
    from .routes import main
    from .auth import auth  # or auth_bp depending on what your auth.py defines

    app.register_blueprint(main)
    app.register_blueprint(auth)

    #--------------------------
    # Import models for migrations
    #---------------------------
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app