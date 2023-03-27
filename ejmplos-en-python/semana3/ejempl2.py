cant_noches = 0
costo_noche = 0.0
porc_desc = 0
descuento = 0.0
subtotal_hospedaje = 0.0
total_hospedaje = 0.0
cant_noches = int(input('Ingrese la cantidad de noches a hospedarse: '))
costo_noche = float(input('Ingrese el costo de la estadía por noche: '))
if (cant_noches > 4):
    porc_desc = 0.05
    subtotal_hospedaje = costo_noche * cant_noches
    descuento = subtotal_hospedaje * porc_desc
    total_hospedaje = subtotal_hospedaje - descuento
    print('El costo total del hospedaje es:', total_hospedaje)
else:
    porc_desc = 0
    subtotal_hospedaje = costo_noche * cant_noches
    descuento = subtotal_hospedaje * porc_desc
    total_hospedaje = subtotal_hospedaje - descuento
    print('El costo total del hospedaje es:', total_hospedaje)