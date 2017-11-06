# -*- coding: utf-8 -*-
# Clase Producto
class Producto(object):
    def __init__(self, cod, nombre, precio):
        self.__cod = cod
        self.__nombre = nombre
        self.__precio = precio

    def get_cod(self):
        return self.__cod

    def set_cod(self, cod):
        self.__cod = cod

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def str(self):
        return 'Código de producto: %s   Nombre: %s   Precio: %s  ' % (
            self.get_cod(), self.get_nombre(), self.get_precio())
