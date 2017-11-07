# -*- coding: utf-8 -*-
import producto
import alimentacion
import electronica
import ropa

listaProductos = [
    alimentacion('ES-SE-22314','cebolla',0.14,'11/11/2017'),
    alimentacion('ES-JA-23623','botella de vino',11.55,'01/01/2038'),
    alimentacion('ES-CO-12352','chuleta de cerdo',0.90,'10/11/2017'),
    alimentacion('SU-SC-23145','tableta de chocolate',1.15,'10/02/2018'),
    alimentacion('ES-VI-54324','queso curado de cabra',13.30,'20/0/2018'),
    ropa('CH-YG-92114','vaqueros negros',19.95,'38'),
    ropa('CH-BE-54628','camiseta joker',9.95,'M'),
    ropa('CH-HK-13597','deportes Fila',29.95,'43'),
    ropa('CH-YZ-95371','colgante Mjölnir',2.50,'12'),
    ropa('CH-GH-53928','tirantes negros',11.25,'M'),
    electronica('US-CA-52417','iPhone X',1350.00,'1 año'),
    electronica('US-CO-74125','portátil Mountain',2150.00,'2 años'),
    electronica('US-MI-95682','lcd samsung s8',250.00,'6 meses'),
    electronica('US-CH-12456','microSD 1 TB',100.00,'1 año'),
    electronica('US-TX-65236','usb cafetera',50.00,'8 meses')
]

print listaProductos
