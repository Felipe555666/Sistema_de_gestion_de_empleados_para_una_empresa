class tipoEmpleado:
    def __init__(self,Id_tipo_empleado,Tipo,Permiso,Desc_empleado):
        self._Id_tipo_empleado = Id_tipo_empleado
        self._Tipo = Tipo
        self._Permiso = Permiso
        self._Desc_empleado = Desc_empleado

    def actualizar_tipo_empleado(self, Tipo=None, Permiso=None, Desc_empleado=None):
        # Validar y actualizar el tipo
        if Tipo is not None:
            if isinstance(Tipo, str) and Tipo:
                self._Tipo = Tipo
            else:
                return False, "El tipo debe ser un valor de texto no vacío."

        # Validar y actualizar el permiso
        if Permiso is not None:
            if isinstance(Permiso, int) and 0 <= Permiso <= 10:  # Ajusta el rango de permisos según tus necesidades
                self._Permiso = Permiso
            else:
                return False, "El permiso debe ser un número entero entre 0 y 10."

        # Validar y actualizar la descripción del empleado
        if Desc_empleado is not None:
            if isinstance(Desc_empleado, str) and Desc_empleado:
                self._Desc_empleado = Desc_empleado
            else:
                return False, "La descripción debe ser un valor de texto no vacío."

        return True, "Los datos del tipo de empleado han sido actualizados exitosamente."
