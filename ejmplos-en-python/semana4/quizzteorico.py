#entradas 

annos_de_la_piedra = 0.0
annos_de_la_piedra = float(input('ingrese los annos de la piedra:'))

#proceso y salida 
if annos_de_la_piedra <= 65.5:
    print (' la piedra pertenece a la era Cenozoica')
elif (annos_de_la_piedra > 65.5 and annos_de_la_piedra <= 251):
    print('la piedra Pertenece a la era Mesozoica')
elif annos_de_la_piedra >251 and annos_de_la_piedra <= 542:
    print('la piedra Pertenece a la era Paleozoica')
else:
     print('la piedra Pertenece a la era Pre-paleozoica')