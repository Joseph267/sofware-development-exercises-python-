costo_metro = 0
ancho = 20 
largo = 150
area = 0
monto = 0

costo_metro = float(input('Ingrese el costo del metro: '))
area = ancho * largo
monto = area * costo_metro

print('El monto a pagar es de: ', monto)