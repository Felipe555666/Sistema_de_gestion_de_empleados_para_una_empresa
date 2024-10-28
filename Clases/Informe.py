from datetime import datetime
from Empleado import empleado

class informe():
    def __init__(self,Id_informe,Nombre_informe,Fecha_creacion,Id_empleado,Estado_informe):
        super().__init__(self, Id_empleado)
        self._Id_informe = Id_informe
        self._Nombre_informe = Nombre_informe
        self._Fecha_creacion = Fecha_creacion
        self._Estado_informe = Estado_informe

    def validar_fecha_creacion(self):
        formato_fecha = "%Y-%m-%d"  # Cambia el formato según tus necesidades

        try:
            fecha_creacion = datetime.strptime(self._Fecha_creacion, formato_fecha)
        except ValueError:
            return False, "La fecha de creación no está en el formato correcto (YYYY-MM-DD)."

        fecha_actual = datetime.now()
        if fecha_creacion > fecha_actual:
            return False, "La fecha de creación no puede estar en el futuro."

        return True, "La fecha de creación es válida."
    
    