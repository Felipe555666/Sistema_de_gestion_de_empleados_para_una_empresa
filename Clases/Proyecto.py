import mysql.connector
from conexion import Conexion
from datetime import datetime
from mysql.connector import Error


mydb = Conexion.iniciar_conexion()


class proyecto:
    def __init__(self, Id_proyecto=None, Nombre=None, Descripcion=None, Fecha_inicio=None, Fecha_fin=None):
        self._Id_proyecto = Id_proyecto
        self._Nombre = Nombre
        self._Descripcion = Descripcion
        self._Fecha_inicio = Fecha_inicio
        self._Fecha_fin = Fecha_fin

    def validar_proyecto(self):
        """Valida todos los datos del proyecto"""
        try:
            if not isinstance(self._Id_proyecto, int) or self._Id_proyecto <= 0:
                return False, "El ID del proyecto debe ser un número entero positivo"
            if not isinstance(self._Nombre, str) or not self._Nombre.strip():
                return False, "El nombre del proyecto no puede estar vacío"
            if not isinstance(self._Descripcion, str) or not self._Descripcion.strip():
                return False, "La descripción del proyecto no puede estar vacía"
            validacion_fechas, mensaje = self.validar_fechas()
            if not validacion_fechas:
                return False, mensaje
            return True, "Datos del proyecto válidos"
        except Exception as e:
            return False, f"Error en la validación del proyecto: {str(e)}"
    
    def validar_fechas(self):
        """Valida las fechas del proyecto"""
        formato_fecha = "%Y-%m-%d"
        try:
            fecha_inicio = datetime.strptime(self._Fecha_inicio, formato_fecha)
            fecha_fin = datetime.strptime(self._Fecha_fin, formato_fecha)
            fecha_actual = datetime.now()

            if fecha_inicio > fecha_fin:
                return False, "La fecha de inicio no puede ser posterior a la fecha de fin"
            if fecha_inicio > fecha_actual or fecha_fin > fecha_actual:
                return False, "Las fechas no pueden estar en el futuro"
            return True, "Las fechas son válidas"
        except ValueError:
            return False, "Las fechas deben estar en formato YYYY-MM-DD"
        except Exception as e:
            return False, f"Error en la validación de fechas: {str(e)}"

    def obtener_informacion_proyecto(self):
        return {
            'ID': self._Id_proyecto,
            'Nombre': self._Nombre,
            'Descripción': self._Descripcion,
            'Fecha Inicio': self._Fecha_inicio,
            'Fecha Fin': self._Fecha_fin
        }

    def actualizar_proyecto(self, nombre=None, descripcion=None, fecha_inicio=None, fecha_fin=None):
        """Actualiza la información del proyecto en memoria"""
        try:
            if nombre:
                self._Nombre = nombre
            if descripcion:
                self._Descripcion = descripcion
            if fecha_inicio:
                self._Fecha_inicio = fecha_inicio
            if fecha_fin:
                self._Fecha_fin = fecha_fin
            validacion, mensaje = self.validar_proyecto()
            if not validacion:
                return False, mensaje
            return True, "Proyecto actualizado correctamente"
        except Exception as e:
            return False, f"Error al actualizar el proyecto: {str(e)}"
    
    def __str__(self):
        return f"Proyecto: {self._Nombre} (ID: {self._Id_proyecto})"
    
    
    # Métodos para la base de datos
    @classmethod
    def crear_proyecto_bd(cls, conexion, proyecto):
        try:
            with conexion.cursor() as cursor:
                sql = """INSERT INTO proyecto (id_proyecto, nombre, descripcion, 
                        fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s, %s)"""
                valores = (proyecto._Id_proyecto, proyecto._Nombre, 
                           proyecto._Descripcion, proyecto._Fecha_inicio, 
                           proyecto._Fecha_fin)
                cursor.execute(sql, valores)
                conexion.commit()
                return True, "Proyecto creado exitosamente"
        except Error as e:
            return False, f"Error al crear el proyecto en la BD: {str(e)}"

    @classmethod
    def obtener_proyecto_bd(cls, conexion, id_proyecto):
        try:
            with conexion.cursor(dictionary=True) as cursor:
                sql = "SELECT * FROM proyecto WHERE id_proyecto = %s"
                cursor.execute(sql, (id_proyecto,))
                resultado = cursor.fetchone()
                if resultado:
                    return True, resultado
                return False, "Proyecto no encontrado"
        except Error as e:
            return False, f"Error al obtener el proyecto de la BD: {str(e)}"

    def actualizar_proyecto_bd(self, conexion):
        """Actualiza un proyecto existente en la base de datos"""
        try:
            with conexion.cursor() as cursor:
                sql = """UPDATE proyecto SET nombre = %s, descripcion = %s, 
                        fecha_inicio = %s, fecha_fin = %s WHERE id_proyecto = %s"""
                valores = (self._Nombre, self._Descripcion, self._Fecha_inicio,
                           self._Fecha_fin, self._Id_proyecto)
                cursor.execute(sql, valores)
                conexion.commit()
                if cursor.rowcount > 0:
                    return True, "Proyecto actualizado exitosamente"
                return False, "No se encontró el proyecto para actualizar"
        except Error as e:
            return False, f"Error al actualizar el proyecto en la BD: {str(e)}"

    @classmethod
    def eliminar_proyecto_bd(cls, conexion, id_proyecto):
        try:
            with conexion.cursor() as cursor:
                sql = "DELETE FROM proyecto WHERE id_proyecto = %s"
                cursor.execute(sql, (id_proyecto,))
                conexion.commit()
                if cursor.rowcount > 0:
                    return True, "Proyecto eliminado exitosamente"
                return False, "No se encontró el proyecto para eliminar"
        except Error as e:
            return False, f"Error al eliminar el proyecto de la BD: {str(e)}"


    def crear_proyecto_bd(self, mydb):
        try:
            print("\n--- Crear Nuevo Proyecto ---")
            nombre = input("Nombre del proyecto: ")
            descripcion = input("Descripción: ")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
            
            self._Nombre = nombre
            self._Descripcion = descripcion
            self._Fecha_inicio = fecha_inicio
            self._Fecha_fin = fecha_fin
            
            if self.validar_fechas()[0]:
                cursor = mydb.cursor()
                sql = """INSERT INTO proyecto (nombre, descripcion, 
                        fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s)"""
                valores = (self._Nombre, self._Descripcion, 
                        self._Fecha_inicio, self._Fecha_fin)
                cursor.execute(sql, valores)
                mydb.commit()
                print("Proyecto creado exitosamente")
                return True, "Proyecto creado exitosamente"
            else:
                print("Error al crear proyecto. Verifique las fechas ingresadas.")
                return False, "Error en las fechas ingresadas"
        except Error as e:
            print(f"Error al crear el proyecto en la BD: {e}")
            return False, str(e)

    def ver_proyecto(self, mydb):
        try:
            id_proy_input = input("Ingrese el ID del proyecto: ")
            if not id_proy_input.isdigit():
                print("Por favor, ingrese un ID válido (número entero).")
                return
            
            id_proy = int(id_proy_input)

            # Usar el parámetro mydb en lugar de self.mydb
            cursor = mydb.cursor(dictionary=True)
            sql = "SELECT * FROM proyecto WHERE id_proyecto = %s"
            cursor.execute(sql, (id_proy,))
            proyecto_info = cursor.fetchone()

            if proyecto_info:
                print("\n=== Detalles del Proyecto ===")
                for key, value in proyecto_info.items():
                    print(f"{key}: {value}")
            else:
                print("Proyecto no encontrado.")

            cursor.close()

        except mysql.connector.Error as err:
            print(f"Error de base de datos: {err}")
        except Exception as e:
            print(f"Error al ver el proyecto: {str(e)}")

    def actualizar_proyecto_bd(self, mydb):
        try:
            # Verificar si el proyecto existe
            cursor = mydb.cursor(dictionary=True)
            sql_check = "SELECT * FROM proyecto WHERE id_proyecto = %s"
            cursor.execute(sql_check, (self._Id_proyecto,))
            proyecto_actual = cursor.fetchone()

            if not proyecto_actual:
                return False, "Proyecto no encontrado"

            # Actualizar en la base de datos
            sql_update = """
                UPDATE proyecto 
                SET nombre = %s, 
                    descripcion = %s, 
                    fecha_inicio = %s, 
                    fecha_fin = %s 
                WHERE id_proyecto = %s
            """
            
            valores = (
                self._Nombre,
                self._Descripcion,
                self._Fecha_inicio,
                self._Fecha_fin,
                self._Id_proyecto
            )
            
            cursor.execute(sql_update, valores)
            mydb.commit()
            
            return True, "Proyecto actualizado exitosamente"
            
        except mysql.connector.Error as err:
            return False, f"Error de base de datos: {err}"
        except Exception as e:
            return False, f"Error al actualizar el proyecto: {str(e)}"
        finally:
            if cursor:
                cursor.close()

    def eliminar_proyecto(self, mydb):
        try:
            id_proyecto = int(input("Ingrese el ID del proyecto a eliminar: "))
            cursor = mydb.cursor()
            sql = "DELETE FROM proyecto WHERE id_proyecto = %s"
            cursor.execute(sql, (id_proyecto,))
            mydb.commit()
            
            if cursor.rowcount > 0:
                print("Proyecto eliminado con éxito.")
            else:
                print("No se encontró el proyecto para eliminar.")
        except mysql.connector.Error as err:
            print(f"Error de base de datos: {err}")
        except ValueError:
            print("Por favor, ingrese un ID válido (número entero)")
        except Exception as e:
            print(f"Error al eliminar proyecto: {str(e)}")