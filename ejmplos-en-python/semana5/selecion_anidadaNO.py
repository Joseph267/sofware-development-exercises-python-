puntos = 0.0


puntos = float(input('ingrese los puntos:'))

if puntos >= 90:
    nota = 'A'
else:
    if puntos >= 80:
        nota = 'B'
    else: 
        if puntos >= 70:
            nota = 'C'
        else:
            nota = 'D'
print('su nota fue de:',nota)    


