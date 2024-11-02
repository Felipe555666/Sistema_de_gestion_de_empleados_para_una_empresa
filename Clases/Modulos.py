class modulos:
    def __init__(self, Id_modulo=None, Nombre=None, Nivel_requerido=None):
        self._Id_modulo = Id_modulo
        self._Nombre = Nombre
        self._Nivel_requerido = Nivel_requerido

    def validar_modulo(self):
        """Valida los datos del módulo"""
        try:
            if not isinstance(self._Id_modulo, str) or not self._Id_modulo:
                return False, "El ID del módulo debe ser una cadena no vacía"
            
            if not isinstance(self._Nombre, str) or not self._Nombre:
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
        """Valida si el nivel del usuario es suficiente para acceder al módulo"""
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

    def actualizar_modulo(self, nombre=None, nivel_requerido=None):
        """Actualiza la información del módulo"""
        if nombre:
            self._Nombre = nombre
        if nivel_requerido is not None:
            self._Nivel_requerido = nivel_requerido
        
        validacion, mensaje = self.validar_modulo()
        if not validacion:
            return False, mensaje
        
        return True, "Módulo actualizado correctamente"

    def __str__(self):
        """Representación en string del módulo"""
        return f"Módulo: {self._Nombre} (ID: {self._Id_modulo}, Nivel requerido: {self._Nivel_requerido})"