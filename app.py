from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from yourapp.auth import auth
from yourapp.routes import main  # Adjust 'yourapp' to your folder name
from yourapp.extensions import db, login_manager  # Reuse your extension setup
from config import Config  # Optional if you have config.py

def create_app():
    app = Flask(__name__)
    
    # Load Config (Edit this as needed)
    app.config.from_object(Config)

    # Initialize Extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register Blueprints
    app.register_blueprint(main)

    return app

# Running the app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)