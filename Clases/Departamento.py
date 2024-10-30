from Empleado import empleado

class departamento(empleado):
    def __init__(self,Id_departamento,Nombre,Telefono,Id_empleado):
        super().__init__(self, Id_empleado)
        self._Id_departamento = Id_departamento
        self._Nombre = Nombre
        self._Telefono = Telefono
        
    def agregar_empleado(self, empleado):
        if empleado not in self._empleados:
            self._empleados.append(empleado)
            return True, f"Empleado {empleado.Nombre} agregado al departamento {self._Nombre}"
        return False, "El empleado ya está en este departamento"
    
    def remover_empleado(self, empleado):
        if empleado in self._empleados:
            self._empleados.remove(empleado)
            return True, f"Empleado {empleado.Nombre} removido del departamento {self._Nombre}"
        return False, "El empleado no está en este departamento"
    
    def listar_empleados(self):
        return self._empleados
