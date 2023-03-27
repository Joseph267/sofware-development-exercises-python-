#Determinar si un ciudadano puede votar. Un ciudadano puede votar si ya cuenta con 18
#años cumplidos. El programa recibe la edad del ciudadano.


edad = 0

edad = int(input('ingrese su edad:'))

if edad >= 18:
    print('puede votar')
else:   
    print('no puede votar')