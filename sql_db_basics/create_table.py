import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)

cursor = conn.cursor()

cursor.execute('CREATE TABLE Test_DB.Users ( UID int , USER_NAME VARCHAR(50) ) ')