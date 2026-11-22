from storage.scheme.connection import get_connection

def total_expense(start, end):
    cnn = get_connection()
    try:
        rows = cnn.execute(
            """
            SELECT
                categories.category AS category,
                SUM(expenses.expense) AS total,
                ROUND(SUM(expenses.usd_amount), 2) AS total_usd
            FROM expenses
            JOIN categories
                ON expenses.category_id = categories.id
            WHERE expenses.created_at >= ? AND expenses.created_at < ?
            GROUP BY categories.id, categories.category
            ORDER BY total DESC
            """,
            (start, end),
        ).fetchall()
    finally:
        cnn.close()
    return rows