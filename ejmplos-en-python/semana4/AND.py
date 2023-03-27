# inicializacion
edad =0
esEstudiante = False
respEstudiante = 0

# entrada de datos
# bool TRUE or FALSE
respEstudiante = int(input('digite si es estudiante o no TRUE(1) o FALSE(0):'))
edad = int(input('Digite la edad:'))

#proceso<>

if (respEstudiante==1):
    esEstudiante = True
else:
    esEstudiante = False
# proceso
if (edad >= 18 and esEstudiante==True):
    print('Es estudiante y mayor de edad: ')

else:
    if (edad >=18 and esEstudiante==False):
      print('Es mayor a 18 pero no es estudiante')
    
    if (edad <18 and esEstudiante==True):  
      print('Es estudiante pero menor de edad')
    else:   
       print('No es ni estudiante ni mayor de edad')