class tipoEmpleado:
    def __init__(self, Id_tipo_empleado, Tipo, Permiso, Desc_empleado):
        self._Id_tipo_empleado = Id_tipo_empleado
        self._Tipo = Tipo
        self._Permiso = Permiso
        self._Desc_empleado = Desc_empleado

    def validar_tipo_empleado(self):
        """Valida los datos del tipo de empleado"""
        try:
            if not isinstance(self._Id_tipo_empleado, int) or self._Id_tipo_empleado <= 0:
                return False, "El ID del tipo de empleado debe ser un número entero positivo"
            
            if not isinstance(self._Tipo, str) or not self._Tipo.strip():
                return False, "El tipo debe ser una cadena no vacía"
            
            if not isinstance(self._Permiso, int) or self._Permiso < 0 or self._Permiso > 10:
                return False, "El permiso debe ser un número entero entre 0 y 10"
            
            if not isinstance(self._Desc_empleado, str):
                return False, "La descripción debe ser una cadena"
            
            return True, "Datos del tipo de empleado válidos"
        except Exception as e:
            return False, f"Error en la validación del tipo de empleado: {str(e)}"

    def actualizar_tipo_empleado(self, Tipo=None, Permiso=None, Desc_empleado=None):
        """Actualiza los datos del tipo de empleado"""
        try:
            if Tipo is not None:
                self._Tipo = Tipo
            if Permiso is not None:
                self._Permiso = Permiso
            if Desc_empleado is not None:
                self._Desc_empleado = Desc_empleado

            validacion, mensaje = self.validar_tipo_empleado()
            if not validacion:
                return False, mensaje

            return True, "Los datos del tipo de empleado han sido actualizados exitosamente"
        except Exception as e:
            return False, f"Error al actualizar el tipo de empleado: {str(e)}"

    def get_permiso(self):
        """Retorna el nivel de permiso del tipo de empleado"""
        return self._Permiso

    def obtener_informacion_tipo_empleado(self):
        """Retorna la información básica del tipo de empleado"""
        return {
            'ID': self._Id_tipo_empleado,
            'Tipo': self._Tipo,
            'Permiso': self._Permiso,
            'Descripción': self._Desc_empleado
        }

    def __str__(self):
        """Representación en string del tipo de empleado"""
        return f"Tipo Empleado: {self._Tipo} (ID: {self._Id_tipo_empleado}, Permiso: {self._Permiso})"


class modulos:
    def __init__(self, Id_modulo, Nombre, Nivel_requerido):
        self._Id_modulo = Id_modulo
        self._Nombre = Nombre
        self._Nivel_requerido = Nivel_requerido

    def validar_modulo(self):
        """Valida los datos del módulo"""
        try:
            if not isinstance(self._Id_modulo, int) or self._Id_modulo <= 0:
                return False, "El ID del módulo debe ser un número entero positivo"
            
            if not isinstance(self._Nombre, str) or not self._Nombre.strip():
                return False, "El nombre del módulo debe ser una cadena no vacía"
            
            if not isinstance(self._Nivel_requerido, int) or self._Nivel_requerido < 0:
                return False, "El nivel requerido debe ser un número entero no negativo"
            
            return True, "Datos del módulo válidos"
        except Exception as e:
            return False, f"Error en la validación del módulo: {str(e)}"

    def get_nivel_requerido(self):
        """Retorna el nivel requerido del módulo"""
        return self._Nivel_requerido
    
    def validar_nivel(self, nivel_usuario):
        """Valida si el nivel del usuario es suficiente para el módulo"""
        try:
            if not isinstance(nivel_usuario, int):
                return False, "El nivel del usuario debe ser un número entero"
            
            if nivel_usuario >= self._Nivel_requerido:
                return True, "Nivel de acceso suficiente"
            else:
                return False, f"Nivel insuficiente. Se requiere nivel {self._Nivel_requerido}"
        except Exception as e:
            return False, f"Error en la validación del nivel: {str(e)}"

    def obtener_informacion_modulo(self):
        """Retorna la información básica del módulo"""
        return {
            'ID': self._Id_modulo,
            'Nombre': self._Nombre,
            'Nivel Requerido': self._Nivel_requerido
        }

    def __str__(self):
        """Representación en string del módulo"""
        return f"Módulo: {self._Nombre} (ID: {self._Id_modulo}, Nivel Requerido: {self._Nivel_requerido})"