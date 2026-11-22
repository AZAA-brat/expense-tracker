from storage.scheme.connection import get_connection

def delete_category(category_id):
    cnn = get_connection()
    try:
        cursor = cnn.execute(
            """
            DELETE FROM categories 
            WHERE id = ?
            """,
            (category_id,),
        )
        cnn.commit()
        return cursor.rowcount > 0
    finally:
        cnn.close()