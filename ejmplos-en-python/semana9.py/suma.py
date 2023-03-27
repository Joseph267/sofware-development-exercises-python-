nom_equipo = 'maryland'
resultado = 0 
contrario = 'texas'
marcador_equipo = 40
marcador_oponente = 40
snitch = False

resultado = nom_equipo + " vs " + contrario + " " + str(marcador_equipo) + "-" + str(marcador_oponente)
print(resultado)
if snitch == 'si':
    index = len(resultado) - 3
    print(index)
    #resultado = resultado[:index] + "*" + resultado[index:]
