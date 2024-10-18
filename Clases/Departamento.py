from Empleado import empleado

class departamento(empleado):
    def __init__(self,Id_departamento,Nombre,Telefono,Id_empleado):
        super().__init__(self, Id_empleado)
        self._Id_departamento = Id_departamento
        self._Nombre = Nombre
        self._Telefono = Telefono