nom_equipo= 'maryland'
contrario = 'texas'
marcador_equipo = 40
marcador_oponente = 40
snitch = 'no'
contrario_snitch='no'
index= ''

resultado = nom_equipo + " vs " + contrario + " " + str(marcador_equipo ) +"-" + str(marcador_oponente )

if snitch == 'si':
    index = len(resultado) - 3
    resultado = resultado[:index] + "*" + resultado[index:]
else:
    if contrario_snitch== 'si':
        index = len(resultado)
        resultado = resultado[:index] + "*" + resultado[index:]
    else:
        resultado = nom_equipo + " vs " + contrario + " " + str(marcador_equipo) + "-" + str(marcador_oponente)
print (resultado)
