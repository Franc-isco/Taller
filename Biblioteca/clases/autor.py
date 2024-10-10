#importar la clase datetime para trabajr con fechas y horas
from datetime import datetime

class autor:
    def __init__(self, id_autor, nombre_autor, seudonimo_autor, obras_autor, nacionalidad, fecha_nacimiento, fecha_defuncion):
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.seudonimo_autor = seudonimo_autor
        self.obras_autor = obras_autor
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_defuncion = fecha_defuncion

    def convertir_fechas(self, fecha):
        fecha_dt = datetime.strptime(fecha, '%d/%m/%Y') #convierte la cadena fecha a un objeto datetime
        fecha_str = fecha_dt.strftime('%Y-%m-%d') #convierte el objeto datetima a una cadena
        return fecha_str