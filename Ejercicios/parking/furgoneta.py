# -*- coding: utf-8 -*-
from vehiculo import vehiculo as v

class furgoneta(v):
    def __init__(self, matricula, marca, tiempoEstacionado, longitud):
        super(furgoneta, self).__init__(matricula, marca, tiempoEstacionado)
        self.__longitud = longitud

    def get_longitud(self):
        return self.__longitud

    def set_longitud(self, longitud):
        self.__longitud = longitud

    def precioAPagar(self):
        importe = 0.04
        tasaLongitud = 0.2
        return importe * self.get_tiempoEstacionado() + tasaLongitud * self.get_longitud()

    def __str__(self):
        return super.__str__() + " Longitud: %s" % self.get_longitud()

    def avisarLongitud(self):
        print "Su furgoneta mide "+str(self.get_longitud())+" metros."