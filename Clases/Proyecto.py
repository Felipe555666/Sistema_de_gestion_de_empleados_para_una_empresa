from datetime import datetime
class proyecto:
    def __init__(self,Id_proyecto,Nombre,Descripcion,Fecha_inicio,Fecha_fin):
        self.__Id_proyecto = Id_proyecto
        self._Nombre = Nombre
        self._Descripcion = Descripcion
        self._Fecha_inicio = Fecha_inicio
        self._Fecha_fin = Fecha_fin
    
    def validar_fechas(self):

        formato_fecha = "%Y-%m-%d"

        try:
            fecha_inicio = datetime.strptime(self._Fecha_inicio, formato_fecha)
        except ValueError:
            return False, "La fecha de inicio no esta en el formato correcto"
        
        try:
            fecha_fin = datetime.strptime(self._Fecha_fin, formato_fecha)
        except:
            return False, "La fecha de fin no esta en el formato correcto"
        
        if fecha_inicio > fecha_fin:
            return False, "La fecha de inicio no puede se posterior a la fecha fin"
        
        fecha_actual = datetime.now()
        if fecha_inicio > fecha_actual or fecha_fin > fecha_actual:
            return False, "Las fechas no puedes ir al futuro"
        
        return True, "las fechas son validas"
    
    
    
    # Método para crear un proyecto en la base de datos
    @classmethod
    def crear_proyecto(cls, Id_proyecto, Nombre, Descripcion, Fecha_inicio, Fecha_fin):
        conexion = obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                sql = "INSERT INTO proyectos (Id_proyecto, Nombre, Descripcion, Fecha_inicio, Fecha_fin) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (Id_proyecto, Nombre, Descripcion, Fecha_inicio, Fecha_fin))
                conexion.commit()
            return f"Proyecto {Nombre} creado exitosamente."
        except Error as e:
            return f"Error al crear el proyecto: {str(e)}"
        finally:
            conexion.close()
    
    # Método para leer un proyecto de la base de datos
    @classmethod
    def leer_proyecto(cls, Id_proyecto):
        conexion = obtener_conexion()
        try:
            with conexion.cursor(dictionary=True) as cursor:
                sql = "SELECT * FROM proyectos WHERE Id_proyecto = %s"
                cursor.execute(sql, (Id_proyecto,))
                proyecto = cursor.fetchone()
            return proyecto if proyecto else "Proyecto no encontrado."
        except Error as e:
            return f"Error al leer el proyecto: {str(e)}"
        finally:
            conexion.close()
    
    # Método para actualizar un proyecto en la base de datos
    def actualizar_proyecto(self, Nombre=None, Descripcion=None, Fecha_inicio=None, Fecha_fin=None):
        conexion = obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                sql = "UPDATE proyectos SET Nombre = %s, Descripcion = %s, Fecha_inicio = %s, Fecha_fin = %s WHERE Id_proyecto = %s"
                cursor.execute(sql, (
                    Nombre or self.Nombre,
                    Descripcion or self.Descripcion,
                    Fecha_inicio or self.Fecha_inicio,
                    Fecha_fin or self.Fecha_fin,
                    self.Id_proyecto
                ))
                conexion.commit()
            return "Proyecto actualizado exitosamente."
        except Error as e:
            return f"Error al actualizar el proyecto: {str(e)}"
        finally:
            conexion.close()
    
    # Método para eliminar un proyecto de la base de datos
    @classmethod
    def eliminar_proyecto(cls, Id_proyecto):
        conexion = obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                sql = "DELETE FROM proyectos WHERE Id_proyecto = %s"
                cursor.execute(sql, (Id_proyecto,))
                conexion.commit()
            return "Proyecto eliminado exitosamente."
        except Error as e:
            return f"Error al eliminar el proyecto: {str(e)}"
        finally:
            conexion.close()
    
    # Método para asignar un empleado a un proyecto
    @classmethod
    def asignar_empleado(cls, Id_proyecto, Id_empleado):
        conexion = obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                sql = "INSERT INTO proyecto_empleados (Id_proyecto, Id_empleado) VALUES (%s, %s)"
                cursor.execute(sql, (Id_proyecto, Id_empleado))
                conexion.commit()
            return f"Empleado {Id_empleado} asignado al proyecto {Id_proyecto}."
        except Error as e:
            return f"Error al asignar empleado: {str(e)}"
        finally:
            conexion.close()
    
    # Método para eliminar un empleado de un proyecto
    @classmethod
    def eliminar_empleado(cls, Id_proyecto, Id_empleado):
        conexion = obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                sql = "DELETE FROM proyecto_empleados WHERE Id_proyecto = %s AND Id_empleado = %s"
                cursor.execute(sql, (Id_proyecto, Id_empleado))
                conexion.commit()
            return f"Empleado {Id_empleado} eliminado del proyecto {Id_proyecto}."
        except Error as e:
            return f"Error al eliminar empleado: {str(e)}"
        finally:
            conexion.close()
    