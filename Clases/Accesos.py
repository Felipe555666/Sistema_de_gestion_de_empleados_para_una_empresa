from Modulos import modulos
from Tipo_empleado import tipoEmpleado

class Accesos(modulos, tipoEmpleado):
    def __init__(self,Id_acceso,Id_modulo,Id_empleado):
        tipoEmpleado.__init__(self, Id_empleado)
        modulos.__init__(self, Id_modulo)
        self._Id_acceso = Id_acceso

    
    def validar_acceso(self):
        #Verifica si el empleado tiene el permiso adecuado para acceder al módulo.
        if self._Permiso >= self.Nivel_requerido:
            return True, "Acceso permitido"
        else:
            return False, "Acceso denegado: permiso insuficiente"
    
    def registrar_acceso(self):
        #Registra el acceso al módulo si la validación es exitosa.
        # Validar acceso antes de registrar
        acceso_valido, mensaje = self.validar_acceso()
        if acceso_valido:
            # Simulación de registro de acceso (podría almacenarse en una base de datos)
            return True, f"Acceso registrado correctamente para el empleado con ID {self._Id_acceso}"
        else:
            return False, mensaje