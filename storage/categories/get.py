from storage.scheme.connection import get_connection

def get_category(category_id):
    cnn = get_connection()
    try:
        cursor = cnn.execute(
            """
            SELECT * FROM categories
            WHERE id = ?
            """,
            (category_id,),
        )
        return cursor.fetchone()
    finally:
        cnn.close()
