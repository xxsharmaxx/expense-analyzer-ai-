import mysql.connector
import pandas as pd

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="expense_db"
    )

def fetch_expenses():
    conn = get_connection()
    query = """
    SELECT c.category_name, e.amount, e.date
    FROM expense e
    JOIN category c ON e.category_id = c.category_id
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df
