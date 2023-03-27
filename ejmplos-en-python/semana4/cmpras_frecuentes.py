cant_compras = 0 
valor_nueva_compra = 0.0
descuento_porc = 0.35



cant_compras = int(input('ingrese la cantidad de compras:'))
valor_nueva_compra = int(input('ingrese la valor de la nueva compra'))

if (cant_compras >= 6 and valor_nueva_compra >= 10000):
    descuento = valor_nueva_compra - (valor_nueva_compra * 0.35)
    total =   descuento
    print('el valor de la compra seria',total)
else:
    print('el valor de la compra seria', valor_nueva_compra)


    #costo_final = costo_total - (costo_total * 0.35)