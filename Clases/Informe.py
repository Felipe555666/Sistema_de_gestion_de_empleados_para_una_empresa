from datetime import datetime
from Empleado import empleado

class informe(empleado):
    def __init__(self, Id_informe, Nombre_informe, Fecha_creacion, Id_empleado, Estado_informe, Id_tipo_empleado, Tipo, Permiso, Desc_empleado):
        super().__init__(Id_empleado, Id_tipo_empleado, Tipo, Permiso, Desc_empleado)
        self._Id_informe = Id_informe
        self._Nombre_informe = Nombre_informe
        self._Fecha_creacion = Fecha_creacion
        self._Estado_informe = Estado_informe

    def validar_informe(self):
        """Valida los datos del informe"""
        try:
            if not isinstance(self._Id_informe, int) or self._Id_informe <= 0:
                return False, "El ID del informe debe ser un número entero positivo"
            
            if not self._Nombre_informe or not isinstance(self._Nombre_informe, str):
                return False, "El nombre del informe no puede estar vacío y debe ser texto"
            
            if not self._Estado_informe or not isinstance(self._Estado_informe, str):
                return False, "El estado del informe no puede estar vacío y debe ser texto"
            
            fecha_valida, mensaje = self.validar_fecha_creacion()
            if not fecha_valida:
                return False, mensaje
            
            return True, "Datos del informe válidos"
        except Exception as e:
            return False, f"Error en la validación del informe: {str(e)}"

    def validar_fecha_creacion(self):
        """Valida la fecha de creación del informe"""
        formato_fecha = "%Y-%m-%d"
        try:
            fecha_creacion = datetime.strptime(self._Fecha_creacion, formato_fecha)
            fecha_actual = datetime.now()
            
            if fecha_creacion > fecha_actual:
                return False, "La fecha de creación no puede estar en el futuro"
            
            return True, "La fecha de creación es válida"
        except ValueError:
            return False, "La fecha de creación no está en el formato correcto (YYYY-MM-DD)"
        except Exception as e:
            return False, f"Error en la validación de la fecha: {str(e)}"

    def obtener_informacion_informe(self):
        """Retorna la información básica del informe"""
        return {
            'ID': self._Id_informe,
            'Nombre': self._Nombre_informe,
            'Fecha de Creación': self._Fecha_creacion,
            'Estado': self._Estado_informe,
            'ID Empleado': self._Id_empleado
        }

    def actualizar_informe(self, nombre=None, estado=None):
        """Actualiza la información del informe"""
        if nombre:
            self._Nombre_informe = nombre
        if estado:
            self._Estado_informe = estado
        
        validacion, mensaje = self.validar_informe()
        if not validacion:
            return False, mensaje
        
        return True, "Informe actualizado correctamente"

    def __str__(self):
        """Representación en string del informe"""
        return f"Informe: {self._Nombre_informe} (ID: {self._Id_informe})"