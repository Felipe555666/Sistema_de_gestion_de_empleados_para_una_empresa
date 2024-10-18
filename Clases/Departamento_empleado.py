from Departamento import departamento
from Empleado import empleado

class departamento_empleado(departamento, empleado):
    def __init__(self,Id_dep_empleado,Id_departamento,Id_empleado):
        departamento.__init__(self, Id_departamento)
        empleado.__init__(self, Id_empleado)
        self._Id_dep_empleado = Id_dep_empleado
