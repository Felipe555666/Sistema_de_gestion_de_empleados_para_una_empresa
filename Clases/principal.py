import sys
from Empleado import empleado
from Proyecto import proyecto
from Registro_tiempo import registroTiempo
from Informe import informe
from Tipo_empleado import tipoEmpleado

class SistemaGestionEmpleados:
    def __init__(self):
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
            elif opcion == "0":
                print("Gracias por usar el sistema. ¡Hasta luego!")
                sys.exit()
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_empleados(self):
        while True:
            print("\n--- Gestión de Empleados ---")
            print("1. Registrar nuevo empleado")
            print("2. Ver datos de empleado")
            print("3. Actualizar empleado")
            print("4. Eliminar empleado")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.registrar_empleado()
            elif opcion == "2":
                self.ver_empleado()
            elif opcion == "3":
                self.actualizar_empleado()
            elif opcion == "4":
                self.eliminar_empleado()
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_proyectos(self):
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
                self.crear_proyecto()
            elif opcion == "2":
                self.ver_proyecto()
            elif opcion == "3":
                self.actualizar_proyecto()
            elif opcion == "4":
                self.eliminar_proyecto()
            elif opcion == "5":
                self.asignar_empleado_proyecto()
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_registro_tiempo(self):
        while True:
            print("\n--- Registro de Tiempo ---")
            print("1. Registrar horas trabajadas")
            print("2. Ver total de horas trabajadas")
            print("3. Reiniciar contador de horas")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.registrar_horas()
            elif opcion == "2":
                self.ver_horas_trabajadas()
            elif opcion == "3":
                self.reiniciar_horas()
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_informes(self):
        while True:
            print("\n--- Informes ---")
            print("1. Crear nuevo informe")
            print("2. Ver informe")
            print("3. Actualizar informe")
            print("4. Eliminar informe")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.crear_informe()
            elif opcion == "2":
                self.ver_informe()
            elif opcion == "3":
                self.actualizar_informe()
            elif opcion == "4":
                self.eliminar_informe()
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    # Aquí irían los métodos para cada operación (registrar_empleado, crear_proyecto, etc.)
    # Por ejemplo:
    
    def registrar_empleado(self):
        print("\n--- Registrar Nuevo Empleado ---")
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
        salario = float(input("Salario: "))
        fecha_nac = input("Fecha de nacimiento (YYYY-MM-DD): ")
        contrasena = input("Contraseña: ")
        tipo_empleado = input("Tipo de empleado: ")
        permiso = int(input("Nivel de permiso (0-10): "))

        nuevo_empleado = empleado(self.id_empleado, self.id_tipo_empleado, tipo_empleado, permiso, "")
        nuevo_empleado.establecer_datos_personales(nombre, direccion, telefono, correo, fecha_inicio, salario, fecha_nac, contrasena)
        
        if nuevo_empleado.validar_datos()[0] and nuevo_empleado.validar_fechas()[0]:
            self.empleados[self.id_empleado] = nuevo_empleado
            self.id_empleado += 1
            print("Empleado registrado con éxito.")
        else:
            print("Error al registrar empleado. Verifique los datos ingresados.")

    def ver_empleado(self):
        id_emp = int(input("Ingrese el ID del empleado: "))
        if id_emp in self.empleados:
            info = self.empleados[id_emp].obtener_informacion_empleado()
            for key, value in info.items():
                print(f"{key}: {value}")
        else:
            print("Empleado no encontrado.")

    def actualizar_empleado(self):
        id_emp = int(input("Ingrese el ID del empleado a actualizar: "))
        if id_emp in self.empleados:
            emp = self.empleados[id_emp]
            print("Deje en blanco si no desea actualizar el campo.")
            nombre = input("Nuevo nombre: ") or emp._Nombre
            direccion = input("Nueva dirección: ") or emp._Direccion
            telefono = input("Nuevo teléfono: ") or emp._Telefono
            correo = input("Nuevo correo: ") or emp._Correo
            
            emp.establecer_datos_personales(nombre, direccion, telefono, correo, 
                                            emp._Fecha_inicio, emp._Salario, emp._Fecha_nac, emp.__Contrasena)
            if emp.validar_datos()[0]:
                print("Empleado actualizado con éxito.")
            else:
                print("Error al actualizar empleado. Verifique los datos ingresados.")
        else:
            print("Empleado no encontrado.")

    def eliminar_empleado(self):
        id_emp = int(input("Ingrese el ID del empleado a eliminar: "))
        if id_emp in self.empleados:
            del self.empleados[id_emp]
            print("Empleado eliminado con éxito.")
        else:
            print("Empleado no encontrado.")

    def crear_proyecto(self):
        print("\n--- Crear Nuevo Proyecto ---")
        nombre = input("Nombre del proyecto: ")
        descripcion = input("Descripción: ")
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")

        nuevo_proyecto = proyecto(self.id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin)
        if nuevo_proyecto.validar_fechas()[0]:
            self.proyectos[self.id_proyecto] = nuevo_proyecto
            self.id_proyecto += 1
            print("Proyecto creado con éxito.")
        else:
            print("Error al crear proyecto. Verifique las fechas ingresadas.")

    def ver_proyecto(self):
        id_proy = int(input("Ingrese el ID del proyecto: "))
        if id_proy in self.proyectos:
            info = self.proyectos[id_proy].obtener_informacion_proyecto()
            for key, value in info.items():
                print(f"{key}: {value}")
        else:
            print("Proyecto no encontrado.")

    def actualizar_proyecto(self):
        id_proy = int(input("Ingrese el ID del proyecto a actualizar: "))
        if id_proy in self.proyectos:
            proy = self.proyectos[id_proy]
            print("Deje en blanco si no desea actualizar el campo.")
            nombre = input("Nuevo nombre: ") or proy._Nombre
            descripcion = input("Nueva descripción: ") or proy._Descripcion
            fecha_fin = input("Nueva fecha de fin (YYYY-MM-DD): ") or proy._Fecha_fin
            
            proy._Nombre = nombre
            proy._Descripcion = descripcion
            proy._Fecha_fin = fecha_fin
            
            if proy.validar_fechas()[0]:
                print("Proyecto actualizado con éxito.")
            else:
                print("Error al actualizar proyecto. Verifique las fechas ingresadas.")
        else:
            print("Proyecto no encontrado.")

    def eliminar_proyecto(self):
        id_proy = int(input("Ingrese el ID del proyecto a eliminar: "))
        if id_proy in self.proyectos:
            del self.proyectos[id_proy]
            print("Proyecto eliminado con éxito.")
        else:
            print("Proyecto no encontrado.")

    def asignar_empleado_proyecto(self):
        id_emp = int(input("Ingrese el ID del empleado: "))
        id_proy = int(input("Ingrese el ID del proyecto: "))
        if id_emp in self.empleados and id_proy in self.proyectos:
            # Aquí se debería crear una instancia de proyectoEmpleado
            print("Empleado asignado al proyecto con éxito.")
        else:
            print("Empleado o proyecto no encontrado.")

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
        