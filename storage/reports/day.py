from storage.scheme.connection import get_connection

def totals_by_day(start, end):
    cnn = get_connection()
    try:
        rows = cnn.execute(
            """
            SELECT
                date(created_at, '+5 hours') AS day,
                SUM(expense) AS total_expense,
                ROUND(SUM(usd_amount), 2) AS total_usd
            FROM expenses
            WHERE created_at >= ? AND created_at < ?
            GROUP BY date(created_at, '+5 hours')
            ORDER BY day
            """,
            (start, end),
        ).fetchall()
    finally:
        cnn.close()
    return rows