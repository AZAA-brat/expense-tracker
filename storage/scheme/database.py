from storage.scheme.connection import get_connection

def init_db():
    cnn = get_connection()
    cnn.executescript(
    """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER NOT NULL COLLATE NOCASE UNIQUE,
        username TEXT,
        created_at TEXT NOT NULL DEFAULT (datetime('now'))
    );
        
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL UNIQUE,
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
