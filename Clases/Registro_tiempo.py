from Proyecto_empleado import proyectoEmpleado
from datetime import datetime

class registroTiempo(proyectoEmpleado):
    def __init__(self, Id_reg_tiempo=None, Id_pro_empleado=None, Id_proyecto=None, 
                 Id_empleado=None, Nombre=None, Descripcion=None, Fecha_inicio=None, 
                 Fecha_fin=None):
        super().__init__(Id_pro_empleado, Id_proyecto, Id_empleado, 
                        Nombre, Descripcion, Fecha_inicio, Fecha_fin)
        self._Id_reg_tiempo = Id_reg_tiempo
        self._horas_trabajadas = 0

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
        
    def obtener_total_horas(self, mydb):
        """Retorna el total de horas trabajadas desde la base de datos"""
        try:
            cursor = mydb.cursor()
            id_emp = int(input("Ingrese el ID del empleado: "))
            
            # Consulta SQL para obtener el total de horas
            sql = """
            SELECT SUM(rt.horas_trabajadas) as total_horas
            FROM registroTiempo rt
            JOIN proyectoEmpleado pe ON rt.Id_pro_empleado = pe.Id_pro_empleado
            WHERE pe.Id_empleado = %s
            """
            cursor.execute(sql, (id_emp,))
            resultado = cursor.fetchone()
            
            if resultado and resultado[0]:
                print(f"\nTotal de horas trabajadas: {resultado[0]} horas")
                return True, resultado[0]
            else:
                print("No hay registros de horas para este empleado")
                return False, 0
                
        except Exception as e:
            print(f"Error al obtener total de horas: {str(e)}")
            return False, 0
        finally:
            if cursor:
                cursor.close()
    
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

    def reiniciar_horas(self, mydb):
        """Reinicia el contador de horas trabajadas en la base de datos"""
        try:
            cursor = mydb.cursor()
            id_emp = int(input("Ingrese el ID del empleado: "))
            
            # Verificar si el empleado existe
            sql_check = "SELECT id_empleado FROM empleado WHERE id_empleado = %s"
            cursor.execute(sql_check, (id_emp,))
            if cursor.fetchone():
                # Reiniciar las horas trabajadas
                sql_reset = """
                UPDATE registroTiempo rt
                JOIN proyectoEmpleado pe ON rt.Id_pro_empleado = pe.Id_pro_empleado
                SET rt.horas_trabajadas = 0
                WHERE pe.Id_empleado = %s
                """
                cursor.execute(sql_reset, (id_emp,))
                mydb.commit()
                print("Contador de horas reiniciado correctamente")
                return True, "Contador de horas reiniciado correctamente"
            else:
                print("Empleado no encontrado")
                return False, "Empleado no encontrado"
                
        except Exception as e:
            print(f"Error al reiniciar horas: {str(e)}")
            return False, f"Error al reiniciar horas: {str(e)}"
        finally:
            if cursor:
                cursor.close()

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


    def registrar_horas(self, mydb):
        try:
            id_emp = int(input("Ingrese el ID del empleado: "))
            id_proy = int(input("Ingrese el ID del proyecto: "))
            horas = float(input("Ingrese las horas trabajadas: "))
            fecha = input("Ingrese la fecha (YYYY-MM-DD) o deje en blanco para hoy: ")
            
            if not fecha:
                fecha = datetime.now().strftime("%Y-%m-%d")
            
            cursor = mydb.cursor()
            # Verificar si el empleado y el proyecto existen
            sql_check = """SELECT pe.Id_pro_empleado FROM proyectoEmpleado pe 
                        WHERE pe.Id_empleado = %s AND pe.Id_proyecto = %s"""
            cursor.execute(sql_check, (id_emp, id_proy))
            resultado = cursor.fetchone()
            
            if resultado:
                id_pro_empleado = resultado[0]
                # Insertar el registro de tiempo
                sql_insert = """INSERT INTO registroTiempo (Id_pro_empleado, 
                            horas_trabajadas, fecha) VALUES (%s, %s, %s)"""
                cursor.execute(sql_insert, (id_pro_empleado, horas, fecha))
                mydb.commit()
                print("Horas registradas exitosamente")
                return True, "Horas registradas exitosamente"
            else:
                print("El empleado no está asignado a este proyecto")
                return False, "El empleado no está asignado a este proyecto"
                
        except Exception as e:
            print(f"Error al registrar horas: {str(e)}")
            return False, f"Error al registrar horas: {str(e)}"
        finally:
            if cursor:
                cursor.close()
        