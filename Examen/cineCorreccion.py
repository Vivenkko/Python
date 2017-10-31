# -*- coding: utf-8 -*-
# Variables
cartelera = {
    "Lunes" : "Terminator 2",
    "Martes" : "Blade",
    "Miércoles" : "Jurassic Park",
    "Jueves" : "TMNT",
    "Viernes" : "Labyrinth",
    "Sábado" : "Gremlims",
    "Domingo" : "Pulp fiction"
}

# Clases
class Pelicula(object):
    def __init__(self, Entrada, id, titulo):
        self.__entrada = Entrada

# Métodos
def mostrarCartelera():
    for key in cartelera:
        print "%s: %s" % (key, cartelera[key])

def mostrarMenu():
    print ""
    print "***** Opciones del menú *****"
    print "1. Mostrar cartelera"
    print "2. Comprar entradas"
    print "3. Mostrar total a pagar"
    print "4. Mostrar ganancias del día"
    print "0. Salir"
    print " "
    print "Elige una opción"

# Matriz
numFilas = 0
numColumnas = 0
matriz = []
for i in range(numFilas):
    matriz.append([])
    for j in range(numColumnas):
        matriz[i].append(None)