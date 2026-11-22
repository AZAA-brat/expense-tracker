from storage.scheme.connection import get_connection

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
