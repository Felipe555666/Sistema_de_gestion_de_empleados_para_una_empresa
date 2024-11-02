import mysql.connector
from conexion import Conexion


mydb = Conexion.iniciar_conexion()

class tipoEmpleado:
    def __init__(self, Id_tipo_empleado=None, Tipo=None, Permiso=None, Desc_empleado=None):
        self._Id_tipo_empleado = Id_tipo_empleado
        self._Tipo = Tipo
        self._Permiso = Permiso
        self._Desc_empleado = Desc_empleado
        


    def validar_tipo_empleado(self):
        """Valida los datos del tipo de empleado."""
        if not isinstance(self._Id_tipo_empleado, int) or self._Id_tipo_empleado <= 0:
            return False, "El ID del tipo de empleado debe ser un número entero positivo."
        
        if not isinstance(self._Tipo, str) or not self._Tipo.strip():
            return False, "El tipo de empleado no puede estar vacío."
        
        if not isinstance(self._Permiso, int) or not (0 <= self._Permiso <= 10):
            return False, "El permiso debe ser un número entero entre 0 y 10."
        
        return True, "Los datos del tipo de empleado son válidos."

    def actualizar_tipo_empleado(self, Tipo=None, Permiso=None):
        """Actualiza el tipo de empleado y/o permiso."""
        if Tipo is not None:
            if isinstance(Tipo, str) and Tipo:
                self._Tipo = Tipo
            else:
                return False, "El tipo debe ser un valor de texto no vacío."

        if Permiso is not None:
            if isinstance(Permiso, int) and 0 <= Permiso <= 10:
                self._Permiso = Permiso
            else:
                return False, "El permiso debe ser un número entero entre 0 y 10."

        return True, "Los datos del tipo de empleado han sido actualizados exitosamente."

    def obtener_informacion_tipo_empleado(self):
        """Devuelve la información del tipo de empleado en un diccionario."""
        return {
            'ID Tipo Empleado': self._Id_tipo_empleado,
            'Tipo': self._Tipo,
            'Permiso': self._Permiso
        }

    def __str__(self):
        return f"Tipo Empleado: {self._Tipo} (ID: {self._Id_tipo_empleado}, Permiso: {self._Permiso})"