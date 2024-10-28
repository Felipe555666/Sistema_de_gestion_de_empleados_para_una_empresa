from cryptography.fernet import Fernet
from datetime import datetime
from Tipo_empleado import tipoEmpleado

class empleado(tipoEmpleado):
    def __init__(self,Id_empleado,Id_tipo_empleado,Nombre,Direccion,Telefono,Correo,Fecha_inicio,Salario,Fecha_nac,Contrasena,Estado_empleado):
        super().__init__(Id_tipo_empleado)
        self._Id_empleado = Id_empleado
        self.Nombre = Nombre
        self._Direccion = Direccion
        self._Telefono = Telefono
        self._Correo = Correo
        self._Fecha_inicio = Fecha_inicio
        self._Salario = Salario
        self._Fecha_nac = Fecha_nac
        self._Estado_empleado = Estado_empleado
        self.__Contrasena = Contrasena
        self.clave = Fernet.generate_key()
        self.cipher_suite = Fernet(self.clave)
        

        
    def validar_datos(self):
        # Asegura que el campo no este vacío
        if not self.Nombre:
            return False, "El campo no puede estar vacío."
        
        # valida que el correo tenga un formato básico
        if "@" not in self._Correo or "." not in self._Correo:
            return False, "El correo debe tener un formato basico de un correo electronico"
        
        # Hace que el Salario del empleado sea numerico positivo, entero o decimal y que no sea mayor o igual a 0
        if not isinstance(self._Salario, (int, float)) or self._Salario <= 0:
            return False, "El salario del empleado debe ser un numero positivo y mayor a 0"
        
        return True, "Los datos dados son validos"
    
    def validar_fechas(self):

        formato_fecha = "%Y-%m-%d" # el formato será Año-Mes-Dia por formato de datetime

        #valida que el formato de la fecha de nacimiento este en el correcto
        try:
            fecha_nacimiento = datetime.strptime(self._Fecha_nac, formato_fecha)
        except ValueError:
            return False, "La fecha nacimiento no esta en el formato indicado"
        
        # valida que el formato de la fecha de inicio sea valido
        try:
            fecha_inicio = datetime.strptime(self._Fecha_inicio, formato_fecha)
        except ValueError:
            return False, "La fecha de inicio no esta en el formato valido."
        
        #verifica que la fecha de inicio no sea menor o igual a la fecha de nac
        if fecha_inicio <= fecha_nacimiento:
            return False, "La fecha de inicio no puede ser menor a la fecha de nac."
        
        #la fecha de nacimiento no puede estar en el "futuro"
        fecha_actual = datetime.now()
        if fecha_nacimiento > fecha_actual:
            return False, "la fecha de nacimiento no puede estar despues que la fecha actual"
        if fecha_inicio > fecha_actual:
            return False, "la fecha de inicio no puede estar despues que la fecha actual"
        
        return True, "Las fechas son validas"
    
    def encriptar_contrasena(self):
        self.__Contrasena = self.cipher_suite.encrypt(self.__Contrasena.encode())
        return self.__Contrasena
    
    def desencriptar_contrasena(self):
        contrasena_desencriptar = self.cipher_suite.decrypt(self.__Contrasena).decode()
        return contrasena_desencriptar
    
    def registrar_empleado(self):
        datos_validos, mensaje_datos = self.validar_datos()
        if not datos_validos:
            return False, f"Error en la validación de datos: {mensaje_datos}"
        
        fechas_validas, mensaje_fechas = self.validar_fechas()
        if not fechas_validas:
            return False, f"Error en la validación de fechas: {mensaje_fechas}"
        
        # Encriptar la contraseña antes de almacenar
        self.encriptar_contrasena()
        
        # Aquí podrías agregar la lógica para almacenar el empleado en una base de datos o en otro almacenamiento.
        # Por ahora, solo simularemos que el empleado fue registrado exitosamente.
        
        return True, f"Empleado {self.Nombre} registrado exitosamente."