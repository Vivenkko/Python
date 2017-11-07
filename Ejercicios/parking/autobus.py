# -*- coding: utf-8 -*-
from vehiculo import vehiculo as v

class autobus(v):
    def __init__(self, matricula, marca, tiempoEstacionado, numAsientos):
        super(autobus, self).__init__(matricula, marca, tiempoEstacionado)
        self.__numAsientos = numAsientos

    def get_numAsientos(self):
        return self.__numAsientos

    def set_numAsientos(self, numAsientos):
        self.__numAsientos = numAsientos

    def precioAPagar(self):
        tasaAsientos = 0.25
        return super(autobus, self).precioAPagar() + tasaAsientos * self.get_numAsientos()

    def __str__(self):
        return super(self).__str__() + " Número de asientos: %s" % self.get_numAsientos()
