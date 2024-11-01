from Empleado import empleado

class departamento(empleado):
    def __init__(self,Id_departamento,Nombre,Telefono,Id_empleado):
        super().__init__(self, Id_empleado)
        self._Id_departamento = Id_departamento
        self._Nombre = Nombre
        self._Telefono = Telefono
        self.__empleados_asignados = []

 # Agrega un empleado al departamento
    def agregar_empleado(self, empleado):
        self.__empleados_asignados.append(empleado)

    # Lista los empleados asignados al departamento
    def listar_empleados(self):
        print(f"Departamento: {self._Nombre}")
        for empleado in self.__empleados_asignados:
            print(empleado.obtener_detalles())
    