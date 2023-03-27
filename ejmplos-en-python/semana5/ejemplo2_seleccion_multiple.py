
salario = 0.0
max_horas_extra = 0
codigo_puesto = 0


print('1. Ingeniero Civil')
print('2. Ingeniero de Software')
print('3. Ingeniero Eléctrico')
print('4. Ingeniero Industrial')


codigo_puesto =  int(input('Digite el tipo de ingeniero: '))
total_horas_extra =  int(input('Digite el total de horas extra: '))

if(codigo_puesto == 1):
    salario_base = 750000
    monto_horas_extra = 6250
elif(codigo_puesto == 2):
    salario_base = 1300000
    monto_horas_extra = 10800
elif(codigo_puesto == 3):
    salario_base = 675000
    monto_horas_extra = 5625
elif(codigo_puesto == 4):
    salario_base = 1150000
    monto_horas_extra = 0
else:
    salario_base = 0
    monto_horas_extra = 0

if total_horas_extra >= max_horas_extra:
    salario_total = salario_base + (total_horas_extra * monto_horas_extra)
else:
    salario_total = salario_base + max_horas_extra * monto_horas_extra

print(salario_total)

