from Modulos import modulos
from Tipo_empleado import tipoEmpleado

class Accesos(modulos, tipoEmpleado):
    def __init__(self,Id_acceso,Id_modulo,Id_empleado):
        tipoEmpleado.__init__(self, Id_empleado)
        modulos.__init__(self, Id_modulo)
        self._Id_acceso = Id_acceso
        