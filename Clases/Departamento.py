from Empleado import empleado

class departamento(empleado):
    def __init__(self,Id_departamento,Nombre,Telefono,Id_empleado):
        # Primero, necesitamos corregir la llamada al constructor padre
        # y agregar todos los parámetros requeridos por la clase empleado
        super().__init__(
            Id_empleado=Id_empleado,
            Id_tipo_empleado=None,  # Agregar valor apropiado
            Nombre=Nombre,
            Direccion='',  # Agregar valor apropiado
            Telefono=Telefono,
            Correo='',  # Agregar valor apropiado
            Fecha_inicio='',  # Agregar valor apropiado
            Salario=0,  # Agregar valor apropiado
            Fecha_nac='',  # Agregar valor apropiado
            Contrasena='',  # Agregar valor apropiado
            Estado_empleado=True  # Agregar valor apropiado
        )
        
        # Atributos propios de departamento
        self._Id_departamento = Id_departamento
        self._Nombre = Nombre
        self._Telefono = Telefono
        self._empleados = []  # Lista para almacenar los empleados del departamento
        
    def validar_departamento(self):
        """Método para validar los datos del departamento"""
        if not self._Nombre:
            return False, "El nombre del departamento no puede estar vacío"
        
        if not self._Telefono:
            return False, "El teléfono del departamento no puede estar vacío"
        
        # Validar formato del teléfono
        if not str(self._Telefono).isdigit():
            return False, "El teléfono debe contener solo números"
        
        return True, "Datos del departamento válidos"

    def agregar_empleado(self, empleado):
        """Método para agregar un empleado al departamento"""
        # Validar que el parámetro sea una instancia de empleado
        if not isinstance(empleado, empleado):
            return False, "El objeto proporcionado no es un empleado válido"
        
        if empleado not in self._empleados:
            self._empleados.append(empleado)
            return True, f"Empleado {empleado.Nombre} agregado al departamento {self._Nombre}"
        return False, "El empleado ya está en este departamento"
    
    def remover_empleado(self, empleado):
        """Método para remover un empleado del departamento"""
        if empleado in self._empleados:
            self._empleados.remove(empleado)
            return True, f"Empleado {empleado.Nombre} removido del departamento {self._Nombre}"
        return False, "El empleado no está en este departamento"
    
    def listar_empleados(self):
        """Método para obtener la lista de empleados"""
        if not self._empleados:
            return [], "No hay empleados en este departamento"
        return self._empleados, f"Total de empleados: {len(self._empleados)}"
    
    def obtener_informacion_departamento(self):
        """Método para obtener información del departamento"""
        return {
            'ID': self._Id_departamento,
            'Nombre': self._Nombre,
            'Teléfono': self._Telefono,
            'Cantidad de empleados': len(self._empleados)
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
