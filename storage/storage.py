import sqlite3
from config import DB_PATH
from datetime import datetime

def init_db():
    cnn = sqlite3.connect(DB_PATH)
    cnn.execute("PRAGMA foreign_keys = ON;")
    cnn.executescript(
    """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER NOT NULL UNIQUE,
        username TEXT,
        created_at TEXT NOT NULL DEFAULT (datetime('now'))
    );
        
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT (datetime('now'))
    );
    
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL, 
        expense REAL NOT NULL CHECK (expense > 0),
        usd_amount REAL NOT NULL CHECK (usd_amount > 0),
        rate REAL NOT NULL CHECK (rate > 0),
        name TEXT NOT NULL, 
        created_at TEXT NOT NULL DEFAULT (datetime('now')),
        FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
    );
    """
    )
    cnn.commit()
    cnn.close()
