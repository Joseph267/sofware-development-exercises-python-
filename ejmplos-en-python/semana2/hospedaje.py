cant_noches = 0
costo_noche = 100.0
porc_desc = 0.05
subtotal = 0.0
descuento = 0.0
total = 0.0

cant_noches= int(input('Ingrese la cantidad de noches:'))
subtotal= cant_noches * costo_noche
descuento = subtotal * porc_desc
total = subtotal - descuento
print('el total de hospedaje es de:', total, 'dolares')