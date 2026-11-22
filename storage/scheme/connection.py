from config import DB_PATH
import sqlite3

def get_connection():
    cnn = sqlite3.connect(DB_PATH)
    cnn.execute("PRAGMA foreign_keys = ON;")
    cnn.row_factory = sqlite3.Row
    return cnn