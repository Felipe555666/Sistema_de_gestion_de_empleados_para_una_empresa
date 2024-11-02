import mysql.connector
from mysql.connector import Error
from conexion import Conexion

mydb = Conexion.iniciar_conexion()

class DepartamentoEmpleado:
    def __init__(self, Id_dep_empleado=None, Id_departamento=None, Id_empleado=None):
        self._Id_dep_empleado = Id_dep_empleado
        self._Id_departamento = Id_departamento
        self._Id_empleado = Id_empleado

    def validar_asignacion(self):
        """Valida que la asignación sea correcta"""
        try:
            if not isinstance(self._Id_dep_empleado, int) or self._Id_dep_empleado <= 0:
                return False, "El ID de asignación debe ser un número entero positivo"
            
            if not isinstance(self._Id_departamento, int) or self._Id_departamento <= 0:
                return False, "El ID de departamento debe ser un número entero positivo"
            
            if not isinstance(self._Id_empleado, int) or self._Id_empleado <= 0:
                return False, "El ID de empleado debe ser un número entero positivo"
            
            return True, "Asignación válida"
        except Exception as e:
            return False, f"Error en la validación: {str(e)}"
        
    def obtener_informacion_asignacion(self):
        """Retorna la información de la asignación"""
        return {
            'id_asignacion': self._Id_dep_empleado,
            'id_departamento': self._Id_departamento,
            'id_empleado': self._Id_empleado
        }

    def actualizar_asignacion(self, nuevo_id_departamento=None, nuevo_id_empleado=None):
        """Actualiza la asignación del empleado al departamento"""
        if nuevo_id_departamento:
            self._Id_departamento = nuevo_id_departamento
        if nuevo_id_empleado:
            self._Id_empleado = nuevo_id_empleado
        
        es_valido, mensaje = self.validar_asignacion()
        if es_valido:
            return True, "Asignación actualizada correctamente"
        else:
            return False, f"Error al actualizar la asignación: {mensaje}"
        
    @classmethod
    def crear_departamento_empleado_bd(cls, conexion, departamento_empleado):
        try:
            with conexion.cursor() as cursor:
                sql = """INSERT INTO departamentoEmpleado (Id_departamento, Id_empleado) 
                        VALUES (%s, %s)"""
                valores = (departamento_empleado._Id_departamento, departamento_empleado._Id_empleado)
                cursor.execute(sql, valores)
                conexion.commit()
                return True, "Empleado asignado al departamento exitosamente"
        except Error as e:
            return False, f"Error al asignar empleado al departamento en la BD: {str(e)}"

    @classmethod
    def obtener_departamento_empleado_bd(cls, conexion, id_dep_empleado):
        try:
            with conexion.cursor(dictionary=True) as cursor:
                sql = "SELECT * FROM departamentoEmpleado WHERE Id_dep_empleado = %s"
                cursor.execute(sql, (id_dep_empleado,))
                resultado = cursor.fetchone()
                if resultado:
                    return True, resultado
                return False, "Asignación de departamento-empleado no encontrada"
        except Error as e:
            return False, f"Error al obtener la asignación de departamento-empleado de la BD: {str(e)}"

    def actualizar_departamento_empleado_bd(self, conexion):
        """Actualiza una asignación de departamento-empleado existente en la base de datos"""
        try:
            with conexion.cursor() as cursor:
                sql = """UPDATE departamentoEmpleado SET Id_departamento = %s, Id_empleado = %s 
                        WHERE Id_dep_empleado = %s"""
                valores = (self._Id_departamento, self._Id_empleado, self._Id_dep_empleado)
                cursor.execute(sql, valores)
                conexion.commit()
                if cursor.rowcount > 0:
                    return True, "Asignación de departamento-empleado actualizada exitosamente"
                return False, "No se encontró la asignación para actualizar"
        except Error as e:
            return False, f"Error al actualizar la asignación de departamento-empleado en la BD: {str(e)}"

    @classmethod
    def eliminar_departamento_empleado_bd(cls, conexion, id_dep_empleado):
        try:
            with conexion.cursor() as cursor:
                sql = "DELETE FROM departamentoEmpleado WHERE Id_dep_empleado = %s"
                cursor.execute(sql, (id_dep_empleado,))
                conexion.commit()
                if cursor.rowcount > 0:
                    return True, "Asignación de departamento-empleado eliminada exitosamente"
                return False, "No se encontró la asignación para eliminar"
        except Error as e:
            return False, f"Error al eliminar la asignación de departamento-empleado de la BD: {str(e)}"

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
        
    def __str__(self):
        """Representación en string de la asignación"""
        return (f"Asignación ID: {self._Id_dep_empleado} - "
                f"Departamento: {self._Id_departamento} - "
                f"Empleado: {self._Id_empleado}")
