from storage.scheme.connection import get_connection
import sqlite3

def add_category(category):
    cnn = get_connection()
    try:
        cursor = cnn.execute(
            """
            INSERT INTO categories(category)
            VALUES (?)
            """,
            (category,),
        )
        cnn.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        return None
    finally:
        cnn.close()
