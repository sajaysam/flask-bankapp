# db_test.py
import os
import psycopg2
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read the database URL
db_url = os.getenv("DATABASE_URL")

try:
    conn = psycopg2.connect(db_url)
    print("✅ Connected successfully to:", db_url)
    conn.close()
except Exception as e:
    print("❌ Failed to connect:")
    print(e)