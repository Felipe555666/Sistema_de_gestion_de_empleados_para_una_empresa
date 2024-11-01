import sys
from Empleado import empleado
from Proyecto import proyecto
from Registro_tiempo import registroTiempo
from Informe import informe
from Tipo_empleado import  tipoEmpleado
from Proyecto_empleado import  proyectoEmpleado


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
        obj =  empleado()

        while True:
            print("\n--- Gestión de Empleados ---")
            print("1. Registrar nuevo empleado")
            print("2. Ver datos de empleado")
            print("3. Actualizar empleado")
            print("4. Eliminar empleado")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                obj.registrar_empleado()
            elif opcion == "2":
                obj.ver_empleado()
            elif opcion == "3":
                obj.actualizar_empleado()
            elif opcion == "4":
                obj.eliminar_empleado()
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_proyectos(self):
        obj =   proyecto()

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
                obj.crear_proyecto()
            elif opcion == "2":
                obj.ver_proyecto()
            elif opcion == "3":
                obj.actualizar_proyecto()
            elif opcion == "4":
                obj.eliminar_proyecto()
            elif opcion == "5":
                obj.asignar_empleado_proyecto()
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
                obj.registrar_horas()
            elif opcion == "2":
                obj.ver_horas_trabajadas()
            elif opcion == "3":
                obj.reiniciar_horas()
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

    def menu_proyecto_empleado(self):
        obj =   proyectoEmpleado()
    # Aquí irían los métodos para cada operación (registrar_empleado, crear_proyecto, etc.)
    # Por ejemplo:
    
    

    

    

    

    


        