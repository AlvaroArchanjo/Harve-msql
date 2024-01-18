import mysql.connector

conn = mysql.connector.connect(
    user='root',
    password='jr',
    host='127.0.0.1',
    database='meu_banco',
    port='3307'
)

if conn.is_connected():
    print('CONECTAMOS!!!') 