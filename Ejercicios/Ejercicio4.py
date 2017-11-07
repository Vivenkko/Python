print "Introduzca su frase:"
cadena = raw_input()
letras = []
num = []

for x in cadena:
    if x.isalpha():
        letras.append(x)
    if x.isdigit():
        num.append(x)

print "LETRAS "+str(len(letras))+", NUMEROS "+str(len(num))