# -*- coding: utf-8 -*-
from vehiculo import vehiculo as v

class parking(object):
    def __init__(self, numPlazas, plazasOcupadas, listaVehiculos, caja):
        self.__numPlazas = numPlazas
        self.__plazasOcupadas = plazasOcupadas
        self.__listaVehiculos = listaVehiculos
        self.__caja = caja

    def get_numPlazas(self):
        return self.__numPlazas

    def set_numPlazas(self, numPlazas):
        self.__numPlazas = numPlazas

    def get_plazasOcupadas(self):
        return self.__plazasOcupadas

    def set_plazasOcupadas(self, plazasOcupadas):
        self.__plazasOcupadas = plazasOcupadas

    def get_listaVehiculos(self):
        return self.__listaVehiculos

    def set_listaVehiculos(self, listaVehiculos):
        self.__listaVehiculos = listaVehiculos

    def get_caja(self):
        return self.__caja

    def set_caja(self, caja):
        self.__caja = caja

    def __str__(self):
        return "Plazas totales del parking: %s \nPlazas ocupadas: %s \nPlazas libres: %s" % \
               (self.get_numPlazas(), self.get_plazasOcupadas(), str(self.get_numPlazas() - self.get_plazasOcupadas()))

    def calcularPagoUno(self):
        return v.precioAPagar()

    def calcularCajaTotal(self):
        self.caja += self.calcularPagoUno()
        return
