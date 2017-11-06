# -*- coding: utf-8 -*-
from producto import Producto as p

# Clase alimentación, que hereda de producto
class Alimentacion(p):
    def __init__(self, cod, nombre, precio, fechaCad):
        #p.Producto.__init__(self, cod, nombre, precio)
        super(Alimentacion,self).__init__(cod,nombre,precio)
        self.__fechaCad = fechaCad

    def get_fechaCad(self):
        return self.__fechaCad

    def set_fechaCad(self, fechaCad):
        self.__fechaCad = fechaCad

    def __str__(self):
        return p.str() + 'Fecha de caducidad: %s  ' % self.__fechaCad()
