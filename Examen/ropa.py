# -*- coding: utf-8 -*-
from producto import Producto as p

# Clase alimentación, que hereda de producto
class Ropa(p):
    def __init__(self, cod, nombre, precio, talla):
        p.Producto.__init__(self, cod, nombre, precio)
        self.__talla = talla

    def get_talla(self):
        return self.__talla

    def set_talla(self, talla):
        self.__talla = talla

    def __str__(self):
        return p.str() + 'Talla: %s  ' % self.__talla()
