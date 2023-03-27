#Haga un programa que reciba como entrada la cantidad de exámenes realizados por un estudiante en
#un curso, y debe calcular la nota del curso que se obtiene del promedio de todos los exámenes. El
#programa deberá determinar además, si el estudiante aprobó, debe ir a ampliación o reprobó el curso.
#Un estudiante aprueba el curso si su nota es mayor o igual a 70, debe hacer ampliación si su nota es
#inferior a 70 pero superior o igual a 60, o reprueba el curso si la nota es menor que 60

cantidad_examenes = 0
promedio_examenes = 0.0
examenes = 0
promedio = 0.0
examen = 0

cantidad_examenes = int(input('ingrese la cantidad de examenes:'))

while(examenes <= cantidad_examenes):
    examen = int(input('digite nota de examen:'))
    promedio_examenes += examen
    promedio = promedio_examenes/cantidad_examenes
print(promedio)