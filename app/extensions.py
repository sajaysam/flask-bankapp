# --------------------------------------------
#  Flask Extensions for Modular Integration
# --------------------------------------------

# SQLAlchemy is the ORM (Object Relational Mapper)
# It allows interaction with the database using Python classes and objects
from flask_sqlalchemy import SQLAlchemy

# Flask-Migrate handles database migrations (schema changes) using Alembic
# It integrates with Flask CLI commands like `flask db migrate` and `flask db upgrade`
from flask_migrate import Migrate

# Flask-Login manages user sessions
# It handles login/logout functionality, current_user, and session persistence
from flask_login import LoginManager

# Initialize each extension without attaching to the app yet
# They will be bound to the Flask app in `create_app()` using `.init_app(app)`
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()