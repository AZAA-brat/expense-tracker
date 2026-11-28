from storage.scheme.connection import get_connection

def add_expense(category_id, expense, rate, name):
    if rate > 0:
        usd = expense / rate
        usd_amount = round(usd, 6)
    else:
        raise ValueError ("rate is invalid")
    cnn = get_connection()
    try:
        cursor = cnn.execute(
            """
            INSERT INTO expenses(category_id, expense, usd_amount, rate, name)
            VALUES (?,?,?,?,?)
            """,
            (category_id, expense, usd_amount, rate, name),
        )
        cnn.commit()
        return cursor.lastrowid
    finally:
        cnn.close()
