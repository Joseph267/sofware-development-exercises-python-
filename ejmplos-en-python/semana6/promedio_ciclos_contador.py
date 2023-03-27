#Cuando un usuario digite que desea calcular el promedio de 10
#números, el algoritmo debe solicitar 10 números enteros al usuario
#por teclado y obtener el promedio total de estos. Si el usuario desea
#calcular el promedio de 6 números, solo se deben solicitar 6 números

sumatotal = 0
contador = 1
promedio = 0
cantidad_numeros = 0

cantidad_numeros = int(input('digite la cantidad de numeros a utilizar'))

while (contador <= cantidad_numeros):
  numero = int(input('digite el numero:'))
  sumatotal += numero
  contador += 1
print('el promedio es:',sumatotal/cantidad_numeros)
