#Una piedra con menos de 65.5 millones de años de haber sido formada pertenece a la era cenozoica. Una con más de
#esta cantidad, pero menos de 251 millones de años se clasifica como mesozoica. Una con más de esta edad,
#pero menos de 542 millones de años se considera de la era paleozoica. Una piedra con más de esta cantidad de
#años se considera como de la era pre-paleozoica. El siguiente cuadro resume esta información


Edad_de_piedra = 0.0

Edad_de_piedra = float(input('ingrese los annos de la piedra:'))

if Edad_de_piedra < 65.5:
    print ('pertenece a la era Cenozoica')
elif (Edad_de_piedra > 66 and Edad_de_piedra < 251):
    print('Pertenece a la era Mesozoica')
elif Edad_de_piedra >251 and Edad_de_piedra < 542:
    print('Pertenece a la era Paleozoica')
else:
     print('Pertenece a la era Pre-paleozoica')