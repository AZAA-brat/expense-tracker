from storage.scheme.connection import get_connection

def get_or_create_user(telegram_id, username):
    cnn = get_connection()

    try:
        cnn.execute(
            """
            INSERT OR IGNORE INTO users (telegram_id, username)
            VALUES (?, ?)
            """,
            (telegram_id, username),
        )
        cnn.commit()

        cursor = cnn.execute(
            """
            SELECT telegram_id, username
            FROM users
            WHERE telegram_id = ?
            """,
            (telegram_id,),
        )
        row = cursor.fetchone()

        if row is None:
            raise RuntimeError(f"User with telegram_id={telegram_id} was not created")

        return {
            "telegram_id": row[0],
            "username": row[1],
        }
    finally:
        cnn.close()