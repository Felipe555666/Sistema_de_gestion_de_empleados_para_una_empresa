import mysql.connector.errors
from Obtener_conexion import obtener_conexion
from mysql.connector import Error
from cryptography.fernet import Fernet
from datetime import datetime
from Tipo_empleado import tipoEmpleado

class empleado(tipoEmpleado):
    def __init__(self,Id_empleado,Rut,Id_tipo_empleado,Nombre,Direccion,Telefono,Correo,Fecha_inicio,Salario,Fecha_nac,Contrasena,Estado_empleado):
        super().__init__(Id_tipo_empleado)
        self._Id_empleado = Id_empleado
        self.__Rut = Rut
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
    
    @property
    def Nombre(self):
        return self.Nombre

    @Nombre.setter
    def Nombre(self, nuevo_nombre):
        self.Nombre = nuevo_nombre

    @property
    def Direccion(self):
        return self._Direccion

    @Direccion.setter
    def Direccion(self, nueva_direccion):
        self._Direccion = nueva_direccion

    @property
    def Telefono(self):
        return self._Telefono

    @Telefono.setter
    def Telefono(self, nuevo_telefono):
        self._Telefono = nuevo_telefono

    @property
    def Correo(self):
        return self._Correo

    @Correo.setter
    def Correo(self, nuevo_correo):
        self._Correo = nuevo_correo

    @property
    def Fecha_inicio(self):
        return self._Fecha_inicio
    @Fecha_inicio.setter
    def Fecha_inicio(self, nueva_fecha):
        self._Fecha_inicio = nueva_fecha

    @property
    def Salario(self):
        return self._Salario

    @Salario.setter
    def Salario(self, nuevo_salario):
        self._Salario = nuevo_salario

    @property
    def Id_tipo_empleado(self):
        return self._Id_tipo_empleado

    @Id_tipo_empleado.setter
    def tipo_empleado(self, nuevo_tipo):
        self._Id_tipo_empleado = nuevo_tipo

    @property
    def Contrasena(self):
        return self.__Contrasena
    
    @Contrasena.setter
    def Contrasena(self, nueva_contrasena):
        self.__Contrasena = nueva_contrasena

    @property
    def Estado_empleado(self):
        return self._Estado_empleado
    
    @Estado_empleado.setter
    def Estado_empleado(self, nuevo_estado):
        self._Estado_empleado = nuevo_estado
    
    def obtener_detalles(self):
        return f"ID: {self._Id_empleado}, Rut: {self.__Rut}, Nombre: {self.Nombre}, Dirección: {self._Direccion}, Teléfono: {self._Telefono}, Correo: {self._Correo}, Fecha de inicio: {self._Fecha_inicio}, Salario: {self._Salario}, Tipo: {self._Id_tipo_empleado}, Estado: {self._Estado_empleado}"
    
    def guardar_en_db(self, conexion):
        cursor = conexion.cursor()
        try:
            query = """
            INSERT INTO Empleado (Nombre, Rut, Direccion, Telefono, Correo, Fecha_inicio, Salario, Id_tipo_empleado, Estado_empleado)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores = (self.Nombre, self._Direccion, self._Telefono, self._Correo, self._Fecha_inicio, self._Salario, self._Id_tipo_empleado, self._Estado_empleado)
            cursor.execute(query, valores)
            conexion.commit()
            self.__id_empleado = cursor.lastrowid
            print(f"Empleado {self.Nombre} ha sido guardado en la base de datos con ID {self.__id_empleado}.")
        except mysql.connector.Error as err:
            print(f"Error al guardar el empleado: {err}")
        finally:
            cursor.close()

    @classmethod
    def obtener_por_id(cls, conexion, id_empleado):
        cursor = conexion.cursor()
        query = "SELECT * FROM Empleado WHERE id = %s"
        cursor.execute(query, (id_empleado,))
        resultado = cursor.fetchone()
        cursor.close()

    @classmethod
    def obtener_por_id(cls, conexion, id_empleado):
        cursor = conexion.cursor()
        query = "SELECT * FROM Empleado WHERE id = %s"
        cursor.execute(query, (id_empleado,))
        resultado = cursor.fetchone()
        cursor.close()

        if resultado:
            return cls(
                Nombre=resultado[1],
                Direccion=resultado[2],
                Telefono=resultado[3],
                Correo=resultado[4],
                Fecha_inicio=resultado[5],
                Salario=resultado[6],
                Id_tipo_empleado=resultado[7], 
                id_empleado=resultado[0]
            )
        else:
            return None
        
    def actualizar_en_db(self, conexion):
        cursor = conexion.cursor()
        query = """
        UPDATE Empleado SET Nombre = %s, Direccion = %s, Telefono = %s, Correo = %s, Fecha_inicio = %s, Salario = %s, Id_tipo_empleado = %s
        WHERE id_empleado = %s
        """
        valores = (self.Nombre, self._Direccion, self._Telefono, self._Correo, self._Fecha_inicio, self._Salario, self._Id_tipo_empleado, self.__id_empleado)
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        print(f"Empleado {self.Nombre} ha sido actualizado en la base de datos.")