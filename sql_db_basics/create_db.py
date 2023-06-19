import mysql.connector
conn  = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)

cursor = conn.cursor()
# Create DB
cursor.execute('CREATE DATABASE IF NOT EXISTS Test_DB')

for i in cursor:
    print(i)