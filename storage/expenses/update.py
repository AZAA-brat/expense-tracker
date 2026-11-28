from storage.scheme.connection import get_connection

def update_expense(new_expense, expense_id):
    if new_expense <= 0:
        raise ValueError ("new expense must be greater than zero")
    cnn = get_connection()
    try:
        cursor = cnn.cursor()
        cursor.execute(
            """
            SELECT rate FROM expenses
            WHERE id = ?
            """,
            (expense_id,),
        )
        row = cursor.fetchone()
        if row is None:
            return False
        rate = row[0]
        usd_amount = round(new_expense / rate, 6)
        cursor.execute(
            """
            UPDATE expenses
            SET expense = ?, usd_amount = ?
            WHERE id = ?
            """,
            (new_expense, usd_amount, expense_id),
        )
        cnn.commit()
        return cursor.rowcount > 0
    finally:
        cnn.close()