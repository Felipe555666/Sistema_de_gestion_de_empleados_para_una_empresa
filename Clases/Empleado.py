import mysql.connector
from mysql.connector import Error
from conexion import Conexion
from cryptography.fernet import Fernet
from datetime import datetime
from Tipo_empleado import tipoEmpleado


mydb = Conexion.iniciar_conexion()


class empleado(tipoEmpleado):
    def __init__(self, Id_empleado=None, Nombre=None, Direccion=None, Telefono=None, 
                 Correo=None, Fecha_inicio=None, Salario=None, Fecha_nac=None, 
                 Estado_empleado=None, Contrasena=None, Id_tipo_empleado=None, 
                 Tipo=None, Permiso=None):
        
        super().__init__(Id_tipo_empleado, Tipo, Permiso)
        self._Id_empleado = Id_empleado
        self._Nombre = Nombre
        self._Direccion = Direccion
        self._Telefono = Telefono
        self._Correo = Correo
        self._Fecha_inicio = Fecha_inicio
        self._Salario = Salario
        self._Fecha_nac = Fecha_nac
        self._Estado_empleado = True if Estado_empleado is None else Estado_empleado
        self.__Contrasena = Contrasena
        self._clave = Fernet.generate_key()
        self._cipher_suite = Fernet(self._clave)

    

    def validar_datos(self):
        if not all([self._Nombre, self._Direccion, self._Telefono, self._Correo,
                    self._Fecha_inicio, self._Fecha_nac, self.__Contrasena]):
            return False, "Todos los campos son obligatorios"
        
        if "@" not in self._Correo or "." not in self._Correo:
            return False, "El correo debe tener un formato válido"
        
        if not isinstance(self._Salario, (int, float)) or self._Salario <= 0:
            return False, "El salario debe ser un número positivo"
        
        if not str(self._Telefono).isdigit():
            return False, "El teléfono debe contener solo números"

        return True, "Los datos son válidos"

    def validar_fechas(self):
        formato_fecha = "%Y-%m-%d"
        try:
            fecha_nacimiento = datetime.strptime(self._Fecha_nac, formato_fecha)
            fecha_inicio = datetime.strptime(self._Fecha_inicio, formato_fecha)
            fecha_actual = datetime.now()

            if fecha_inicio <= fecha_nacimiento:
                return False, "La fecha de inicio no puede ser anterior a la fecha de nacimiento"
            
            if fecha_nacimiento > fecha_actual or fecha_inicio > fecha_actual:
                return False, "Las fechas no pueden ser futuras"

            return True, "Las fechas son válidas"
        except ValueError:
            return False, "Las fechas deben tener el formato YYYY-MM-DD"

    def encriptar_contrasena(self):
        if self.__Contrasena:
            self.__Contrasena = self._cipher_suite.encrypt(self.__Contrasena.encode())
            return True, "Contraseña encriptada correctamente"
        return False, "No hay contraseña para encriptar"

    def desencriptar_contrasena(self):
        if self.__Contrasena:
            return True, self._cipher_suite.decrypt(self.__Contrasena).decode()
        return False, "No hay contraseña para desencriptar"

    def obtener_informacion_empleado(self):
        return {
            'ID': self._Id_empleado,
            'Nombre': self._Nombre,
            'Correo': self._Correo,
            'Teléfono': self._Telefono,
            'Fecha Inicio': self._Fecha_inicio,
            'Estado': "Activo" if self._Estado_empleado else "Inactivo"
        }

    def cambiar_estado(self, nuevo_estado):
        if isinstance(nuevo_estado, bool):
            self._Estado_empleado = nuevo_estado
            return True, f"Estado cambiado a {'activo' if nuevo_estado else 'inactivo'}"
        return False, "El estado debe ser un valor booleano"

    def __str__(self):
        return f"Empleado: {self._Nombre} (ID: {self._Id_empleado})"
    
    @classmethod
    def crear_empleado_bd(cls, conexion, empleado):
        try:
            with conexion.cursor() as cursor:
                sql = """INSERT INTO empleado (nombre, direccion, telefono, correo, 
                        fecha_inicio, salario, fecha_nac, estado_empleado, contrasena, 
                        id_tipo_empleado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                valores = (empleado.Nombre, empleado._Direccion, empleado._Telefono, 
                           empleado._correo, empleado._Fecha_inicio, empleado._Salario, 
                           empleado._Fecha_nac, empleado._Estado_empleado, 
                           empleado._Contrasena, empleado._Id_tipo_empleado)
                cursor.execute(sql, valores)
                conexion.commit()
                return True, "Empleado creado exitosamente"
        except Error as e:
            return False, f"Error al crear el empleado en la BD: {str(e)}"

    @classmethod
    def obtener_empleado_bd(cls, conexion, id_empleado):
        try:
            with conexion.cursor(dictionary=True) as cursor:
                sql = "SELECT * FROM empleado WHERE id_empleado = %s"
                cursor.execute(sql, (id_empleado,))
                resultado = cursor.fetchone()
                if resultado:
                    return True, resultado
                return False, "Empleado no encontrado"
        except Error as e:
            return False, f"Error al obtener el empleado de la BD: {str(e)}"
        
    @classmethod
    def actualizar_empleado_bd(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """UPDATE empleado SET nombre = %s, direccion = %s, telefono = %s, 
                        correo = %s, fecha_inicio = %s, salario = %s, fecha_nac = %s, 
                        estado_empleado = %s, contrasena = %s, id_tipo_empleado = %s 
                        WHERE id_empleado = %s"""
                valores = (self._nombre, self._direccion, self._telefono, self._correo, 
                           self._fecha_inicio, self._salario, self._fecha_nac, 
                           self._estado_empleado, self._contrasena, 
                           self._id_empleado)
                cursor.execute(sql, valores)
                conexion.commit()
                if cursor.rowcount > 0:
                    return True, "Empleado actualizado exitosamente"
                return False, "No se encontró el empleado para actualizar"
        except Error as e:
            return False, f"Error al actualizar el empleado en la BD: {str(e)}"

    @classmethod
    def eliminar_empleado_bd(cls, conexion, id_empleado):
        try:
            with conexion.cursor() as cursor:
                sql = "DELETE FROM empleado WHERE id_empleado = %s"
                cursor.execute(sql, (id_empleado,))
                conexion.commit()
                if cursor.rowcount > 0:
                    return True, "Empleado eliminado exitosamente"
                return False, "No se encontró el empleado para eliminar"
        except Error as e:
            return False, f"Error al eliminar el empleado de la BD: {str(e)}"


    def registrar_empleado(self, mydb):
        try:
            print("\n--- Registrar Nuevo Empleado ---")
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            salario = float(input("Salario: "))
            fecha_nac = input("Fecha de nacimiento (YYYY-MM-DD): ")
            contrasena = input("Contraseña: ")
            tipo_empleado = input("Tipo de empleado: ")
            permiso = int(input("Nivel de permiso (0-10): "))

            self._Nombre = nombre
            self._Direccion = direccion
            self._Telefono = telefono
            self._Correo = correo
            self._Fecha_inicio = fecha_inicio
            self._Salario = salario
            self._Fecha_nac = fecha_nac
            self.__Contrasena = contrasena
            self._Tipo = tipo_empleado
            self._Permiso = permiso

            if self.validar_datos()[0] and self.validar_fechas()[0]:
                cursor = mydb.cursor()
                sql = """INSERT INTO empleado (nombre, direccion, telefono, correo, 
                        fecha_inicio, salario, fecha_nac, contrasena, id_tipo_empleado) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                
                sql_tipo = "INSERT INTO tipoEmpleado (Tipo, Permiso) VALUES (%s, %s)"
                cursor.execute(sql_tipo, (tipo_empleado, permiso))
                mydb.commit()
                id_tipo_empleado = cursor.lastrowid

                valores = (nombre, direccion, telefono, correo, fecha_inicio, 
                        salario, fecha_nac, contrasena, id_tipo_empleado)
                cursor.execute(sql, valores)
                mydb.commit()
                
                print("Empleado registrado con éxito.")
                return True, "Empleado registrado exitosamente"
            else:
                print("Error al registrar empleado. Verifique los datos ingresados.")
                return False, "Error en la validación de datos"
                
        except Exception as e:
            print(f"Error al registrar empleado: {str(e)}")
            return False, f"Error al registrar empleado en la BD: {str(e)}"
    
    def ver_empleado(self, mydb):
        try:
            id_emp = int(input("Ingrese el ID del empleado: "))
            cursor = mydb.cursor(dictionary=True)
            
            # Consulta SQL para obtener los datos del empleado y su tipo
            sql = """
            SELECT e.*, te.Tipo, te.Permiso 
            FROM empleado e
            LEFT JOIN tipoEmpleado te ON e.id_tipo_empleado = te.Id_tipo_empleado
            WHERE e.id_empleado = %s
            """
            
            cursor.execute(sql, (id_emp,))
            empleado_data = cursor.fetchone()
            
            if empleado_data:
                print("\n--- Datos del Empleado ---")
                for key, value in empleado_data.items():
                    # Formatear la salida para mejor legibilidad
                    if value is not None:  # Solo mostrar valores no nulos
                        print(f"{key}: {value}")
            else:
                print("Empleado no encontrado.")
                
        except mysql.connector.Error as err:
            print(f"Error de base de datos: {err}")
        except ValueError:
            print("Por favor, ingrese un ID válido (número entero)")
        except Exception as e:
            print(f"Error al ver empleado: {str(e)}")

    
    def actualizar_empleado_bd(self, mydb):
        try:
            id_emp = int(input("Ingrese el ID del empleado a actualizar: "))
            
            cursor = mydb.cursor(dictionary=True)
            
            # Verificar si el empleado existe
            cursor.execute("SELECT * FROM empleado WHERE id_empleado = %s", (id_emp,))
            empleado_actual = cursor.fetchone()
            
            if not empleado_actual:
                print("Empleado no encontrado.")
                return
            
            print("\nDeje en blanco si no desea actualizar el campo.")
            nombre = input(f"Nuevo nombre ({empleado_actual['nombre']}): ") or empleado_actual['nombre']
            direccion = input(f"Nueva dirección ({empleado_actual['direccion']}): ") or empleado_actual['direccion']
            telefono = input(f"Nuevo teléfono ({empleado_actual['telefono']}): ") or empleado_actual['telefono']
            correo = input(f"Nuevo correo ({empleado_actual['correo']}): ") or empleado_actual['correo']
            
            # Actualizar en la base de datos
            sql = """UPDATE empleado 
                     SET nombre = %s, direccion = %s, telefono = %s, correo = %s 
                     WHERE id_empleado = %s"""
            valores = (nombre, direccion, telefono, correo, id_emp)
            
            cursor.execute(sql, valores)
            mydb.commit()
            
            if cursor.rowcount > 0:
                print("Empleado actualizado exitosamente.")
            else:
                print("No se realizaron cambios.")
                
        except mysql.connector.Error as err:
            print(f"Error de base de datos: {err}")
        except ValueError:
            print("Por favor, ingrese un ID válido (número entero)")
        except Exception as e:
            print(f"Error al actualizar empleado: {str(e)}")
        finally:
            if cursor:
                cursor.close()

    def eliminar_empleado(self, mydb):
        try:
            id_emp = int(input("Ingrese el ID del empleado a eliminar: "))
            cursor = mydb.cursor()
            sql = "DELETE FROM empleado WHERE id_empleado = %s"
            cursor.execute(sql, (id_emp,))
            mydb.commit()
            
            if cursor.rowcount > 0:
                print("Empleado eliminado con éxito.")
            else:
                print("No se encontró el empleado para eliminar.")
        except mysql.connector.Error as err:
            print(f"Error de base de datos: {err}")
        except ValueError:
            print("Por favor, ingrese un ID válido (número entero)")
        except Exception as e:
            print(f"Error al eliminar empleado: {str(e)}")