from Proyecto_empleado import proyectoEmpleado
from datetime import datetime

class registroTiempo(proyectoEmpleado):
    def __init__(self, Id_reg_tiempo, Id_pro_empleado, Id_proyecto, Id_empleado, 
                 Nombre, Descripcion, Fecha_inicio, Fecha_fin):
        super().__init__(Id_pro_empleado, Id_proyecto, Id_empleado, 
                        Nombre, Descripcion, Fecha_inicio, Fecha_fin)
        self._Id_reg_tiempo = Id_reg_tiempo
        self._horas_trabajadas = 0
        self._registros = []  # Lista para almacenar el historial de registros

    def validar_registro(self):
        """Valida los datos del registro de tiempo"""
        try:
            if not isinstance(self._Id_reg_tiempo, int) or self._Id_reg_tiempo <= 0:
                return False, "El ID de registro debe ser un número entero positivo"
            
            # Validar la asignación proyecto-empleado
            validacion_asignacion, mensaje = self.validar_proyecto_empleado()
            if not validacion_asignacion:
                return False, mensaje
            
            return True, "Datos del registro válidos"
        except Exception as e:
            return False, f"Error en la validación del registro: {str(e)}"

    def validar_horas(self, horas):
        """Valida que las horas tengan un formato apropiado"""
        try:
            if not isinstance(horas, (int, float)):
                return False, "Las horas trabajadas deben estar en formato numérico"
            
            if horas < 0 or horas > 24:
                return False, "Las horas deben estar en un rango de 0 a 24"
            
            return True, "Las horas son válidas"
        except Exception as e:
            return False, f"Error en la validación de horas: {str(e)}"
    
    def registro_horas(self, horas, fecha=None):
        """Registra las horas trabajadas con fecha"""
        try:
            # Validar las horas
            es_valido, mensaje = self.validar_horas(horas)
            if not es_valido:
                return False, mensaje

            # Si no se proporciona fecha, usar la fecha actual
            if fecha is None:
                fecha = datetime.now().strftime("%Y-%m-%d")

            # Crear registro
            registro = {
                'fecha': fecha,
                'horas': horas,
                'id_empleado': self._Id_empleado,
                'id_proyecto': self._Id_proyecto
            }

            # Agregar al historial y actualizar total
            self._registros.append(registro)
            self._horas_trabajadas += horas

            return True, f"Se han registrado {horas} horas correctamente"
        except Exception as e:
            return False, f"Error al registrar horas: {str(e)}"
        
    def obtener_total_horas(self):
        """Retorna el total de horas trabajadas"""
        return self._horas_trabajadas
    
    def obtener_registros(self):
        """Retorna el historial de registros"""
        if not self._registros:
            return False, "No hay registros de tiempo"
        return True, self._registros

    def obtener_horas_por_fecha(self, fecha):
        """Obtiene las horas trabajadas en una fecha específica"""
        try:
            horas_fecha = sum(registro['horas'] for registro in self._registros 
                            if registro['fecha'] == fecha)
            return True, horas_fecha
        except Exception as e:
            return False, f"Error al obtener horas por fecha: {str(e)}"

    def reiniciar_contador(self):
        """Reinicia el contador de horas trabajadas"""
        try:
            self._horas_trabajadas = 0
            return True, "Contador de horas reiniciado correctamente"
        except Exception as e:
            return False, f"Error al reiniciar contador: {str(e)}"

    def obtener_informacion_registro(self):
        """Retorna la información básica del registro de tiempo"""
        return {
            'ID Registro': self._Id_reg_tiempo,
            'ID Proyecto-Empleado': self._Id_pro_empleado,
            'ID Empleado': self._Id_empleado,
            'ID Proyecto': self._Id_proyecto,
            'Total Horas': self._horas_trabajadas,
            'Cantidad Registros': len(self._registros)
        }

    def __str__(self):
        """Representación en string del registro de tiempo"""
        return (f"Registro Tiempo ID: {self._Id_reg_tiempo} - "
                f"Total Horas: {self._horas_trabajadas}")


    def registrar_horas(self):
        id_emp = int(input("Ingrese el ID del empleado: "))
        id_proy = int(input("Ingrese el ID del proyecto: "))
        horas = float(input("Ingrese las horas trabajadas: "))
        fecha = input("Ingrese la fecha (YYYY-MM-DD) o deje en blanco para hoy: ")
        
        if not fecha:
            fecha = datetime.now().strftime("%Y-%m-%d")
        
        if id_emp in self.empleados and id_proy in self.proyectos:
            registro = registroTiempo(self.id_registro, 0, id_proy, id_emp, "", "", "", "")
            resultado, mensaje = registro.registro_horas(horas, fecha)