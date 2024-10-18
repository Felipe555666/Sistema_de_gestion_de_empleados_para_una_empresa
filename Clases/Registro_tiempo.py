from Proyecto_empleado import proyectoEmpleado

class registroTiempo(proyectoEmpleado):
    def __init__(self,Id_reg_tiempo,Id_pro_empleado,Nombre,Direccion,Telefono,Correo,Fecha_inicio,Salario):
        super().__init__(self, Id_pro_empleado)
        self._Id_reg_tiempo = Id_reg_tiempo
        self._Nombre = Nombre
        self._Direccion = Direccion
        self._Telefono = Telefono
        self._Correo = Correo
        self._Fecha_inicio = Fecha_inicio
        self._Salario = Salario
        