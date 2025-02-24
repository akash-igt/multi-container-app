import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="user_db"
    )
    return conn
