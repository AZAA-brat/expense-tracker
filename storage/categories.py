from storage.connection import get_connection
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

def get_category(category_id):
    cnn = get_connection()
    try:
        cursor = cnn.execute(
            """
            SELECT * FROM categories
            WHERE id = ?
            """,
            (category_id,),
        )
        return cursor.fetchone()
    finally:
        cnn.close()

def count_category_expenses(category_id):
    cnn = get_connection()
    try:
        cursor = cnn.execute(
            """
            SELECT COUNT(*) FROM expenses
            WHERE category_id = ?
            """,
            (category_id,),
        )
        return cursor.fetchone()
    finally:
        cnn.close()

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