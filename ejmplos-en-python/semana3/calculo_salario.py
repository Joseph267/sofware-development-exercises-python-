# Entrada
horasTrabajadas = 0.0
precioHora = 0.0 

horasTrabajadas = int(input('Digite las horas Trabajadas:'))
precioHora = int(input('Digite el precio por Hora:'))

# Proceso

calculoSalario = 0.0
if horasTrabajadas > 40:
    horasExtras = horasTrabajadas-40     
    pagoHoraExtra = precioHora * 1.5
    calculoSalario = 40*precioHora + (pagoHoraExtra * horasExtras) 
else:
    calculoSalario = horasTrabajadas*precioHora

# Salida
print(calculoSalario)




