from cryptography.fernet import Fernet
from datetime import datetime
from Tipo_empleado import tipoEmpleado

class empleado(tipoEmpleado):
    def __init__(self, Id_empleado, Id_tipo_empleado, Tipo, Permiso, Desc_empleado):
        super().__init__(Id_tipo_empleado, Tipo, Permiso, Desc_empleado)
        self._Id_empleado = Id_empleado
        self._Nombre = None
        self._Direccion = None
        self._Telefono = None
        self._Correo = None
        self._Fecha_inicio = None
        self._Salario = None
        self._Fecha_nac = None
        self._Estado_empleado = True
        self.__Contrasena = None
        self._clave = Fernet.generate_key()
        self._cipher_suite = Fernet(self._clave)

    def establecer_datos_personales(self, Nombre, Direccion, Telefono, Correo, 
                                    Fecha_inicio, Salario, Fecha_nac, Contrasena):
        self._Nombre = Nombre
        self._Direccion = Direccion
        self._Telefono = Telefono
        self._Correo = Correo
        self._Fecha_inicio = Fecha_inicio
        self._Salario = Salario
        self._Fecha_nac = Fecha_nac
        self.__Contrasena = Contrasena

    def validar_datos(self):
        if not all([self._Nombre, self._Direccion, self._Telefono, self._Correo,
                    self._Fecha_inicio, self._Fecha_nac, self.__Contrasena]):
            return False, "Todos los campos son obligatorios"
        
        if "@" not in self._Correo or "." not in self._Correo:
            return False, "El correo debe tener un formato válido"
        
        if not isinstance(self._Salario, (int, float)) or self._Salario <= 0:
            return False, "El salario debe ser un número positivo"
        
        if not str(self._Telefono).isdigit():
            return False, "El teléfono debe contener solo números"

        return True, "Los datos son válidos"

    def validar_fechas(self):
        formato_fecha = "%Y-%m-%d"
        try:
            fecha_nacimiento = datetime.strptime(self._Fecha_nac, formato_fecha)
            fecha_inicio = datetime.strptime(self._Fecha_inicio, formato_fecha)
            fecha_actual = datetime.now()

            if fecha_inicio <= fecha_nacimiento:
                return False, "La fecha de inicio no puede ser anterior a la fecha de nacimiento"
            
            if fecha_nacimiento > fecha_actual or fecha_inicio > fecha_actual:
                return False, "Las fechas no pueden ser futuras"

            return True, "Las fechas son válidas"
        except ValueError:
            return False, "Las fechas deben tener el formato YYYY-MM-DD"

    def encriptar_contrasena(self):
        if self.__Contrasena:
            self.__Contrasena = self._cipher_suite.encrypt(self.__Contrasena.encode())
            return True, "Contraseña encriptada correctamente"
        return False, "No hay contraseña para encriptar"

    def desencriptar_contrasena(self):
        if self.__Contrasena:
            return True, self._cipher_suite.decrypt(self.__Contrasena).decode()
        return False, "No hay contraseña para desencriptar"

    def obtener_informacion_empleado(self):
        return {
            'ID': self._Id_empleado,
            'Nombre': self._Nombre,
            'Correo': self._Correo,
            'Teléfono': self._Telefono,
            'Fecha Inicio': self._Fecha_inicio,
            'Estado': "Activo" if self._Estado_empleado else "Inactivo"
        }

    def cambiar_estado(self, nuevo_estado):
        if isinstance(nuevo_estado, bool):
            self._Estado_empleado = nuevo_estado
            return True, f"Estado cambiado a {'activo' if nuevo_estado else 'inactivo'}"
        return False, "El estado debe ser un valor booleano"

    def __str__(self):
        return f"Empleado: {self._Nombre} (ID: {self._Id_empleado})"