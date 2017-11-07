opcion = 0
resultado = 0

while opcion.isdigit():
    print "Introduzca un numero:"
    opcion = raw_input()
    if opcion.isdigit():
        int(opcion)
        resultado += opcion

print "La suma total es "+resultado