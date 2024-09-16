class editorial:
    def __init__ (self, indice_editorial, nombre, telefono, ISBN):
        self.__indice_editorial = indice_editorial
        self.__nombre = nombre
        self.__telefono = telefono
        self.__ISBN = ISBN
    
    def obtener_indice_editorial(self):
        return self.__indice_editorial

    def obtener_nombre(self):
        return self.__nombre

    def obtener_telefono(self):
        return self.__telefono
    
    def obtener_ISBN(self):
        return self.__ISBN
    