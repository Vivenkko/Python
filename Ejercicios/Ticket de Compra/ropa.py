# -*- coding: utf-8 -*-
import producto

# Clase alimentación, que hereda de producto
class Ropa(producto):
    def __init__(self, cod, nombre, precio, talla):
        producto.__init__()
        self.__talla = talla

    def get_talla(self):
        return self.__talla

    def set_talla(self, talla):
        self.__talla = talla

    def __str__(self):
        return 'Código de producto: %s   Nombre: %s   Precio: %s   Talla: %s  ' % (
            self.get_cod(), self.get_nombre(), self.get_precio(), self.__talla())
