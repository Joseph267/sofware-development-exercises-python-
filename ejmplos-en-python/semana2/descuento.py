costo = 0
dia = ''
costo = int(input('Ingrese el costo de la entrada: '))
dia = input('Ingrese el nombre del día de la semana: ')
if(dia == 'miércoles'):
    costo = costo / 2
print(costo)