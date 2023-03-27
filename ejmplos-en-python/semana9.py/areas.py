import math
radioLote1 = 0.0
ladoLote2 = 0.0
areaLote1 = 0.0
perimetroLote1 = 0.0
areaLote2 = 0.0
perimetroLote2 = 0.0
PI = math.pi


radioLote1 = float(input('Por favor escriba el radio del Lote 1:'))
ladoLote2 = float(input('Por favor escriba el lado del Lote 2: '))


#Definición de las rutinas
def calcularAreaCirculo(pRadio):
    area = 0
    area = PI * pRadio * pRadio
    return area
def calcularPerimetroCirculo(pRadio):
    perimetro = 0
    perimetro = 2 * PI * pRadio
    return perimetro
def calcularAreaCuadrado(pLado):
    area = 0
    area = pLado * pLado
    return area
def calcularPerimetroCuadrado(pLado):
    perimetro = 0
    perimetro = pLado * 4
    return perimetro



# Flujo principal
if (radioLote1 < 0 or ladoLote2 < 0):
    print('Por favor ingrese valores positivos.')
else:
    areaLote1 = calcularAreaCirculo(radioLote1)
    perimetroLote1 = calcularPerimetroCirculo(radioLote1)
    print(f'El área del Lote 1 es: {areaLote1}')
    print(f'El perímetro del Lote 1 es: {perimetroLote1}')    
    areaLote2 = calcularAreaCuadrado(ladoLote2)
    perimetroLote2 = calcularPerimetroCuadrado(ladoLote2)
    print(f'El área del Lote 2 es: {areaLote2}' )
    print(f'El perímetro del Lote 2 es: {perimetroLote2}' )