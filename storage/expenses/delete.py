from storage.scheme.connection import get_connection

def delete_expense(expense_id):
    cnn = get_connection()
    try:
        cursor = cnn.execute(
            """
            DELETE FROM expenses 
            WHERE id = ?
            """,
            (expense_id,),
        )
        cnn.commit()
        return cursor.rowcount > 0
    finally:
        cnn.close()