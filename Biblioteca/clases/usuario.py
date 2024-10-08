import re
from rut_chile import rut_chile

class usuario:
    def __init__(self, id_usuario, nombre_usuario, correo_usuario, telefono_usuario, habilitado, pais_usuario, rut_usuario):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.correo_usuario = correo_usuario
        self.telefono_usuario = telefono_usuario
        self.habilitado = habilitado
        self.pais_usuario = pais_usuario
        self.rut_usuario = rut_usuario

    def validar_rut(self, rut): #validar formato de RUT chileno con rut_chile
        if rut_chile.validar(rut):
            return rut
        else:
            raise ValueError('El RUT es inválido.')

    # def validar_rut(self, rut):
    #     if rut_chile.validar(rut):
    #         return rut
    #     else:
    #         raise ValueError('El RUT es inválido')

    def validar_correo(self, correo):
        patron_correo = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(patron_correo, correo):
            return correo
        else:
            raise ValueError('El correo es inválido.')

    
