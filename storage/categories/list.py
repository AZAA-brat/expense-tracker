from storage.scheme.connection import get_connection

def list_categories():
    cnn = get_connection()
    try:
        cursor = cnn.execute(
            """
            SELECT * 
            FROM categories
            """
        )
        return cursor.fetchall()
    finally:
        cnn.close()
