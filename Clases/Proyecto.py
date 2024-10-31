from datetime import datetime
from mysql.connector import Error

class proyecto:
    def __init__(self, Id_proyecto, Nombre, Descripcion, Fecha_inicio, Fecha_fin):
        self._Id_proyecto = Id_proyecto
        self._Nombre = Nombre
        self._Descripcion = Descripcion
        self._Fecha_inicio = Fecha_inicio
        self._Fecha_fin = Fecha_fin

    def validar_proyecto(self):
        """Valida todos los datos del proyecto"""
        try:
            # Validar ID
            if not isinstance(self._Id_proyecto, int) or self._Id_proyecto <= 0:
                return False, "El ID del proyecto debe ser un número entero positivo"
            
            # Validar nombre
            if not isinstance(self._Nombre, str) or not self._Nombre.strip():
                return False, "El nombre del proyecto no puede estar vacío"
            
            # Validar descripción
            if not isinstance(self._Descripcion, str) or not self._Descripcion.strip():
                return False, "La descripción del proyecto no puede estar vacía"
            
            # Validar fechas
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
            # Convertir strings a objetos datetime
            fecha_inicio = datetime.strptime(self._Fecha_inicio, formato_fecha)
            fecha_fin = datetime.strptime(self._Fecha_fin, formato_fecha)
            fecha_actual = datetime.now()

            # Validar que fecha_inicio sea anterior a fecha_fin
            if fecha_inicio > fecha_fin:
                return False, "La fecha de inicio no puede ser posterior a la fecha de fin"
            
            # Validar que las fechas no estén en el futuro
            if fecha_inicio > fecha_actual or fecha_fin > fecha_actual:
                return False, "Las fechas no pueden estar en el futuro"
            
            return True, "Las fechas son válidas"
        except ValueError:
            return False, "Las fechas deben estar en formato YYYY-MM-DD"
        except Exception as e:
            return False, f"Error en la validación de fechas: {str(e)}"

    def obtener_informacion_proyecto(self):
        """Retorna la información básica del proyecto"""
        return {
            'ID': self._Id_proyecto,
            'Nombre': self._Nombre,
            'Descripción': self._Descripcion,
            'Fecha Inicio': self._Fecha_inicio,
            'Fecha Fin': self._Fecha_fin
        }

    def actualizar_proyecto(self, nombre=None, descripcion=None, fecha_inicio=None, fecha_fin=None):
        """Actualiza la información del proyecto"""
        try:
            if nombre:
                self._Nombre = nombre
            if descripcion:
                self._Descripcion = descripcion
            if fecha_inicio:
                self._Fecha_inicio = fecha_inicio
            if fecha_fin:
                self._Fecha_fin = fecha_fin

            # Validar los nuevos datos
            validacion, mensaje = self.validar_proyecto()
            if not validacion:
                return False, mensaje

            return True, "Proyecto actualizado correctamente"
        except Exception as e:
            return False, f"Error al actualizar el proyecto: {str(e)}"

    def __str__(self):
        """Representación en string del proyecto"""
        return f"Proyecto: {self._Nombre} (ID: {self._Id_proyecto})"

    # Métodos para la base de datos
    @classmethod
    def crear_proyecto_bd(cls, conexion, proyecto):
        """Crea un nuevo proyecto en la base de datos"""
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
        """Obtiene un proyecto de la base de datos por su ID"""
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
        """Elimina un proyecto de la base de datos"""
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