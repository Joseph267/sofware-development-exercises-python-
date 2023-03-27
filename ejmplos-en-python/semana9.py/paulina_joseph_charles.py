#entradas 
import math

#Entradas:
nom_equipo=''
juegos_ejecutados=0
total_marcador = 0

resultado=''
resultados = []
contrario = ''
i=1 
y = 1
snitch=False
contrario_snitch=False
index = ''

nom_equipo= input ('Ingrese el nombre de su equipo: ')
juegos_ejecutados = int(input(f'Ingrese el numero de juegos de {nom_equipo}:'))
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
    
    y+=1
    resultados.append(resultado)
    
    total_marcador += marcador_equipo
    i+=1
    
for resultado in resultados:
    print (resultado)
suma=f'El puntaje total de partidos de {nom_equipo} es: {total_marcador}'
print('\n')
print (suma)
