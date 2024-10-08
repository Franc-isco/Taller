#importar módulo re, permite trabajar con expresiones regulares. 
import re

class editorial:
    def __init__ (self, id_editorial, nombre_editorial, telefono_editorial, correo_editorial, pais_editorial):
        self.id_editorial = id_editorial
        self.nombre_editorial = nombre_editorial
        self.telefono_editorial = telefono_editorial
        self.correo_editorial = correo_editorial
        self.pais_editorial = pais_editorial
    
    #validar correo cuando se cree una nueva instancia de la clase
        if not self.validar_correo(correo_editorial):
            raise ValueError('El formato del correo es inválido.')
    
    def validar_correo(self,correo):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' #expresión para validar el formato del correo
        return re.match(patron, correo) is not None #coincidencia o no con el patrón