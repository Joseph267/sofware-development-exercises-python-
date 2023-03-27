#entradas 
import math

#Entradas:
nom_equipo=''
puntaje_num_juegos=0
juegos_ejecutados=0
total_puntos_juego=0.0
marcador=0


resultado=''
nom_equipo= '' 
juegos_ejecutados= 0 
resultados = []
contrario = ''
i=1 
y = 1
snitch=False
marcador = 0
marcador_contrario=0
contrario_snitch=False
index = ''

nom_equipo= input ('Ingrese el nombre de su equipo: ')
juegos_ejecutados = int(input(f'Ingrese el numero de juegos de {nom_equipo}:'))
snitch=False
juego=1
puntaje_total=0
while (i<=juegos_ejecutados):
    print (f'juego {y}')
    contrario = input ('Ingrese el nombre del equipo contrario:')
    marcador_equipo = int(input(f"Marcador de {nom_equipo}: "))
    snitch = input("Atrapó la snitch: ")
    marcador_oponente = int(input(f'Marcador de {contrario}: '))
    contrario_snitch=input("equipo contrario atrapó la snitch: ")
    resultado = nom_equipo + " vs " + contrario + " " + str(marcador_equipo) + "-" + str(marcador_oponente)
    if snitch == 'si':
        index = len(resultado) - 3
        resultado = resultado[:index] + "*" + resultado[index:]
    else:
        if contrario_snitch== 'si':
            index = len(resultado)
            resultado = resultado[:index] + "*" + resultado[index:]           
        else:
            resultado = nom_equipo + " vs " + contrario + " " + str(marcador_equipo) + "-" + str(marcador_oponente)
    marcador_equipo += marcador_equipo
    #print(resultado)
    y+=1
    i+=1
    print(resultado)
suma = f'El puntaje total de partidos de {nom_equipo} es: {marcador_equipo}'

print (suma)