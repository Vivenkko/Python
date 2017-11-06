# -*- coding: utf-8 -*-
from producto import Producto as p

# Clase alimentación, que hereda de producto
class Electronica(p):
    def __init__(self, cod, nombre, precio, garantia):
        p.__init__(self, cod, nombre, precio)
        self.__garantia = garantia

    def get_garantia(self):
        return self.__fechaCadgarantia

    def set_garantia(self, garantia):
        self.__garantia = garantia

    def __str__(self):
        return p.str()+'Garantía: %s  ' % self.__garantia()
