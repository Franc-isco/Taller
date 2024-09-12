class usuario:
    def __init__(self, numero_identificacion, nombre, correo, telefono, habilitado):
        self.__numero_identificacion = numero_identificacion
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
        self.__habilitado = habilitado

    def obtener_numero_identificacion(self):
        return self.__numero_identificacion
    
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_correo(self):
        return self.__correo
    
    def obtener_telefono(self):
        return self.__telefono
    
    def obtener_habilitado(self):
        return self.__habilitado


    
