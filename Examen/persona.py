# -*- coding: utf-8 -*-
class Persona(object):
    def __init__(self, nombre, apellidos):
        self.__nombre = nombre
        self.__apellidos = apellidos

    def __str__(self):
        return '%s %s' % (self.__nombre, self.__apellidos)

class Trabajador(Persona):
    def __init__(self, nombre, apellidos, sueldo):
        super(Trabajador, self).__init__(nombre, apellidos)
        self.__sueldo = sueldo

    def get_sueldo(self):
        return self.__sueldo

    def set_sueldo(self, sueldo):
        self.__sueldo = sueldo

    def __str__(self):
        return super(Trabajador, self).__str__() + ' ' + str(self.__sueldo)

    def __cmp__(self, other):
        return self.__sueldo - other.__sueldo


p = Persona('Manuel', 'Ramallo')
t = Trabajador('Luismi', 'López', 10000)
t2 = Trabajador('Miguel', 'Campos', 10001)

print t
print t2