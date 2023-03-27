#Haga un programa que lea todos los retiros que un usuario quiere hacer de su cuenta
#bancaria, hasta que la cuenta llegue a cero o se quiera hacer un retiro mayor al saldo de la
#cuenta. Para esto usted debe leer del usuario el saldo inicial de la cuenta y cada uno de los
#retiros que el usuario quiera hacer, hasta que se cumpla la condición mencionada. Ejemplo:
#si el saldo inicial y los retiros del usuario son los siguientes, el programa se comporta de
#esta manera


monto = 0 
contador = 0
subtotal = 0 
monto_inicial = 0

monto_inicial = int(input('digite la cantidad de dinero en la cuenta'))

while (subtotal <= monto_inicial):       
    retiro = int(input('digite el monto a retirar'))
    subtotal = monto_inicial - retiro
    print ('sus fondos en la cuenta son de', subtotal, 'colones')
    if subtotal == 0:
        print ('ya no tiene fondos')
else:
    print ('monto no valido')