# inicializacion
edad =0
esEstudiante = False
respEstudiante = 0
# entrada de datos
# bool TRUE or FALSE
respEstudiante = int(input('digite si es estudiante o no TRUE(1) o FALSE(0):'))
edad = int(input('Digite la edad:'))

#proceso<>
#podemos hagarrar el input para trasformalo a verdadero o falso y asi hacer bien el boolean 
if (respEstudiante==1):
    esEstudiante = True
else:
    esEstudiante = False

print(esEstudiante)
if (edad >= 18 or esEstudiante):
    print('Mayor de edad o Estudiante o ambos')
else:
    print('No es estudiante mayor de edad')