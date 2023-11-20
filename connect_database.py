import pyodbc
conn = pyodbc.connect(
"Driver={SQL Server};"
"Server=DESKTOP-SGHRP03\SQLEXPRESS;"
"Database =Stonks;"
"Trusted_Connection=yes;")
