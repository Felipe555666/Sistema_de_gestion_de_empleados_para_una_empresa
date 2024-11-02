import mysql.connector
from mysql.connector import Error
from datetime import datetime
from Modulos import modulos
from Tipo_empleado import tipoEmpleado
from conexion import Conexion

mydb = Conexion.iniciar_conexion()


class Accesos(modulos, tipoEmpleado):
    def __init__(self, Id_acceso=None, Id_modulo=None, Nombre=None, Nivel_requerido=None,
                 Id_tipo_empleado=None, Tipo=None, Permiso=None, Desc_empleado=None):
        modulos.__init__(self, Id_modulo, Nombre, Nivel_requerido)
        tipoEmpleado.__init__(self, Id_tipo_empleado, Tipo, Permiso, Desc_empleado)
        self._Id_acceso = Id_acceso
        self._registro_accesos = []  # Lista para almacenar el historial de accesos

    def validar_acceso(self):
        """Valida si el nivel de permiso es suficiente para acceder al módulo"""
        if self._Permiso >= self._Nivel_requerido:
            return True, "Acceso permitido"
        else:
            return False, f"Acceso denegado. Se requiere nivel {self._Nivel_requerido}, usted tiene nivel {self._Permiso}"
    
    def registrar_acceso(self, fecha=None, exitoso=None):
        """Registra el intento de acceso al módulo"""
        try:
            if fecha is None:
                fecha = datetime.now()
            
            if exitoso is None:
                exitoso, mensaje = self.validar_acceso()
            else:
                mensaje = "Acceso permitido" if exitoso else "Acceso denegado"

            registro = {
                'id_acceso': self._Id_acceso,
                'id_modulo': self._Id_modulo,
                'id_tipo_empleado': self._Id_tipo_empleado,
                'fecha': fecha,
                'exitoso': exitoso,
                'mensaje': mensaje
            }
            
            self._registro_accesos.append(registro)
            return exitoso, mensaje
        except Exception as e:
            return False, f"Error al registrar acceso: {str(e)}"
        
    @classmethod
    def obtener_acceso(cls, id_empleado, id_modulo):
        """Obtiene el acceso de un empleado a un módulo"""
        try:
            cursor = mydb.cursor(dictionary=True)

            # Obtener nivel de permiso del empleado
            cursor.execute("""
                SELECT te.Permiso, te.Id_tipo_empleado 
                FROM empleado e 
                JOIN tipoEmpleado te ON e.id_tipo_empleado = te.Id_tipo_empleado 
                WHERE e.id_empleado = %s
            """, (id_empleado,))
            empleado_result = cursor.fetchone()

            if not empleado_result:
                return False, "Empleado no encontrado"
            
            # Obtener nivel requerido del módulo
            cursor.execute("""
                SELECT Nivel_requerido 
                FROM modulos 
                WHERE Id_modulo = %s
            """, (id_modulo,))
            modulo_result = cursor.fetchone()

            if not modulo_result:
                return False, "Módulo no encontrado"
            
            # Crear instancia de Accesos para validar
            acceso = cls(Id_modulo=id_modulo, Id_tipo_empleado=empleado_result['Id_tipo_empleado'],
                          Permiso=empleado_result['Permiso'], Nivel_requerido=modulo_result['Nivel_requerido'])

            return acceso.validar_acceso()
        except Exception as e:
            return False, f"Error al obtener acceso: {str(e)}"
        finally:
            cursor.close()    
        
    def ver_historial_accesos(self):
        """Ver el historial de accesos"""
        try:
            cursor = mydb.cursor(dictionary=True)
            sql = """
            SELECT a.Id_acceso, m.Nombre as Modulo, te.Tipo as Tipo_Empleado, 
                   a.Fecha, a.Exitoso
            FROM Accesos a
            JOIN modulos m ON a.Id_modulo = m.Id_modulo
            JOIN tipoEmpleado te ON a.Id_tipo_empleado = te.Id_tipo_empleado
            ORDER BY a.Fecha DESC
            LIMIT 50
            """
            cursor.execute(sql)
            historial = cursor.fetchall()
            
            if historial:
                print("\n=== Historial de Accesos (últimos 50 registros) ===")
                for acceso in historial:
                    print(f"ID: {acceso['Id_acceso']}")
                    print(f"Módulo: {acceso['Modulo']}")
                    print(f"Tipo Empleado: {acceso['Tipo_Empleado']}")
                    print(f"Fecha: {acceso['Fecha']}")
                    print(f"Exitoso: {'Sí' if acceso['Exitoso'] else 'No'}")
                    print("-" * 30)
            else:
                print("No hay registros de accesos")
        except mysql.connector.Error as err:
            print(f"Error de base de datos: {err}")
        finally:
            if cursor:
                cursor.close()

    def limpiar_historial_accesos(self):
        """Limpia el historial de accesos"""
        try:
            confirmacion = input("¿Está seguro de que desea limpiar el historial de accesos? (S/N): ")
            if confirmacion.upper() != 'S':
                print("Operación cancelada")
                return

            cursor = mydb.cursor()
            sql = "TRUNCATE TABLE Accesos"
            cursor.execute(sql)
            mydb.commit()
            print("Historial de accesos limpiado exitosamente")
        except mysql.connector.Error as err:
            print(f"Error al limpiar historial: {err}")
        finally:
            if cursor:
                cursor.close()        

    def __str__(self):
        """Representación en string de la clase Accesos"""
        return f"Acceso ID: {self._Id_acceso}, Módulo: {self._Nombre}, Nivel requerido: {self.Nivel_requerido}"
        