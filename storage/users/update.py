from storage.scheme.connection import get_connection

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