import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc123.",   # pon tu contraseña si tienes
        database="recetas_db"
    )

    print("✅ Conexión correcta a MariaDB")

    cursor = conexion.cursor()
    cursor.execute("SELECT DATABASE();")

    for db in cursor:
        print("Base de datos:", db)

    conexion.close()

except Exception as e:
    print("❌ Error:", e)