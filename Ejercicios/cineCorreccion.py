# -*- coding: utf-8 -*-
# Variables
numEntradas = 0
totalPagar = 0
entradasVendidas = 0
numFila = 0
numLocalidad = 0
id = 0

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
    def __init__(self, entrada, id, titulo):
        self.__entrada = entrada

    def get_entrada(self):
        return self.__entrada

    def set_entrada(self, entrada):
        self.__entrada = entrada

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo


class Entrada(object):
    def __init__(self, id, precio, numFila, numLocalidad):
        self.__id = id
        self.__precio = precio
        self.__numFila = numFila
        self.__numLocalidad = numLocalidad

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def get_numFila(self):
        return self.__numFila

    def set_numFila(self, numFila):
        self.__numFila = numFila

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def str(self):
        return 'Id: %s   Precio: %s   Numero de fila: %s    Numero de localidad: %s' % (
        self.get_numeroId(), self.get_precio(), self.get_numeroFila(), self.get_localidad())


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


def calcularCoste(numEntradas):
    totalPagar = numEntradas * entrada.get_precio()
    numEntradas = 0
    return totalPagar


def calcularGanancias(entradasVendidas):
    totalDia = entradasVendidas * entrada.get_precio()
    return totalDia


# Matriz
numFilas = 10
numColumnas = 14
matriz = []
for i in range(numFilas):  # Crea la matriz asignando el num de columnas a cada una de las filas
    matriz.append([])
    for j in range(numColumnas):
        matriz[i].append(None)


# Ejecución
while opcion != 0:
    mostrarMenu()
    opcion = int(raw_input())

    if opcion == 1:
        mostrarCartelera()

    if opcion == 2:
        print "***** Comprando entrada *****"

        print "¿Cuántas entradas quiere comprar?"
        numEntradas = int(raw_input())
        entradasVendidas += numEntradas

        for i in range(numEntradas):
            id += 1
            print "Indique el número de fila de la entrada %s" % id
            numFila = int(raw_input())
            print "Indique el número de localidad de la entrada %s" % id
            numLocalidad = int(raw_input())

            while matriz[numFila][numLocalidad]:  # Comprueba si la celda de la matriz está ocupada
                print "El asiento elegido está ocupado. Elija otro."
                print "Indique el número de fila de la entrada %s" % id
                numFila = int(raw_input())
                print "Indique el número de localidad de la entrada %s" % id
                numLocalidad = int(raw_input())

            entrada = Entrada(id, precio, numFila, numLocalidad)  # Instancia de la entrada

            if not matriz[numFila][numLocalidad]:  # Comprueba si la celda de la matriz está vacía
                matriz[numFila][numLocalidad].append(entrada)

        for entrada in matriz:
            print entrada

    if opcion == 3:
        print "Total a pagar: %s €" % calcularCoste(numEntradas)

    if opcion == 4:
        print "Hoy se ha recaudado %s €" % calcularGanancias(entradasVendidas)

    if opcion == 0:
        print "Gracias por usar nuestros servicios"
