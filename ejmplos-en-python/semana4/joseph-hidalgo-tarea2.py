#Entradas
puntos = 0
requisitos = 0
costo1 = 5000
costo2 = 10000
BCR = 4200

puntos = int(input('digite la cantidad de puntos acumulados por infracciones:'))

#Proceso 

if puntos >= 12:
    print('.')
    print('Su licensia ha sido suspendida y no puede ser renovada')
    print('.')
    

elif puntos == 6:
    print('su licensia ha sido suspendida')

if puntos <4:
    print('La renovación tiene un costo de', costo1 ,'colones, y la licencia nueva tendrá vigencia por 6 años.')
if puntos >4 and puntos < 9:
    print('La renovación tiene un costo de', costo2 ,'colones, y la licencia nueva tendrá vigencia por 4 años.')

if puntos == 9 or puntos == 10 or puntos == 11:
    print('La renovación tiene un costo de', costo2, 'colones, y la licencia nueva tendrá vigencia por 3 años.')

requisitos = int(input('Si gusta conocer los requisitos para la renovacion de licencia por favor digite 1:')) 

compra =  int(input('Si gusta Realizar el pago mediante el Banco de Costa rica por favor digite 1 si no digite 2:')) 



if compra == 1 and puntos <4:
    print('El total a cobrar sera de ',costo1 + BCR,' colones' )
if compra == 1 and puntos >4 and puntos < 9:
    print('El total a cobrar sera de ',costo2 + BCR,' colones' )
if compra == 1 and (puntos == 9 or puntos == 10 or puntos == 11):
    print('El total a cobrar sera de ',costo2 + BCR, 'colones,' )




if compra == 2 and puntos <4:
    print('El total a cobrar sera de 5000 colones' )
if compra == 2 and puntos >4 and puntos < 9:
    print('El total a cobrar sera de 10000 colones' )
if compra == 2 and (puntos == 9 or puntos == 10 or puntos == 11):
    print('El total a cobrar sera de 10000 colones,' )


print('.')
print('.')
print('.')


# salidas
if requisitos == 1:
    print (" - Documento de indentidad al Dia y en buen estado.\n - Dictamen medico Digital y vigente.\n - Pagar todas las multas de transito pendientes.\n - No haber llegado a 12 puntos o mas por infracciones de transito.\n - En caso de tener 12 puntos o mas  su licencia sera suspendida y no podra renovar.")    
else:
    print('gracias por su visita')





