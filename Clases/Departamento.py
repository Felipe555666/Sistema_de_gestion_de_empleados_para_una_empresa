import mysql.connector
from mysql.connector import Error
from Empleado import empleado
from Departamento_empleado import DepartamentoEmpleado
from conexion import Conexion

mydb = Conexion.iniciar_conexion()

class Departamento:
    def __init__(self, Id_departamento=0, Nombre="", Telefono=""):
        self._Id_departamento = Id_departamento
        self._Nombre = Nombre
        self._Telefono = Telefono
        
    def validar_departamento(self):
        """Método para validar los datos del departamento"""
        try:
            if not isinstance(self._Id_departamento, int) or self._Id_departamento <= 0:
                return False, "El ID del departamento debe ser un número entero positivo"
            
            if not self._Nombre or not isinstance(self._Nombre, str):
                return False, "El nombre del departamento no puede estar vacío y debe ser texto"
            
            if not self._Telefono:
                return False, "El teléfono del departamento no puede estar vacío"
            
            if not str(self._Telefono).isdigit():
                return False, "El teléfono debe contener solo números"
            
            return True, "Datos del departamento válidos"
        except Exception as e:
            return False, f"Error en la validación: {str(e)}"
        
    @classmethod
    def ver_departamentos_db(cls):
        mydb = None
        cursor = None
        try:
            mydb = Conexion.iniciar_conexion()
            if mydb:
                cursor = mydb.cursor(dictionary=True)
                cursor.execute("SELECT * FROM departamento")
                departamentos = cursor.fetchall()
                
                if departamentos:
                    print("\n=== Lista de Departamentos ===")
                    for dep in departamentos:
                        print(f"ID: {dep.get('Id_departamento', 'N/A')}")
                        print(f"Nombre: {dep.get('Nombre', 'N/A')}")
                        print(f"Teléfono: {dep.get('Telefono', 'N/A')}")
                        print("-" * 20)
                else:
                    print("No hay departamentos registrados")
                    
        except mysql.connector.Error as err:
            print(f"Error de MySQL: {err}")
        except Exception as e:
            print(f"Error al consultar departamentos: {str(e)}")
        finally:
            if cursor:
                cursor.close()
            if mydb and mydb.is_connected():
                mydb.close()
    
    @classmethod
    def crear_departamento_bd(cls, conexion, departamento):
        try:
            with conexion.cursor() as cursor:
                sql = """INSERT INTO departamento (Id_departamento, Nombre, Telefono) 
                        VALUES (%s, %s, %s)"""
                valores = (departamento._Id_departamento, departamento._Nombre, 
                        departamento._Telefono)
                cursor.execute(sql, valores)
                conexion.commit()
                return True, "Departamento creado exitosamente"
        except Error as e:
            return False, f"Error al crear el departamento en la BD: {str(e)}"

    @classmethod
    def obtener_departamento_bd(cls, conexion, id_departamento):
        try:
            with conexion.cursor(dictionary=True) as cursor:
                sql = "SELECT * FROM departamento WHERE Id_departamento = %s"
                cursor.execute(sql, (id_departamento,))
                resultado = cursor.fetchone()
                if resultado:
                    return True, resultado
                return False, "Departamento no encontrado"
        except Error as e:
            return False, f"Error al obtener el departamento de la BD: {str(e)}"

    def actualizar_departamento_bd(self, conexion):
        """Actualiza un departamento existente en la base de datos"""
        try:
            with conexion.cursor() as cursor:
                sql = """UPDATE departamento SET Nombre = %s, Telefono = %s 
                        WHERE Id_departamento = %s"""
                valores = (self._Nombre, self._Telefono, self._Id_departamento)
                cursor.execute(sql, valores)
                conexion.commit()
                if cursor.rowcount > 0:
                    return True, "Departamento actualizado exitosamente"
                return False, "No se encontró el departamento para actualizar"
        except Error as e:
            return False, f"Error al actualizar el departamento en la BD: {str(e)}"

    @classmethod
    def eliminar_departamento_bd(cls, conexion, id_departamento):
        try:
            with conexion.cursor() as cursor:
                # Primero verificar si hay empleados asignados
                check_sql = """SELECT COUNT(*) FROM departamentoEmpleado 
                            WHERE Id_departamento = %s"""
                cursor.execute(check_sql, (id_departamento,))
                count = cursor.fetchone()[0]
                
                if count > 0:
                    return False, f"No se puede eliminar el departamento. Hay {count} empleados asignados."
                
                # Si no hay empleados asignados, proceder con la eliminación
                sql = "DELETE FROM departamento WHERE Id_departamento = %s"
                cursor.execute(sql, (id_departamento,))
                conexion.commit()
                
                if cursor.rowcount > 0:
                    return True, "Departamento eliminado exitosamente"
                return False, "No se encontró el departamento para eliminar"
        except Error as e:
            return False, f"Error al eliminar el departamento de la BD: {str(e)}"

    @classmethod
    def asignar_empleado_departamento_bd(cls, conexion, id_empleado, id_departamento):
        try:
            with conexion.cursor() as cursor:
                # Verificar si el empleado existe
                cursor.execute("SELECT id_empleado FROM empleado WHERE id_empleado = %s", 
                            (id_empleado,))
                if not cursor.fetchone():
                    return False, "El empleado no existe"

                # Verificar si el departamento existe
                cursor.execute("SELECT Id_departamento FROM departamento WHERE Id_departamento = %s", 
                            (id_departamento,))
                if not cursor.fetchone():
                    return False, "El departamento no existe"

                # Verificar si la asignación ya existe
                cursor.execute("""SELECT * FROM departamentoEmpleado 
                                WHERE Id_empleado = %s AND Id_departamento = %s""", 
                            (id_empleado, id_departamento))
                if cursor.fetchone():
                    return False, "El empleado ya está asignado a este departamento"

                # Realizar la asignación
                sql = """INSERT INTO departamentoEmpleado 
                        (Id_departamento, Id_empleado) VALUES (%s, %s)"""
                cursor.execute(sql, (id_departamento, id_empleado))
                conexion.commit()
                return True, "Empleado asignado al departamento exitosamente"
        except Error as e:
            return False, f"Error al asignar empleado al departamento en la BD: {str(e)}"

    @classmethod
    def obtener_empleados_por_departamento_bd(cls, conexion, id_departamento):
        """Obtiene todos los empleados asignados a un departamento específico"""
        try:
            with conexion.cursor(dictionary=True) as cursor:
                sql = """
                SELECT e.id_empleado, e.nombre
                FROM empleado e
                JOIN departamentoEmpleado de ON e.id_empleado = de.Id_empleado
                WHERE de.Id_departamento = %s
                """
                cursor.execute(sql, (id_departamento,))
                resultados = cursor.fetchall()
                if resultados:
                    return True, resultados
                return False, "No hay empleados asignados a este departamento"
        except Error as e:
            return False, f"Error al obtener los empleados del departamento: {str(e)}"


    def ver_departamentos(self, mydb):
        try:
            id_dep_input = input("Ingrese el ID del departamento: ")
            if not id_dep_input.isdigit():
                print("Por favor, ingrese un ID válido (número entero).")
                return

            id_dep = int(id_dep_input)

            cursor = mydb.cursor(dictionary=True)
            sql = "SELECT * FROM departamento WHERE id_departamento = %s"
            cursor.execute(sql, (id_dep,))
            departamento_info = cursor.fetchone()

            if departamento_info:
                print("\n=== Detalles del Departamento ===")
                for key, value in departamento_info.items():
                    print(f"{key}: {value}")
            else:
                print("Departamento no encontrado.")

            cursor.close()

        except mysql.connector.Error as err:
            print(f"Error de base de datos: {err}")
        except Exception as e:
            print(f"Error al ver el departamento: {str(e)}")

    def crear_departamento(self):
        try:
            print("\n--- Crear Nuevo Departamento ---")
            id_departamento = input("ID del departamento: ")
            nombre = input("Nombre del departamento: ")
            telefono = input("Teléfono del departamento: ")

            departamento = Departamento(
                Id_departamento=int(id_departamento),
                Nombre=nombre,
                Telefono=telefono
            )

            es_valido, mensaje = departamento.validar_departamento()
            if not es_valido:
                print(f"Error de validación: {mensaje}")
                return

            mydb = Conexion.iniciar_conexion()
            if not mydb:
                print("Error: No se pudo establecer conexión con la base de datos")
                return

            exito, mensaje = Departamento.crear_departamento_bd(mydb, departamento)
            print(mensaje)

            if mydb:
                mydb.close()

        except ValueError:
            print("Error: El ID del departamento debe ser un número entero")
        except Exception as e:
            print(f"Error al crear departamento: {str(e)}")

    def actualizar_departamento(self):
        """Actualiza un departamento existente"""
        try:
            print("\n--- Actualizar Departamento ---")
            id_departamento = input("Ingrese el ID del departamento a actualizar: ")
            
            if not id_departamento.isdigit():
                print("Error: El ID debe ser un número entero")
                return

            # Obtener conexión
            mydb = Conexion.iniciar_conexion()
            if not mydb:
                print("Error: No se pudo establecer conexión con la base de datos")
                return

            # Verificar si el departamento existe
            exito, resultado = Departamento.obtener_departamento_bd(mydb, int(id_departamento))
            if not exito:
                print(resultado)
                return

            # Mostrar datos actuales
            print("\nDatos actuales:")
            print(f"Nombre: {resultado['Nombre']}")
            print(f"Teléfono: {resultado['Telefono']}")

            # Solicitar nuevos datos
            print("\nDeje en blanco si no desea modificar el campo")
            nuevo_nombre = input("Nuevo nombre: ") or resultado['Nombre']
            nuevo_telefono = input("Nuevo teléfono: ") or resultado['Telefono']

            # Crear objeto departamento con los nuevos datos
            departamento_actualizado = Departamento(
                Id_departamento=int(id_departamento),
                Nombre=nuevo_nombre,
                Telefono=nuevo_telefono
            )

            # Validar los nuevos datos
            es_valido, mensaje = departamento_actualizado.validar_departamento()
            if not es_valido:
                print(f"Error de validación: {mensaje}")
                return

            # Actualizar en la base de datos
            exito, mensaje = departamento_actualizado.actualizar_departamento_bd(mydb)
            print(mensaje)

        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error al actualizar departamento: {str(e)}")
        finally:
            if 'mydb' in locals() and mydb:
                mydb.close()

    def eliminar_departamento(self):
        """Elimina un departamento existente"""
        try:
            print("\n--- Eliminar Departamento ---")
            id_departamento = input("Ingrese el ID del departamento a eliminar: ")
            
            if not id_departamento.isdigit():
                print("Error: El ID debe ser un número entero")
                return

            # Obtener conexión
            mydb = Conexion.iniciar_conexion()
            if not mydb:
                print("Error: No se pudo establecer conexión con la base de datos")
                return

            # Eliminar el departamento
            exito, mensaje = Departamento.eliminar_departamento_bd(mydb, int(id_departamento))
            print(mensaje)

        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error al eliminar departamento: {str(e)}")
        finally:
            if 'mydb' in locals() and mydb:
                mydb.close()

    def asignar_empleado_departamento(self):
        """Asigna un empleado a un departamento"""
        try:
            print("\n--- Asignar Empleado a Departamento ---")
            id_emp = int(input("ID del empleado: "))
            id_dep = int(input("ID del departamento: "))
            
            # Obtener conexión
            mydb = Conexion.iniciar_conexion()
            if not mydb:
                print("Error: No se pudo establecer conexión con la base de datos")
                return

            cursor = mydb.cursor()
            
            # Verificar si el empleado existe
            cursor.execute("SELECT id_empleado FROM empleado WHERE id_empleado = %s", (id_emp,))
            if not cursor.fetchone():
                print("Error: El empleado no existe")
                return

            # Verificar si el departamento existe
            cursor.execute("SELECT Id_departamento FROM departamento WHERE Id_departamento = %s", (id_dep,))
            if not cursor.fetchone():
                print("Error: El departamento no existe")
                return

            # Verificar si la asignación ya existe
            cursor.execute("""SELECT * FROM departamentoEmpleado 
                            WHERE Id_empleado = %s AND Id_departamento = %s""", 
                        (id_emp, id_dep))
            if cursor.fetchone():
                print("Error: El empleado ya está asignado a este departamento")
                return

            # Realizar la asignación
            sql = """INSERT INTO departamentoEmpleado 
                    (Id_departamento, Id_empleado) VALUES (%s, %s)"""
            cursor.execute(sql, (id_dep, id_emp))
            mydb.commit()
            
            print("Empleado asignado al departamento exitosamente")

        except ValueError:
            print("Error: Los IDs deben ser números enteros")
        except mysql.connector.Error as err:
            print(f"Error de base de datos: {err}")
        except Exception as e:
            print(f"Error al asignar empleado al departamento: {str(e)}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'mydb' in locals() and mydb:
                mydb.close()
    
    def ver_empleados_departamento(self):
        try:
            id_dep = int(input("ID del departamento: "))
            
            # Obtener conexión
            mydb = Conexion.iniciar_conexion()
            if not mydb:
                print("Error: No se pudo establecer conexión con la base de datos")
                return

            cursor = mydb.cursor(dictionary=True)
            sql = """
            SELECT e.id_empleado, e.nombre
            FROM empleado e
            JOIN departamentoEmpleado de ON e.id_empleado = de.Id_empleado
            WHERE de.Id_departamento = %s
            """
            cursor.execute(sql, (id_dep,))
            empleados = cursor.fetchall()
            
            if empleados:
                print(f"\n=== Empleados del Departamento ID {id_dep} ===")
                for emp in empleados:
                    print(f"ID: {emp['id_empleado']}, Nombre: {emp['nombre']}")
            else:
                print("No hay empleados asignados a este departamento")
        except mysql.connector.Error as err:
            print(f"Error de base de datos: {err}")
        except ValueError:
            print("Error: El ID del departamento debe ser un número entero")
        except Exception as e:
            print(f"Error al ver empleados del departamento: {str(e)}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'mydb' in locals() and mydb:
                mydb.close()

    def __str__(self):
        """Representación en string del departamento"""
        return f"Departamento: {self._Nombre} (ID: {self._Id_departamento})"