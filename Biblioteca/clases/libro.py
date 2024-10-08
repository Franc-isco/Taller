import autor
import re

class libro(autor):
    def __init__ (self, isbn, titulo, n_de_copias, año_publicacion, id_autor):
        super().__init__(id_autor)
        self.isbn = isbn
        self.titulo = titulo
        self.n_de_copias = n_de_copias
        self.año_publicacion = año_publicacion

    def validar_isbn(self, isbn): #para validar si el formato es ISBN-10 o ISBN-13
        patron = r'^(?:ISBN(?:-1[03])?:? )?(?=[0-9]{10}$|[0-9]{13}$)([0-9]+[- ]?)+[0-9]$'
        if not re.match(patron, isbn):
            raise ValueError('El formato del ISBN es inválido.')
        return isbn
        
    def actualizar_copias(self, n_de_copias):
        if n_de_copias < 0:
            raise ValueError('El número de copias no puede ser negativo.')
        self.n_de_copias = n_de_copias #cambia la cantidad disponible de libros a una nueva cantidad
        
    def obtener_info(self):
        raise NotImplementedError('Este metodo debe ser sobrescrito.')

class librofisico(libro): #librofisico hereda de libro
    def obtener_info(self):
        return f'Libro Fisico: {self.titulo} (ISBN: {self.isbn}, Copias: {self.n_de_copias})' #informacion que devuelve

class librodigital(libro): #tambien hereda de libro
    def obtener_info(self):
        return f'Libro Digital: {self.titulo} (ISBN: {self.isbn}, Copias: {self.n_de_copias})'

#Mismo método tiene diferentes comportamientos dependiendo de la clase del objeto que lo invoca (Polimorfismo)
    #donde diferentes clases son tratadas como instancias de la misma clase en un interfaz común. 