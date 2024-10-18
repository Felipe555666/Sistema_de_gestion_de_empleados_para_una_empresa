from Empleado import empleado

class informe(empleado):
    def __init__(self,Id_informe,Nombre_informe,Fecha_creacion,Id_empleado):
        super().__init__(self, Id_empleado)
        self._Id_informe = Id_informe
        self._Nombre_informe = Nombre_informe
        self._Fecha_creacion = Fecha_creacion
