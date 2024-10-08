import libro

class biblioteca(libro):
    def __init__(self, id_biblioteca, nombre_biblioteca, direccion_biblioteca, telefono_biblioteca):
        self.id_biblioteca = id_biblioteca
        self.nombre_biblioteca = nombre_biblioteca
        self.direccion_biblioteca = direccion_biblioteca
        self.telefono_biblioteca = telefono_biblioteca
        self.libros = [] #lista para alamcenar libros

    def agregar_libros(self, libro):
        self.libros.append(libro)
    
    def buscar_libro(self, isbn): #por su isbn y devuelve el libro si lo encuentra
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None  
    
    def prestar_libro(self, isbn):
        libro_encontrado = self.buscar_libro(isbn) #ver si el libro se encuentra
        if libro_encontrado:
            if libro_encontrado.disponible:
                libro_encontrado.disponible = False #libro no disponible
                return f'El libro "{libro_encontrado.titulo}" ha sido prestado.'
            else:
                return f'El libro "{libro_encontrado.titulo}" no esta disponible.'
        else:
            return 'Libro no encontrado'
    
    def devolver_libro(self, isbn): 
        libro_encontrado = self.buscar_libro(isbn)
        if libro_encontrado:
            libro_encontrado.disponible = True #disponible
            return f'El libro "{libro_encontrado.titulo}" ha sido devuelto.'
        else:
            return 'Libro no encontrado.'

    
    