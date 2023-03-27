numero = 0
numero = int(input('Por favor teclee un número para saber si es impar: '))
if (numero % 2 != 0):
    print('El número: ' , numero , 'es impar')
else:
    print('El número: ' , numero , 'es par')




# tambien sepuede hacer asi 

#entrada
numero = 0
#proceso y salida
numero = int(input('Por favor teclee un número para saber si es impar y mayor a 10: '))
if (numero>10):
    if (numero % 2 != 0):
     print('El número: ' , numero , 'es impar')
    else:
     print('El número: ' , numero , 'es par')
else:
     print('El número no se evalua: ' , numero)