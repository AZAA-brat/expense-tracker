from storage.scheme.connection import get_connection

def count_category_expenses(category_id):
    cnn = get_connection()
    try:
        cursor = cnn.execute(
            """
            SELECT COUNT(*) FROM expenses
            WHERE category_id = ?
            """,
            (category_id,),
        )
        return cursor.fetchone()
    finally:
        cnn.close()