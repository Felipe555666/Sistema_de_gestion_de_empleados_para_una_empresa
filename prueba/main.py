import sys
import mysql.connector
#from Empleado import empleado
from Proyecto import proyecto

#from Registro_tiempo import registroTiempo
#from Informe import informe
#from Tipo_empleado import  tipoEmpleado
#from Proyecto_empleado import  proyectoEmpleado
from conexion import Conexion
mydb = Conexion.iniciar_conexion()



class SistemaGestionEmpleados:

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
                self.menu_proyectos(mydb)
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




    def menu_proyectos(self, mydb):
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
                obj.crear_proyecto(mydb)
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

  

obj_principal = SistemaGestionEmpleados()
obj_principal.menu_principal()