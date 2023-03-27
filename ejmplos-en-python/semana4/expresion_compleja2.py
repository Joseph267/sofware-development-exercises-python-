dia_del_mes = 0
promocion = False
valoracion = 0.0
mayor_edad = False
 



dia_del_mes = int(input('ingrase el dia de la funcion:'))
promocion = bool(input('existe promocion? 1 para true 2 para false'))
mayor_edad = bool(input('Es para mayores de edad? 1 para true 2 para false'))
valoracion = float(input('ingrase la valoracion de la pelicula'))


if promocion == 1:
    conpromocion = True
else:
    conpromocion = False


if mayor_edad == 1:
    mayorde_edad = True
else:
    mayorde_edad = False


if (dia_del_mes > 15 or conpromocion) and (valoracion > 4 or not mayorde_edad):
    print('ire al cine')
else:
    print('no ire al cine')
