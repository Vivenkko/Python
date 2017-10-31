print "Escriba su password:"
password = raw_input()
comprobacion = []
contador = 0

for x in password:
    comprobacion.append(x)

for x in comprobacion:
    if x.isdigit():
        contador += 1

if len(comprobacion) < 6 or len(comprobacion) > 12:
    print "Password incorrecto. Longitud inapropiada."
elif contador == 0:
    print "Password incorrecto. Se precisa un numero"