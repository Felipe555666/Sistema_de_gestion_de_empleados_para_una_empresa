import mysql.connector
from mysql.connector import Error

class Conexion:
    @staticmethod
    def iniciar_conexion():
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Sistema_Gestion_De_Empleados"
            )
            print("Conexión establecida exitosamente")
            return mydb
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
