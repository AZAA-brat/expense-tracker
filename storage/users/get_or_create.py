from storage.scheme.connection import get_connection

def get_or_create_user(telegram_id, username):
    cnn = get_connection()
    try:
        cnn.execute(
        """
        INSERT OR IGNORE INTO users(telegram_id, username) 
        VALUES (?, ?, ?)
        """,
            (telegram_id, username),
        )
        cnn.commit()
    finally:
        cnn.close()