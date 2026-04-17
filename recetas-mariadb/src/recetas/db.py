import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc123.",   # pon tu contraseña si tienes
        database="recetas_db"
    )


