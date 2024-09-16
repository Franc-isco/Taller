class autor:
    def __init__(self, id_autor, nombre, obras, ISBN, indice_editorial):
        self.__id_autor = id_autor
        self.__nombre = nombre
        self.__obras = obras
        self.__ISBN = ISBN
        self.__indice_editorial = indice_editorial
    
    def obtener_id_autor(self):
        return self.__id_autor
    
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_obras(self):
        return self.__obras
    
    def obtener_ISBN(self):
        return self.__ISBN
    
    def obtener_indice_editorial(self):
        return self.__indice_editorial
    
    