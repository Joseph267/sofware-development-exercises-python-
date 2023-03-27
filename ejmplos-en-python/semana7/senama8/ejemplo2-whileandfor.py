limite = int(input('Ingrese el número deseado: '))

for numero in range(limite):
 print(f'--- Tabla del {numero} ---')
 contador=0
 while(contador<10):
  print(f'{numero} x {contador} = {numero * contador}')
  contador+=1
 print('--- --- --- --- ---')