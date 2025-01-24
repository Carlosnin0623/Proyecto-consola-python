import mysql.connector
from mysql.connector import Error

try:
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="master_python",
        port=3306
    )
    
    if database.is_connected():
        print("Conexión exitosa a la base de datos")
        cursor = database.cursor(buffered=True)
except Error as e:
    print(f"Error al conectar a la base de datos: {e}")
    database = None
    cursor = None