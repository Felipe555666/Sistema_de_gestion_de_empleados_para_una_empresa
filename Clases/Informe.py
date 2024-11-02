import mysql.connector
from mysql.connector import  Error
from datetime import datetime
from Empleado import empleado
from conexion import Conexion

mydb = Conexion.iniciar_conexion()


from Empleado import empleado

class informe(empleado):
    def __init__(self, Id_informe=None, Nombre_informe=None, Fecha_creacion=None, 
                 Id_empleado=None, Estado_informe=None, Id_tipo_empleado=None, 
                 Tipo=None, Permiso=None, Desc_empleado=None):
        super().__init__(Id_empleado, Id_tipo_empleado, Tipo, Permiso, Desc_empleado)
        self._Id_informe = Id_informe
        self._Nombre_informe = Nombre_informe
        self._Fecha_creacion = Fecha_creacion
        self._Estado_informe = Estado_informe

    def validar_informe(self):
        """Valida los datos del informe"""
        try:
            if not isinstance(self._Id_informe, int) or self._Id_informe <= 0:
                return False, "El ID del informe debe ser un número entero positivo"
            
            if not self._Nombre_informe or not isinstance(self._Nombre_informe, str):
                return False, "El nombre del informe no puede estar vacío y debe ser texto"
            
            if not self._Estado_informe or not isinstance(self._Estado_informe, str):
                return False, "El estado del informe no puede estar vacío y debe ser texto"
            
            fecha_valida, mensaje = self.validar_fecha_creacion()
            if not fecha_valida:
                return False, mensaje
            
            return True, "Datos del informe válidos"
        except Exception as e:
            return False, f"Error en la validación del informe: {str(e)}"

    def validar_fecha_creacion(self):
        """Valida la fecha de creación del informe"""
        formato_fecha = "%Y-%m-%d"
        try:
            fecha_creacion = datetime.strptime(self._Fecha_creacion, formato_fecha)
            fecha_actual = datetime.now()
            
            if fecha_creacion > fecha_actual:
                return False, "La fecha de creación no puede estar en el futuro"
            
            return True, "La fecha de creación es válida"
        except ValueError:
            return False, "La fecha de creación no está en el formato correcto (YYYY-MM-DD)"
        except Exception as e:
            return False, f"Error en la validación de la fecha: {str(e)}"

    def crear_informe(self, mydb):
        try:
            print("\n--- Crear Nuevo Informe ---")
            nombre = input("Nombre del informe: ")
            fecha = input("Fecha de creación (YYYY-MM-DD): ")
            id_emp = int(input("ID del empleado: "))
            estado = input("Estado del informe: ")
            
            cursor = mydb.cursor()
            sql = """INSERT INTO informe (Nombre_informe, Fecha_creacion, 
                    Id_empleado, Estado_informe) VALUES (%s, %s, %s, %s)"""
            valores = (nombre, fecha, id_emp, estado)
            
            cursor.execute(sql, valores)
            mydb.commit()
            print("Informe creado exitosamente")
            return True, "Informe creado exitosamente"
            
        except Exception as e:
            print(f"Error al crear informe: {str(e)}")
            return False, f"Error al crear informe: {str(e)}"
        finally:
            if cursor:
                cursor.close()

    def ver_informe(self, mydb):
        try:
            id_informe = int(input("\nIngrese el ID del informe: "))
            cursor = mydb.cursor(dictionary=True)
            
            sql = """
            SELECT i.*, e.nombre as nombre_empleado 
            FROM informe i
            JOIN empleado e ON i.Id_empleado = e.id_empleado
            WHERE i.Id_informe = %s
            """
            
            cursor.execute(sql, (id_informe,))
            informe_data = cursor.fetchone()
            
            if informe_data:
                print("\n=== Detalles del Informe ===")
                for key, value in informe_data.items():
                    print(f"{key}: {value}")
            else:
                print("Informe no encontrado")
                
        except Exception as e:
            print(f"Error al ver informe: {str(e)}")
        finally:
            if cursor:
                cursor.close()

    def actualizar_informe(self, mydb):
        try:
            id_informe = int(input("\nIngrese el ID del informe a actualizar: "))
            
            cursor = mydb.cursor()
            # Verificar si el informe existe
            cursor.execute("SELECT * FROM informe WHERE Id_informe = %s", (id_informe,))
            if not cursor.fetchone():
                print("Informe no encontrado")
                return
            
            print("\nDeje en blanco si no desea actualizar el campo")
            nombre = input("Nuevo nombre del informe: ")
            estado = input("Nuevo estado del informe: ")
            
            updates = []
            valores = []
            if nombre:
                updates.append("Nombre_informe = %s")
                valores.append(nombre)
            if estado:
                updates.append("Estado_informe = %s")
                valores.append(estado)
            
            if updates:
                sql = f"UPDATE informe SET {', '.join(updates)} WHERE Id_informe = %s"
                valores.append(id_informe)
                cursor.execute(sql, tuple(valores))
                mydb.commit()
                print("Informe actualizado exitosamente")
            
        except Exception as e:
            print(f"Error al actualizar informe: {str(e)}")
        finally:
            if cursor:
                cursor.close()

    def eliminar_informe(self, mydb):
        try:
            id_informe = int(input("\nIngrese el ID del informe a eliminar: "))
            
            cursor = mydb.cursor()
            cursor.execute("DELETE FROM informe WHERE Id_informe = %s", (id_informe,))
            mydb.commit()
            
            if cursor.rowcount > 0:
                print("Informe eliminado exitosamente")
            else:
                print("Informe no encontrado")
                
        except Exception as e:
            print(f"Error al eliminar informe: {str(e)}")
        finally:
            if cursor:
                cursor.close()

    def __str__(self):
        """Representación en string del informe"""
        return f"Informe: {self._Nombre_informe} (ID: {self._Id_informe})"
