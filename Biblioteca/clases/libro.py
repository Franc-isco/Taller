class libro:
    def __init__ (self, ISBN, titulo, id_autor, numero_de_copias, indice_editorial):
        self.__ISBN = ISBN,
        self.__titulo = titulo,
        self.__id_autor = id_autor,
        self.__numero_de_copias = numero_de_copias
        self.__indice_editorial = indice_editorial
        
    def obtener_ISBN(self):
        return self.__ISBN
    
    def obtener_titulo(self):
        return self.__titulo
    
    def obtener_id_autor(self):
        return self.__id_autor
    
    def obtener_numero_de_copias(self):
        return self.__numero_de_copias

    def obtener_indice_editorial(self):
        return self.__indice_editorial
    

