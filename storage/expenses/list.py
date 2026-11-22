from storage.scheme.connection import get_connection

def list_expenses(start, end):
    query = """
    SELECT
        e.id AS e_id,
        e.expense AS e_expense,
        e.usd_amount AS e_usd_amount,
        e.name AS e_name,
        e.created_at AS e_created_at,
        c.category AS c_category
    FROM expenses AS e
    LEFT JOIN categories AS c
        ON e.category_id = c.id
    WHERE e.created_at >= ?
      AND e.created_at < ?
    ORDER BY e.created_at
    """
    cnn = get_connection()
    try:
        cursor = cnn.execute(query, (start, end))
        return cursor.fetchall()
    finally:
        cnn.close()


