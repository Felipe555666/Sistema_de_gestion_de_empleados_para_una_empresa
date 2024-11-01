from conexion import Conexion

mydb = Conexion.iniciar_conexion()

class Empleado:
    def crear_empleado(self):
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

        cursor = mydb.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO empleado (nombre, direccion, telefono, correo, fecha_inicio, salario, fecha_nacimiento, contrasena, id_tipoEmpleado)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (nombre, direccion, telefono, correo, fecha_inicio, salario, fecha_nac, contrasena, tipo_empleado))
            
            mydb.commit()
            print("Empleado agregado correctamente")
        except Exception as e:
            print(f"Error al agregar empleado: {e}")
        finally:
            cursor.close()

obj = Empleado()
obj.crear_empleado()
