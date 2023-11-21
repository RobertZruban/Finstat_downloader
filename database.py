import pyodbc
import pandas as pd

def connect_database(database_name):
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-SGHRP03\SQLEXPRESS;"
        f"Database={database_name};"
        "Trusted_Connection=yes;")
    return conn


def query_table(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()  # Commit the changes if it's an INSERT, UPDATE, or DELETE operation
    result = cursor.fetchall()  # Use fetchall() if the query returns results
    cursor.close()
    return result
