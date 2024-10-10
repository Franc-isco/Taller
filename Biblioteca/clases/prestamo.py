import detalle_libro
import usuario
from datetime import datetime, timedelta

class prestamo(detalle_libro, usuario):
    def __init__ (self, id_prestamo, f_prestamo, f_entrega, entregado, cantidad_solicitada, isbn, id_usuario):
        detalle_libro.__init__(isbn)
        usuario.__init__(id_usuario)
        self.id_prestamo = id_prestamo
        self.f_prestamo = datetime.strptime(f_prestamo, "%Y-%m-%d") #convertir la cadena a un objeto datetime para aplicar en los metodos
        self.f_entrega = datetime.strptime(f_entrega, "%Y-%m-%d") 
        self.entregado = entregado
        self.cantidad_solicitada = cantidad_solicitada

    def agregar_dias(self, dias):
        self.f_prestamo += timedelta(days=dias) #agregas dias a la fecha de prestamo
    
    def calcular_fecha_devolucion(self, dias_prestamo):
        return self.f_prestamo + timedelta(days = dias_prestamo) #devuelve la nueva fecha de devolucion
    
class prestamofisico(prestamo):
    def calcular_fecha_devolucion(self, dias_prestamo):
        return super().calcular_fecha_devolucion(dias_prestamo + 2) #Agregamos 2 días extras al libro fisico

class prestamodigital(prestamo):
    def calcular_fecha_devolucion(self, dias_prestamo):
        return super().calcular_fecha_devolucion(dias_prestamo + 1) #Agregamos un dia extra a libro digital