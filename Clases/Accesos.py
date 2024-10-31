from Modulos import modulos
from Tipo_empleado import tipoEmpleado

class Accesos(modulos, tipoEmpleado):
    def __init__(self, Id_acceso, Id_modulo, Nombre, Nivel_requerido,
                 Id_tipo_empleado, Tipo, Permiso, Desc_empleado):
        modulos.__init__(self, Id_modulo, Nombre, Nivel_requerido)
        tipoEmpleado.__init__(self, Id_tipo_empleado, Tipo, Permiso, Desc_empleado)
        self._Id_acceso = Id_acceso
        self._registro_accesos = []  # Lista para almacenar el historial de accesos

    def validar_acceso(self):
        """Valida si el tipo de empleado tiene suficiente permiso para acceder al módulo"""
        try:
            if not isinstance(self._Permiso, (int, float)):
                return False, "El nivel de permiso debe ser un valor numérico"
            
            if not isinstance(self.Nivel_requerido, (int, float)):
                return False, "El nivel requerido debe ser un valor numérico"
            
            if self._Permiso >= self.Nivel_requerido:
                return True, "Acceso permitido"
            else:
                return False, f"Acceso denegado: permiso insuficiente (Requiere nivel {self.Nivel_requerido})"
        except Exception as e:
            return False, f"Error al validar acceso: {str(e)}"
    
    def registrar_acceso(self, fecha=None, exitoso=None):
        """Registra el intento de acceso al módulo"""
        from datetime import datetime
        
        # Si no se proporciona fecha, usar la fecha actual
        if fecha is None:
            fecha = datetime.now()
            
        # Validar acceso si no se proporciona el parámetro exitoso
        if exitoso is None:
            exitoso, mensaje = self.validar_acceso()
        else:
            mensaje = "Acceso permitido" if exitoso else "Acceso denegado"

        # Crear registro de acceso
        registro = {
            'id_acceso': self._Id_acceso,
            'id_modulo': self._Id_modulo,
            'id_tipo_empleado': self._Id_tipo_empleado,
            'fecha': fecha,
            'exitoso': exitoso,
            'mensaje': mensaje
        }
        
        # Agregar el registro al historial
        self._registro_accesos.append(registro)
        
        return exitoso, mensaje

    def obtener_historial_accesos(self):
        """Retorna el historial de accesos"""
        if not self._registro_accesos:
            return [], "No hay registros de acceso"
        return self._registro_accesos, f"Total de registros: {len(self._registro_accesos)}"

    def limpiar_historial(self):
        """Limpia el historial de accesos"""
        self._registro_accesos = []
        return True, "Historial de accesos limpiado exitosamente"

    def __str__(self):
        """Representación en string de la clase Accesos"""
        return f"Acceso ID: {self._Id_acceso}, Módulo: {self._Nombre}, Nivel requerido: {self.Nivel_requerido}"