#entradas 
import math





#Entradas:



nom_equipo = (input('Nombre del equipo: '))

puntaje_num_juegos = int(input ('Puntaje de todos los partidos: '))

juegos_ejecutados  = int(input('Número de juegos ejecutados: '))

oponentes_diferentes  = int(input('Número de oponentes diferentes: '))

total_puntos_juego=0


if (juegos_ejecutados >= 5):
    puntos_por_juegos=1
    if (oponentes_diferentes==1):
        puntaje_oponentes= 1/3
    elif (oponentes_diferentes==2):
        puntaje_oponentes= 2/3
    elif (oponentes_diferentes>=3):
        puntaje_oponentes= 1
        puntaje_Total = puntaje_num_juegos + puntos_por_juegos+puntaje_oponentes 
        print ('Entradas:')
        print ('Nombre del equipo:',nom_equipo)
        print( 'Puntaje de todos los partidos:', puntaje_num_juegos )
        print('Número de juegos ejecutados:', juegos_ejecutados) 
        print ('Número de oponentes diferentes: ',oponentes_diferentes)
        print ('Salidas')
        print ('El puntaje total del equipo',nom_equipo, 'es:', puntaje_Total)
else: 
    total_puntos_juego+= math.sqrt(juegos_ejecutados) / 2.25
    if (oponentes_diferentes==1):
        puntaje_oponentes= 1/3
    elif(oponentes_diferentes == 2):
        puntaje_oponentes= 2/3
    else:
        (oponentes_diferentes>=3)
        puntaje_oponentes= 1
        Total = puntaje_num_juegos + total_puntos_juego+puntaje_oponentes
        print ('Entradas:')
        print ('Nombre del equipo:',nom_equipo)
        print( 'Puntaje de todos los partidos:', puntaje_num_juegos )
        print('Número de juegos ejecutados:', juegos_ejecutados) 
        print ('Número de oponentes diferentes: ',oponentes_diferentes)
        print ('Salidas')
        print ('El puntaje tota del equipo', nom_equipo, 'es:', Total)













