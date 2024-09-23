import libro
import editorial

class detalle_libro(libro, editorial):
    def __init__ (self, id_detalle, categoria, n_de_paginas, id_editorial, isbn, n_ejemplares, ejemplares_disponibles):
        libro.__init__(isbn)
        editorial.__init__(id_editorial)
        self.id_detalle = id_detalle
        self.isbn = isbn
        self.categoria = categoria
        self.n_de_paginas = n_de_paginas
        self.id_editorial = id_editorial
        

    
    
    

