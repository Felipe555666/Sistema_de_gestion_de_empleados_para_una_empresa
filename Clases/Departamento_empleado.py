from Departamento import Departamento
from Empleado import Empleado

class Departamento_empleado(Departamento, Empleado):
    def __init__(self,Id_dep_empleado,Id_departamento,Id_empleado):
        Departamento.__init__(self, Id_departamento)
        Empleado.__init__(self, Id_empleado)
        self._Id_dep_empleado = Id_dep_empleado
