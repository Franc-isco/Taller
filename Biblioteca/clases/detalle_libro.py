class detalle_libro:
    def __init__ (self, ISBN, categoria, numero_de_paginas, indice_editorial, id_autor):
        self.__ISBN = ISBN
        self.__categoria = categoria
        self.__numero_de_paginas = numero_de_paginas
        self.__indice_editorial = indice_editorial
        self.__id_autor = id_autor
        
    def obtener_ISBN(self):
        return self.__ISBN
    
    def obtener_categoria(self):
        return self.__categoria
    
    def obtener_numero_de_paginas(self):
        return self.__numero_de_paginas
    
    def obtener_indice_editorial(self):
        return self.__indice_editorial
    
    def obtener_id_autor(self):
        return self.__id_autor
    
    
    

