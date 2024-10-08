#importar módulos pasa usar las clases definidas
import libro
import editorial
import categoria

class detalle_libro(libro, editorial, categoria): #herencia de las clases libro, editorial y categoria. 
    def __init__ (self, id_detalle, n_de_paginas, ejemplares_disponibles, n_ejemplares, isbn, id_editorial, id_categoria):
        libro.__init__(isbn) #inicialización de clases bases
        editorial.__init__(id_editorial)
        categoria.__init__(id_categoria)
        self.id_detalle = id_detalle #definición de atributos
        self.n_de_paginas = n_de_paginas
        self.ejemplares_disponibles = ejemplares_disponibles
        self.n_ejemplares = n_ejemplares

    def actualizar_disponibilidad(self, ejemplares_prestados):
        if ejemplares_prestados < 0:
            raise ValueError('El número de ejemplares prestados no puede ser negativo.') #si ejemplares_prestados es negativo, lanza un error. 
        if ejemplares_prestados > self.ejemplares_disponibles:
            raise ValueError('No hay sufientes ejemplares disponibles para prestar.') #verifica si no se estén prestando más ejemplares de los que están disponibles.
        self.ejemplares_disponibles -= ejemplares_prestados #actualiza la cantidad de ejemplares disponibles restando los prestados. 
        if self.ejemplares_disponibles < 0:
            self.ejemplares_disponibles = 0 #asegurar que la nueva cantidad disponible no sea negativo. 
        print(f'Ejemplares disponibles actualizados: {self.ejemplares_disponibles}')