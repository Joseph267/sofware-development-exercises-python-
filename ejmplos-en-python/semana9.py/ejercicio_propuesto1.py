import math
hipotenusa = 0.0
lado1 = 0.0
lado2 = 0.0
lado1 = float(input('Por favor escriba el lado 1:'))
lado2 = float(input('Por favor escriba el lado 2: '))
#Definición de las rutinas
def calcularHipotenusa(l1, l2):
    h = 0
    h = math.sqrt(math.pow(l1,2) + math.pow(l2,2))
    return h
    #print('La hipotenusa es:', h)
hipotenusa = calcularHipotenusa(lado1,lado2)
print(f'El valor de la hipotenusa es: {hipotenusa}' )