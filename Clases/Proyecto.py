from datetime import datetime
class proyecto:
    def __init__(self,Id_proyecto,Nombre,Descripcion,Fecha_inicio,Fecha_fin):
        self.__Id_proyecto = Id_proyecto
        self._Nombre = Nombre
        self._Descripcion = Descripcion
        self._Fecha_inicio = Fecha_inicio
        self._Fecha_fin = Fecha_fin
    
    def validar_fechas(self):

        formato_fecha = "%Y-%m-%d"

        try:
            fecha_inicio = datetime.strptime(self._Fecha_inicio, formato_fecha)
        except ValueError:
            return False, "La fecha de inicio no esta en el formato correcto"
        
        try:
            fecha_fin = datetime.strptime(self._Fecha_fin, formato_fecha)
        except:
            return False, "La fecha de fin no esta en el formato correcto"
        
        if fecha_inicio > fecha_fin:
            return False, "La fecha de inicio no puede se posterior a la fecha fin"
        
        fecha_actual = datetime.now()
        if fecha_inicio > fecha_actual or fecha_fin > fecha_actual:
            return False, "Las fechas no puedes ir al futuro"
        
        return True, "las fechas son validas"
    