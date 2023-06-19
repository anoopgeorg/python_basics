import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM Test_DB.Users ")
for i in cursor.fetchall():
    print(i)
conn.close()