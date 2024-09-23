import libro
import usuario

class prestamo(libro, usuario):
    def __init__ (self, isbn, f_prestamo, f_entrega, n_identificacion, entregado, id_biblioteca):
        libro.__init__(isbn)
        usuario.__init__(n_identificacion)
        self.f_prestamo = f_prestamo
        self.f_entrega = f_entrega
        self.n_identificacion = n_identificacion
        self.entregado = entregado
        self.id_biblioteca = id_biblioteca

    