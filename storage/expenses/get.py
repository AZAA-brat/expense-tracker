from storage.scheme.connection import get_connection

def get_expense(expense_id):
    cnn = get_connection()
    try:
        cursor = cnn.execute(
            """
            SELECT * FROM expenses
            WHERE id = ?
            """,
            (expense_id,),
        )
        return cursor.fetchone()
    finally:
        cnn.close()

