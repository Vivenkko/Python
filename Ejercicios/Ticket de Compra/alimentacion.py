# -*- coding: utf-8 -*-
import producto

# Clase alimentación, que hereda de producto
class Alimentacion(producto):
    def __init__(self, cod, nombre, precio, fechaCad):
        producto.__init__()
        self.__fechaCad = fechaCad

    def get_fechaCad(self):
        return self.__fechaCad

    def set_fechaCad(self, fechaCad):
        self.__fechaCad = fechaCad

    def __str__(self):
        return 'Código de producto: %s   Nombre: %s   Precio: %s   Garantía: %s  ' % (
            self.get_cod(), self.get_nombre(), self.get_precio(), self.__fechaCad())
