from Empleado import empleado

class departamento(empleado):
    def __init__(self, Id_departamento, Nombre, Telefono, Id_empleado, Id_tipo_empleado, 
                 Tipo, Permiso, Desc_empleado):
        # Llamada al constructor de la clase padre (empleado)
        super().__init__(Id_empleado, Id_tipo_empleado, Tipo, Permiso, Desc_empleado)
        
        # Atributos propios de departamento
        self._Id_departamento = Id_departamento
        self._Nombre = Nombre
        self._Telefono = Telefono
        
    def validar_departamento(self):
        """Método para validar los datos del departamento"""
        try:
            # Validar ID del departamento
            if not isinstance(self._Id_departamento, int) or self._Id_departamento <= 0:
                return False, "El ID del departamento debe ser un número entero positivo"
            
            # Validar nombre
            if not self._Nombre or not isinstance(self._Nombre, str):
                return False, "El nombre del departamento no puede estar vacío y debe ser texto"
            
            # Validar teléfono
            if not self._Telefono:
                return False, "El teléfono del departamento no puede estar vacío"
            
            # Validar formato del teléfono (solo números)
            if not str(self._Telefono).isdigit():
                return False, "El teléfono debe contener solo números"
            
            return True, "Datos del departamento válidos"
        except Exception as e:
            return False, f"Error en la validación: {str(e)}"

    def obtener_informacion_departamento(self):
        """Método para obtener información del departamento"""
        return {
            'ID': self._Id_departamento,
            'Nombre': self._Nombre,
            'Teléfono': self._Telefono,
            'ID_Empleado': self._Id_empleado
        }
    
    def actualizar_informacion(self, nombre=None, telefono=None):
        """Método para actualizar la información del departamento"""
        if nombre:
            self._Nombre = nombre
        if telefono:
            self._Telefono = telefono
            
        # Validar los nuevos datos
        validacion, mensaje = self.validar_departamento()
        if not validacion:
            return False, mensaje
        
        return True, "Información del departamento actualizada correctamente"

    def __str__(self):
        """Representación en string del departamento"""
        return f"Departamento: {self._Nombre} (ID: {self._Id_departamento})"