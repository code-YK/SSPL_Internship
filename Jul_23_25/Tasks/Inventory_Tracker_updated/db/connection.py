import sqlite3
import os

DB_PATH = os.path.join("data", "inventory.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
