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
        self._horas_trabajadas = 0

    def validar_horas(self, horas): # valida que las horas tengan un formato apropiado
        if not isinstance(horas, (int, float)):
            return False, "Las horas trabajas deben estar en formato numerico"
        
        if horas < 0 or horas > 24:
            return False, "Las horas tienen que estar en un rango de 0 a 24"
        
        return True, "Las horas son validas"
    
    def registro_horas(self, horas): 
        # valida las horas antes de ser registradas
        es_valido, mensaje = self.validar_horas(horas)
        if es_valido:
            self._horas_trabajadas += horas
            return True, f"Se han registrado {horas} horas correctamente"
        else:
            return False, mensaje