import mysql.connector
from mysql.connector import Error
import sys
from datetime import datetime
from Modulos import modulos
from Accesos import Accesos
from Departamento import Departamento
from Departamento_empleado import DepartamentoEmpleado
from Empleado import empleado
from Proyecto import proyecto
from Registro_tiempo import registroTiempo
from Informe import informe
from Tipo_empleado import tipoEmpleado
from Proyecto_empleado import proyectoEmpleado
from conexion import Conexion

mydb = Conexion.iniciar_conexion()


class SistemaGestionEmpleados:
    def __init__(self):
        self.mydb = Conexion.iniciar_conexion()
        if self.mydb is None:
            print("Error al conectar a la base de datos")
            sys.exit(1)
        self.empleados = {}
        self.proyectos = {}
        self.registros_tiempo = {}
        self.informes = {}
        self.tipos_empleado = {}
        self.id_empleado = 1
        self.id_proyecto = 1
        self.id_registro = 1
        self.id_informe = 1
        self.id_tipo_empleado = 1
        

    def menu_principal(self):
        while True:
            print("\n--- Sistema de Gestión de Empleados ---")
            print("1. Gestión de Empleados")
            print("2. Gestión de Proyectos")
            print("3. Registro de Tiempo")
            print("4. Informes")
            print("5. Tipos de Empleado")
            print("6. Gestión de Departamentos")
            print("7. Gestión de Accesos")
            print("0. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.menu_empleados()
            elif opcion == "2":
                self.menu_proyectos()
            elif opcion == "3":
                self.menu_registro_tiempo()
            elif opcion == "4":
                self.menu_informes()
            elif opcion == "5":
                self.menu_tipos_empleado()
            elif opcion == "6":
                self.menu_departamentos()
            elif opcion == "7":
                self.menu_accesos()    
            elif opcion == "0":
                print("Gracias por usar el sistema. ¡Hasta luego!")
                sys.exit()
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_empleados(self):
        obj = empleado()  # Crear una instancia de la clase empleado
        while True:
            print("\n--- Gestión de Empleados ---")
            print("1. Registrar nuevo empleado")
            print("2. Ver datos de empleado")
            print("3. Actualizar empleado")
            print("4. Eliminar empleado")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                if self.mydb:
                    obj.registrar_empleado(self.mydb)
                else:
                    print("Error: No hay conexión a la base de datos")
            elif opcion == "2":
                if self.mydb:
                    obj.ver_empleado(self.mydb)  # Pasar la conexión a la base de datos
                else:
                    print("Error: No hay conexión a la ba1se de datos")
            elif opcion == "3":
                if self.mydb:
                    obj.actualizar_empleado_bd(self.mydb) 
                else:
                    print("Error: No hay conexión a la base de datos")
            elif opcion == "4":
                if self.mydb:
                    obj.eliminar_empleado(self.mydb)  # Pasar la conexión a la base de datos
                else:
                    print("Error: No hay conexión a la base de datos")
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_proyectos(self):
        obj = proyecto()
        obj_asignacion = proyectoEmpleado(None, None, None, None, None, None, None)
        while True:
            print("\n--- Gestión de Proyectos ---")
            print("1. Crear nuevo proyecto")
            print("2. Ver detalles de proyecto")
            print("3. Actualizar proyecto")
            print("4. Eliminar proyecto")
            print("5. Asignar empleado a proyecto")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                if self.mydb:
                    print("\n--- Crear Nuevo Proyecto ---")
                    
                    # Validar la entrada del ID del proyecto
                    while True:
                        id_proyecto_input = input("ID del proyecto: ")
                        if id_proyecto_input.isdigit():  # Verifica si la entrada es un número
                            id_proyecto = int(id_proyecto_input)
                            break
                        else:
                            print("Por favor, ingrese un ID válido (número entero).")

                    nombre = input("Nombre del proyecto: ")
                    descripcion = input("Descripción: ")
                    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
                    fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
                    
                    nuevo_proyecto = proyecto(id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin)
                    
                    # Llamar al método para crear el proyecto en la base de datos
                    resultado = proyecto.crear_proyecto_bd(self.mydb, nuevo_proyecto)
                    print(resultado[1])  # Mostrar el mensaje de resultado
                else:
                    print("Error: No hay conexión a la base de datos")
                    
            elif opcion == "2":
                try:
                    # Verificar la conexión
                    if not self.mydb or not self.mydb.is_connected():
                        self.mydb = Conexion.iniciar_conexion()
                        if not self.mydb:
                            print("Error: No se pudo establecer la conexión a la base de datos")
                            continue

                    # Solicitar y validar el ID del proyecto
                    while True:
                        id_proyecto_input = input("\nIngrese el ID del proyecto a consultar: ")
                        if id_proyecto_input.isdigit():
                            id_proyecto = int(id_proyecto_input)
                            break
                        else:
                            print("Por favor, ingrese un ID válido (número entero).")

                    # Crear cursor y ejecutar consulta
                    cursor = self.mydb.cursor(dictionary=True)
                    
                    # Consulta SQL
                    sql = """
                        SELECT id_proyecto, nombre, descripcion, 
                            DATE_FORMAT(fecha_inicio, '%Y-%m-%d') as fecha_inicio,
                            DATE_FORMAT(fecha_fin, '%Y-%m-%d') as fecha_fin
                        FROM proyecto 
                        WHERE id_proyecto = %s
                    """
                    
                    cursor.execute(sql, (id_proyecto,))
                    proyecto_info = cursor.fetchone()

                    if proyecto_info:
                        print("\n=== Detalles del Proyecto ===")
                        for key, value in proyecto_info.items():
                            print(f"{key}: {value}")

                        # Consultar empleados asignados
                        sql_empleados = """
                            SELECT e.id_empleado, e.nombre
                            FROM empleado e
                            JOIN proyectoEmpleado pe ON e.id_empleado = pe.Id_empleado
                            WHERE pe.Id_proyecto = %s
                        """
                        cursor.execute(sql_empleados, (id_proyecto,))
                        empleados = cursor.fetchall()

                        if empleados:
                            print("\nEmpleados asignados:")
                            for empleado in empleados:
                                print(f"- {empleado['nombre']} (ID: {empleado['id_empleado']})")
                        else:
                            print("\nNo hay empleados asignados a este proyecto.")
                    else:
                        print("No se encontró ningún proyecto con ese ID.")

                    cursor.close()

                except mysql.connector.Error as err:
                    print(f"Error de base de datos: {err}")
                    # Intentar reconectar si hay error de conexión
                    self.mydb = Conexion.iniciar_conexion()
                except Exception as e:
                    print(f"Error al consultar el proyecto: {str(e)}")

            elif opcion == "3":
                if self.mydb:
                    try:
                        id_proyecto = input("\nIngrese el ID del proyecto a actualizar: ")
                        if not id_proyecto.isdigit():
                            print("Por favor, ingrese un ID válido.")
                            continue
                            
                        cursor = self.mydb.cursor(dictionary=True)
                        sql = "SELECT * FROM proyecto WHERE id_proyecto = %s"
                        cursor.execute(sql, (id_proyecto,))
                        proyecto_actual = cursor.fetchone()
                        
                        if not proyecto_actual:
                            print("Proyecto no encontrado.")
                            continue
                            
                        print("\nDeje en blanco si no desea actualizar el campo.")
                        nombre = input("Nuevo nombre: ") or proyecto_actual['nombre']
                        descripcion = input("Nueva descripción: ") or proyecto_actual['descripcion']
                        fecha_inicio = input("Nueva fecha inicio (YYYY-MM-DD): ") or proyecto_actual['fecha_inicio']
                        fecha_fin = input("Nueva fecha fin (YYYY-MM-DD): ") or proyecto_actual['fecha_fin']
                        
                        # Crear objeto proyecto con los nuevos datos
                        proyecto_obj = proyecto(
                            Id_proyecto=int(id_proyecto),
                            Nombre=nombre,
                            Descripcion=descripcion,
                            Fecha_inicio=fecha_inicio,
                            Fecha_fin=fecha_fin
                        )
                        
                        # Actualizar en la base de datos
                        exito, mensaje = proyecto_obj.actualizar_proyecto_bd(self.mydb)
                        print(mensaje)
                        
                    except Exception as e:
                        print(f"Error al actualizar el proyecto: {str(e)}")
                else:
                    print("Error: No hay conexión a la base de datos")

            elif opcion == "4":
                if self.mydb:
                    obj.eliminar_proyecto(self.mydb)  # Llamar a la función eliminar_proyecto
                else:
                    print("Error: No hay conexión a la base de datos")
        
            elif opcion == "5":
                if self.mydb:
                    obj_asignacion.asignar_empleado_proyecto(self.mydb)
                pass
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_registro_tiempo(self):
        obj = registroTiempo()
        while True:
            print("\n--- Registro de Tiempo ---")
            print("1. Registrar horas trabajadas")
            print("2. Ver total de horas trabajadas")
            print("3. Reiniciar contador de horas")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                if self.mydb:
                    obj.registrar_horas(self.mydb)
                else:
                    print("Error: No hay conexión a la base de datos")
            elif opcion == "2":
                if self.mydb:
                    obj.obtener_total_horas(self.mydb)
                else:
                    print("Error: No hay conexión a la base de datos")
            elif opcion == "3":
                if self.mydb:
                    obj.reiniciar_horas(self.mydb)
                else:
                    print("Error: No hay conexión a la base de datos")
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_informes(self):
        obj = informe()
        while True:
            print("\n--- Informes ---")
            print("1. Crear nuevo informe")
            print("2. Ver informe")
            print("3. Actualizar informe")
            print("4. Eliminar informe")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                if self.mydb:
                    obj.crear_informe(self.mydb)
                else:
                    print("Error: No hay conexión a la base de datos")
            elif opcion == "2":
                if self.mydb:
                    obj.ver_informe(self.mydb)
                else:
                    print("Error: No hay conexión a la base de datos")
            elif opcion == "3":
                if self.mydb:
                    obj.actualizar_informe(self.mydb)
                else:
                    print("Error: No hay conexión a la base de datos")
            elif opcion == "4":
                if self.mydb:
                    obj.eliminar_informe(self.mydb)
                else:
                    print("Error: No hay conexión a la base de datos")
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_tipos_empleado(self):
        obj = tipoEmpleado()
        while True:
            print("\n--- Gestión de Tipos de Empleado ---")
            print("1. Crear nuevo tipo de empleado")
            print("2. Ver tipos de empleado")
            print("3. Actualizar tipo de empleado")
            print("4. Eliminar tipo de empleado")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                try:
                    tipo = input("Ingrese el tipo de empleado: ")
                    permiso = int(input("Ingrese el nivel de permiso (0-10): "))
                    
                    cursor = self.mydb.cursor()
                    sql = "INSERT INTO tipoEmpleado (Tipo, Permiso) VALUES (%s, %s)"
                    cursor.execute(sql, (tipo, permiso))
                    self.mydb.commit()
                    print("Tipo de empleado creado exitosamente")
                    
                except Exception as e:
                    print(f"Error al crear tipo de empleado: {str(e)}")
                finally:
                    if 'cursor' in locals():
                        cursor.close()
                        
            elif opcion == "2":
                try:
                    cursor = self.mydb.cursor(dictionary=True)
                    cursor.execute("SELECT * FROM tipoEmpleado")
                    tipos = cursor.fetchall()
                    
                    if tipos:
                        print("\n=== Tipos de Empleado ===")
                        for tipo in tipos:
                            print(f"ID: {tipo['Id_tipo_empleado']}")
                            print(f"Tipo: {tipo['Tipo']}")
                            print(f"Permiso: {tipo['Permiso']}")
                            print("-" * 20)
                    else:
                        print("No hay tipos de empleado registrados")
                        
                except Exception as e:
                    print(f"Error al consultar tipos de empleado: {str(e)}")
                finally:
                    if 'cursor' in locals():
                        cursor.close()
                        
            elif opcion == "3":
                try:
                    id_tipo = int(input("Ingrese el ID del tipo de empleado a actualizar: "))
                    
                    cursor = self.mydb.cursor(dictionary=True)
                    cursor.execute("SELECT * FROM tipoEmpleado WHERE Id_tipo_empleado = %s", (id_tipo,))
                    tipo_actual = cursor.fetchone()
                    
                    if tipo_actual:
                        print("\nDeje en blanco si no desea actualizar el campo")
                        nuevo_tipo = input(f"Tipo actual ({tipo_actual['Tipo']}). Nuevo tipo: ")
                        nuevo_permiso = input(f"Permiso actual ({tipo_actual['Permiso']}). Nuevo permiso: ")
                        
                        updates = []
                        valores = []
                        if nuevo_tipo:
                            updates.append("Tipo = %s")
                            valores.append(nuevo_tipo)
                        if nuevo_permiso:
                            updates.append("Permiso = %s")
                            valores.append(int(nuevo_permiso))
                        
                        if updates:
                            sql = f"UPDATE tipoEmpleado SET {', '.join(updates)} WHERE Id_tipo_empleado = %s"
                            valores.append(id_tipo)
                            cursor.execute(sql, tuple(valores))
                            self.mydb.commit()
                            print("Tipo de empleado actualizado exitosamente")
                    else:
                        print("Tipo de empleado no encontrado")
                        
                except Exception as e:
                    print(f"Error al actualizar tipo de empleado: {str(e)}")
                finally:
                    if 'cursor' in locals():
                        cursor.close()
                        
            elif opcion == "4":
                try:
                    id_tipo = int(input("Ingrese el ID del tipo de empleado a eliminar: "))
                    
                    cursor = self.mydb.cursor()
                    cursor.execute("DELETE FROM tipoEmpleado WHERE Id_tipo_empleado = %s", (id_tipo,))
                    self.mydb.commit()
                    
                    if cursor.rowcount > 0:
                        print("Tipo de empleado eliminado exitosamente")
                    else:
                        print("Tipo de empleado no encontrado")
                        
                except Exception as e:
                    print(f"Error al eliminar tipo de empleado: {str(e)}")
                finally:
                    if 'cursor' in locals():
                        cursor.close()
                        
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_departamentos(self):
        obj = Departamento()
        while True:
            print("\n--- Gestión de Departamentos ---")
            print("1. Ver departamentos")
            print("2. Crear nuevo departamento")
            print("3. Actualizar departamento")
            print("4. Eliminar departamento")
            print("5. Asignar empleado a departamento")
            print("6. Ver empleados por departamento")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                Departamento.ver_departamentos_db() 
            elif opcion == "2":
                obj.crear_departamento()
            elif opcion == "3":
                obj.actualizar_departamento()
            elif opcion == "4":
                obj.eliminar_departamento()
            elif opcion == "5":
                obj.asignar_empleado_departamento()
            elif opcion == "6":
                obj.ver_empleados_departamento()
            elif opcion == "0":
                break
            else:
                print("Opción no válida")

    def menu_accesos(self):
        try:
            while True:
                print("\n--- Gestión de Accesos ---")
                print("1. Verificar acceso de un empleado")
                print("2. Ver historial de accesos")
                print("3. Limpiar historial de accesos")
                print("0. Volver al menú principal")
                
                opcion = input("Seleccione una opción: ")
                
                if opcion == "1":
                    try:
                        id_empleado = int(input("Ingrese el ID del empleado: "))
                        id_modulo = int(input("Ingrese el ID del módulo: "))
                        
                        tiene_acceso, mensaje = Accesos.obtener_acceso(id_empleado, id_modulo)
                        print(mensaje)
                        
                        # Registrar el acceso
                        cursor = mydb.cursor()
                        cursor.execute("""
                            INSERT INTO Accesos (Id_modulo, Id_tipo_empleado, Exitoso) 
                            VALUES (%s, %s, %s)
                        """, (id_modulo, id_empleado, tiene_acceso))
                        mydb.commit()
                        
                    except ValueError:
                        print("Error: Los IDs deben ser números enteros")
                    except Exception as e:
                        print(f"Error al verificar acceso: {str(e)}")
                    finally:
                        if 'cursor':
                            cursor.close()
                elif opcion == "2":
                    # Ver historial de accesos
                    acceso = Accesos()
                    acceso.ver_historial_accesos()
                elif opcion == "3":
                    # Limpiar historial de accesos
                    acceso = Accesos()
                    acceso.limpiar_historial_accesos()
                elif opcion == "0":
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
        except Exception as e:
            print(f"Error en el menú de accesos: {str(e)}")
    

obj_principal = SistemaGestionEmpleados()
obj_principal.menu_principal()