class prestamo:
    def __init__ (self, ISBN, f_prestamo, f_entrega, numero_identificacion, entregado):
        self.__ISBN = ISBN
        self.__f_prestamo = f_prestamo
        self.__f_entrega = f_entrega
        self.__numero_identificacion = numero_identificacion
        self.__entregado = entregado
    
    def obtener_ISBN(self):
        return self.__ISBN

    def obtener_f_prestamo(self):
        return self.__f_prestamo
    
    def obtener_f_entrega(self):
        return self.__f_entrega
    
    def obtener_numero_identificacion(self):
        return self.__numero_identificacion
    
    def obtener_entregado(self):
        return self.__entregado
    