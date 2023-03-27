#Inicialización
Primo = True
contador1 = 1
acumulador = 0
#Entradas
cantidadNumeros = int(input('Digite la cantidad de números: '))
while (contador1<=cantidadNumeros):
   contador2=2
   acumuladorPrimo=0
   Primo=True
   contadorPrimo=0
   numero = int(input('Digite el número: '))
   while(Primo and contador2<=numero):
     if((numero % contador2)==0):
      Primo=False
     contador2 = contador2 + 1
   if(Primo):
     acumuladorPrimo = acumuladorPrimo + numero
     contadorPrimo = contadorPrimo + 1
   contador1 = contador1 + 1
print('Acumulado de Primos:', acumuladorPrimo,  'total:', contadorPrimo)