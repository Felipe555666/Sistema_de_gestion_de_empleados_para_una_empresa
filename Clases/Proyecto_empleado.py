from Empleado import empleado
from Proyecto import proyecto

class proyectoEmpleado(empleado, proyecto):
    def __init__(self, Id_pro_empleado, Id_proyecto, Id_empleado, Nombre, Descripcion, Fecha_inicio, Fecha_fin):
        empleado.__init__(self, Id_empleado)
        proyecto.__init__(self, Id_proyecto, Nombre, Descripcion, Fecha_inicio, Fecha_fin)
        self._Id_pro_empleado = Id_pro_empleado

    def validar_proyecto_empleado(self):
        """Valida los datos de la asignación proyecto-empleado"""
        try:
            if not isinstance(self._Id_pro_empleado, int) or self._Id_pro_empleado <= 0:
                return False, "El ID de proyecto-empleado debe ser un número entero positivo"
            
            # Validar datos del proyecto
            validacion_proyecto, mensaje_proyecto = self.validar_fechas()
            if not validacion_proyecto:
                return False, f"Error en los datos del proyecto: {mensaje_proyecto}"
            
            # Validar datos del empleado (asumiendo que existe un método similar en la clase empleado)
            validacion_empleado, mensaje_empleado = self.validar_datos()
            if not validacion_empleado:
                return False, f"Error en los datos del empleado: {mensaje_empleado}"
            
            return True, "Datos de proyecto-empleado válidos"
        except Exception as e:
            return False, f"Error en la validación de proyecto-empleado: {str(e)}"

    def obtener_informacion_proyecto_empleado(self):
        """Retorna la información básica de la asignación proyecto-empleado"""
        return {
            'ID Proyecto-Empleado': self._Id_pro_empleado,
            'ID Proyecto': self._Id_proyecto,
            'ID Empleado': self._Id_empleado,
            'Nombre Proyecto': self._Nombre,
            'Fecha Inicio': self._Fecha_inicio,
            'Fecha Fin': self._Fecha_fin
        }

    def actualizar_asignacion(self, nuevo_id_proyecto=None, nuevo_id_empleado=None):
        """Actualiza la asignación proyecto-empleado"""
        if nuevo_id_proyecto:
            self._Id_proyecto = nuevo_id_proyecto
        if nuevo_id_empleado:
            self._Id_empleado = nuevo_id_empleado
        
        validacion, mensaje = self.validar_proyecto_empleado()
        if not validacion:
            return False, mensaje
        
        return True, "Asignación proyecto-empleado actualizada correctamente"

    def __str__(self):
        """Representación en string de la asignación proyecto-empleado"""
        return f"Proyecto-Empleado: ID {self._Id_pro_empleado} - Proyecto: {self._Nombre} - Empleado ID: {self._Id_empleado}"


    def asignar_empleado_proyecto(self):
        id_emp = int(input("Ingrese el ID del empleado: "))
        id_proy = int(input("Ingrese el ID del proyecto: "))
        if id_emp in self.empleados and id_proy in self.proyectos:
            # Aquí se debería crear una instancia de proyectoEmpleado
            print("Empleado asignado al proyecto con éxito.")
        else:
            print("Empleado o proyecto no encontrado.")