#Haga una función que reciba una distancia en metros y calcule el equivalente en pies y otra función que recibe una
#distancia en metros y calcule el equivalente en pulgadas. Pruebe las dos funciones en un programa. Tenga en
#cuenta que:

import math
metros = 0 
metros = float(input('de los metros:'))

def pies(metros_pies):
    p = 0 
    p = metros * 393701
    return p
def pulgadas(metros_pulgadas):
    pul = 0 
    pul = metros * 328084
    return pul

pies_resultado = pies(metros)
print ('la cantidad de metros en pies es de',pies_resultado)

pulgadas_resultado = pulgadas(metros)
print ('la cantidad de metros en pulgadas es de',pulgadas_resultado)