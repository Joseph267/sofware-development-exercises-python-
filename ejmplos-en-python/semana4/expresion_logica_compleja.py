# inicializacion
edad =0
esEstudiante = False

# entrada de datos
# bool TRUE or FALSE
esEstudiante = bool(input('digite si es estudiante o no TRUE o FALSE:'))
edad = int(input('Digite la edad:'))

#proceso<>

if (edad >= 18 or esEstudiante==True):
    print('Mayor de edad o Estudiante o ambos')
else:
    print('No es estudiante mayor de edad')