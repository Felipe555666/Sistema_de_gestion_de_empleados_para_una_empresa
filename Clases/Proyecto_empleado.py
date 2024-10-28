from Empleado import empleado
from Proyecto import proyecto

class proyectoEmpleado(empleado, proyecto):
    def __init__(self,Id_pro_empleado,Id_proyecto,Id_empleado):
        empleado.__init__(self, Id_empleado)
        proyecto.__init__(self, Id_proyecto)
        self._Id_pro_empleado = Id_pro_empleado
    
