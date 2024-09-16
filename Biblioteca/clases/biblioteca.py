class biblioteca:
    def __init__(self, nombre, direccion, telefono, ISBN, buscar_libro, prestar_libro, devolver_libro):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__ISBN = ISBN
        self.__buscar_libro = buscar_libro
        self.__prestar_libro = prestar_libro
        self.__devolver_libro = devolver_libro
        
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_direccion(self):
        return self.__direccion
    
    def obtener_telefono(self):
        return self.__telefono
    
    def obtener_ISBN(self):
        return self.__ISBN
    
    def obtener_buscar_libro(self):
        return self.__buscar_libro
    
    def obtener_prestar_libro(self):
        return self.__prestar_libro
    
    def obtener_devolver_libro(self):
        return self.__devolver_libro
    
    