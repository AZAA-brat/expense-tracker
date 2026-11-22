from storage.scheme.connection import get_connection

def total_by_period(start, end):
    cnn = get_connection()
    try:
        row = cnn.execute(
            """
            SELECT COALESCE(SUM(expense), 0) AS total_expense,
                   COALESCE(ROUND(SUM(usd_amount), 2), 0) AS total_usd
            FROM expenses
            WHERE created_at >= ? AND created_at < ?
            """,
            (start, end),
        ).fetchone()
    finally:
        cnn.close()
    return row
