import mysql.connector

class Conexion:
    def iniciar_conexion():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="empresa"

        )
        return mydb
    
    iniciar_conexion()
