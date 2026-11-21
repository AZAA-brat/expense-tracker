from storage.connection import get_connection

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

def get_user(telegram_id):
    cnn = get_connection()
    try:
        cursor = cnn.execute(
            """
            SELECT * 
            FROM users 
            WHERE telegram_id = ?
            """,
            (telegram_id,),
        )
        return cursor.fetchone()
    finally:
        cnn.close()


def update_username(telegram_id, username):
    cnn = get_connection()
    try:
        cnn.execute(
            """
            UPDATE users 
            SET username = ?
            WHERE telegram_id = ?
            """,
            (username, telegram_id),
        )
        cnn.commit()
    finally:
        cnn.close()