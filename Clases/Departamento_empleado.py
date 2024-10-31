from Departamento import departamento
from Empleado import empleado

class departamento_empleado(departamento, empleado):
    def __init__(self, Id_dep_empleado, Id_departamento, Id_empleado):
        departamento.__init__(self, Id_departamento)
        empleado.__init__(self, Id_empleado)
        self._Id_dep_empleado = Id_dep_empleado

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

    def __str__(self):
        """Representación en string de la asignación"""
        return (f"Asignación ID: {self._Id_dep_empleado} - "
                f"Departamento: {self._Id_departamento} - "
                f"Empleado: {self._Id_empleado}")
