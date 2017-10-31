divisor = 7
no_multiplo = 5
inicio = 2000
fin = 3200
lista_num = []

for num in range(inicio,fin+1):
    if num % 7 == 0 and num % 5 != 0:
        lista_num.append(num)

print lista_num