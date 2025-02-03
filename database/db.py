import sqlite3
from models.models import init_db

DB_PATH = "data/bot.db"


def get_db_connection():
    """Establishes a database connection and returns the cursor & connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Allows fetching results as dictionaries
    return conn


def init_database():
    """Initializes the database with required tables."""
    conn = get_db_connection()
    init_db(conn)  # Calls the function from `models.py`
    conn.close()
