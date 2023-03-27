#En una empresa de venta de productos tecnológicos se tienen N cantidad de sucursales, se requiere
#saber cuánta es la cantidad de ventas a la semana de cada sucursal con su nombre, así como el total
#generado por la empresa. Considere que se trabajan 6 días a la semana y todos los días el monto de las
#ventas es diferente


N = int(input('Digite la cantidad de sucursales: '))
ventEmpresa=0
for numero in range(N):
 print('--- --- --- --- ---')
 print(f'Digite la información para la empresa{numero+1} ---')
 contador=0
 ventaSucursal=0
 while(contador<6):
  ventaSucursal += int(input(f'Digite el valor vendido en el día {contador+1}  '))
  contador+=1
 ventEmpresa+=ventaSucursal 
 print('--- --- --- --- ---')
print(f'Las ventas de la Empresa son de{ventEmpresa} ---')

