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


def get_ico_len(table_name = 'ico_numbers', database_name = 'finstat', schema = 'dbo'):
    query = f"Select COUNT(*) AS COUNT from {database_name}.{schema}.{table_name}"
    count_companies = pd.read_sql(query, connect_database(database_name))
    return count_companies['COUNT'][0]
    

def get_ico_table(table_name = 'ico_numbers', database_name = 'finstat', schema = 'dbo', size = 1000000):
    query = f"Select top({size}) * from {database_name}.{schema}.{table_name}"
    table = pd.read_sql(query, connect_database(database_name))
    return table
    
    
    
