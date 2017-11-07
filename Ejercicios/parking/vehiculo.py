# -*- coding: utf-8 -*-

class vehiculo(object):
    def __init__(self, matricula, marca, tiempoEstacionado):
        self.__matricula = matricula
        self.__marca = marca
        self.__tiempoEstacionado = tiempoEstacionado

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_tiempoEstacionado(self):
        return self.__tiempoEstacionado

    def set_tiempoEstacionado(self, tiempoEstacionado):
        self.__tiempoEstacionado = tiempoEstacionado

    def __str__(self):
        return "Matrícula: %s    Marca: %s    Tiempo estacionado: %s    " % \
               (self.get_matricula(), self.get_marca(), self.get_tiempoEstacionado())

    def precioAPagar(self):
        importe = 0.04
        return importe * self.get_tiempoEstacionado()
