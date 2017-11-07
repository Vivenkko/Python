# -*- coding: utf-8 -*-
import producto

# Clase alimentación, que hereda de producto
class Electronica(producto):
    def __init__(self, cod, nombre, precio, garantia):
        producto.__init__()
        self.__garantia = garantia

    def get_garantia(self):
        return self.__fechaCadgarantia

    def set_garantia(self, garantia):
        self.__garantia = garantia

    def __str__(self):
        return 'Código de producto: %s   Nombre: %s   Precio: %s   Garantía: %s  ' % (
            self.get_cod(), self.get_nombre(), self.get_precio(), self.__garantia())
