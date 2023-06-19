import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)

cursor = conn.cursor()
cursor.execute("INSERT INTO Test_DB.Users VALUES (1,'Anoop')")
conn.commit()
conn.close()