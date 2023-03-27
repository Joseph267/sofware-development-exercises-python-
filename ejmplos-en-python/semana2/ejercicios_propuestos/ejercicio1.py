#Determinar si una persona tiene fiebre. Una persona tiene fiebre si la temperatura es mayor
#a 37 grados. El programa recibe como información la temperatura de la persona.

temperatura = 0

temperatura = int(input('ingrese la temperatura:'))

if temperatura > 37:
    print('tiene fiebre')
else:   
    print('no tiene fiebre')