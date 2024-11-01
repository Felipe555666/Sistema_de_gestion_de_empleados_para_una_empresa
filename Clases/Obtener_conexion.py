import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    #Establece una conexión con la base de datos utilizando las credenciales del usuario ''.
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",                # Usuario MySQL 
            password="",         # Contraseña del usuario 
            database="sistema_gestion_de_empleados"
        )
        if conexion.is_connected():
                print("Conexión exitosa a la base de datos.")
        return conexion
    except ValueError as error:
        print(f"Error al conectar con la base de datos: {error}")
        return None

def cerrar_conexion(conexion):
    #Cierra la conexión con la base de datos de manera segura.
    try:
        if conexion.is_connected():
            conexion.close()
            print("Conexión cerrada correctamente.")
    except ValueError as error:
        print(f"Error al cerrar la conexión: {error}")

def ejecutar_consulta(query):
    conexion = obtener_conexion()
    if conexion is None:
        return None
    try:
        cursor = conexion.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados
    except Error as error:
        print(f"Error al ejecutar la consulta: {error}")
        return None
    finally:
        cerrar_conexion(conexion)

query = "SELECT * FROM empleado"
resultados = ejecutar_consulta(query)
for fila in resultados:
    print(fila)
