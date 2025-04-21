from setuptools import setup, find_packages

setup(
    name='flask_bankapp',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-Migrate',
        'Flask-WTF',
        'Flask-Login',
        'python-dotenv',
        'email-validator',
        'requests',
        'gunicorn'
    ],
)
