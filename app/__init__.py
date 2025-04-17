import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_login import LoginManager
from .extensions import db, migrate, login_manager

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'devkey')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql:///bankapp.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
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

    # Import models for migrations
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app