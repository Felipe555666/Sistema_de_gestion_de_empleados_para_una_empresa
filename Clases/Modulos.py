class modulos:
    def __init__(self,Id_modulo,Nombre,Nivel_requerido):
        self._Id_modulo = Id_modulo
        self._Nombre = Nombre
        self.Nivel_requerido = Nivel_requerido
        
    def get_nivel_requerido(self):
        return self.Nivel_requerido
    
    def validar_nivel(self, nivel_usuario):
        return nivel_usuario >= self.Nivel_requerido
