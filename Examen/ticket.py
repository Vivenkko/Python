# -*- coding: utf-8 -*-
from alimentacion import Alimentacion as a
from electronica import Electronica as e
from ropa import Ropa as r
from producto import Producto as p
from datetime import date

fecha = date.today()

alimento1 = ('ES-SE-22314','cebolla',0.14,'11/11/2017')
alimento2 = ('ES-JA-23623','botella de vino',11.55,'01/01/2038')
alimento3 = ('ES-CO-12352','chuleta de cerdo',0.90,'10/11/2017')
alimento4 = ('SU-SC-23145', 'tableta de chocolate', 1.15, '10/02/2018')
alimento5 = ('ES-VI-54324', 'queso curado de cabra', 13.30, '20/0/2018')
ropa1 = ('CH-BE-54628','camiseta joker',9.95,'M')
ropa2 = ('CH-YG-92114','vaqueros negros',19.95,'38')
ropa3 = ('CH-HK-13597','deportes Fila',29.95,'43')
ropa4 = ('CH-YZ-95371','colgante Mjölnir',2.50,'12')
ropa5 = ('CH-GH-53928','tirantes negros',11.25,'M')
electro1 = ('US-CA-52417','iPhone X',1350.00,'1 año')
electro2 = ('US-TX-65236','usb cafetera',50.00,'8 meses')
electro3 = ('US-CO-74125','portátil Mountain',2150.00,'2 años')
electro4 = ('US-MI-95682', 'lcd samsung s8', 250.00, '6 meses')
electro5 = ('US-CH-12456','microSD 1 TB',100.00,'1 año')

listaCompra = []
listaCompra.append(alimento1)
listaCompra.append(alimento2)
listaCompra.append(alimento3)
listaCompra.append(alimento4)
listaCompra.append(alimento5)
listaCompra.append(ropa1)
listaCompra.append(ropa2)
listaCompra.append(ropa3)
listaCompra.append(ropa4)
listaCompra.append(ropa5)
listaCompra.append(electro1)
listaCompra.append(electro2)
listaCompra.append(electro3)
listaCompra.append(electro4)
listaCompra.append(electro5)

print "********** Ticket de compra **********"
print "     Uncle`s Mike Supplies Store      "
print "             "+str(fecha)+"               "
print ""
print "Producto\tCantidad\tPrecio \t Total"
for x in range(0, len(listaCompra)):
    print listaCompra[x].format()
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
