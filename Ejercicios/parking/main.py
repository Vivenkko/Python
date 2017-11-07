# -*- coding: utf-8 -*-
from vehiculo import vehiculo as v
from furgoneta import furgoneta as f
from parking import parking as p
from autobus import autobus as a

opcion = 1
eleccion = 0
listaVeh = []

v1 = v("KFS 4324", "Bugatti", "120")
v2 = v("HLS 9835", "Lamborgini", "600")
a1 = a("GER 6523", "Mercedes-Benz", "2000", 50)
a2 = a("DFE 1542", "Renault", "120", 50)
f1 = f("EDD 4572", "Volkswagen", "6000", 8)
f2 = f("HHA 3627", "BMW", "180", 6)

listaVeh.append(v1)
listaVeh.append(v2)
listaVeh.append(a1)
listaVeh.append(a2)
listaVeh.append(f1)
listaVeh.append(f2)

p1 = p(30, len(listaVeh), listaVeh, 0)

def mostrarMenu():
    print ""
    print "***** Opciones del menú *****"
    print "1. Mostrar el estado actual del parking"
    print "2. Mostrar los vehículos"
    print "3. Mostrar total a pagar"
    print "4. Mostrar ganancias del día"
    print "0. Salir"
    print " "
    print "Elige una opción"

while opcion != 0:
    mostrarMenu()
    opcion = raw_input()

    if opcion == 0:
        print "Hasta la vista"

    if opcion == 1:
        print "*** Estado del parking ***"
        print p1

    if opcion == 2:
        print "*** Listado de vehículos ***"
        for x in p1.get_listaVehiculos():
            i = 1
            print "%s - %s" % (str(i), x)
            if isinstance(x, f):
                print "\t"+x.avisarLongitud()
            i += 1

    if opcion == 3:
        print "*** Calculando coste ***"
        for x in p1.get_listaVehiculos():
            i = 0
            if i == eleccion:
                if isinstance(x, v):
                    print x.precioAPagar()
                elif isinstance(x, f):
                    print x.precioAPagar()
                elif isinstance(x, a):
                    print x.precioAPagar()
            i += 1

    if opcion == 4:
        for x in p1.get_listaVehiculos():
            p1.calcularCajaTotal()

        print p1.get_caja()
