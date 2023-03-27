#programa que determine si un estudiante de una institución universitaria es candidato
#a que le den una beca. Un estudiante puede optar por una beca solamente si lleva el bloque de cuatro materias
#completo, y no perdió ninguna materia, por lo que el sistema siempre va a recibir las notas de las cuatro materias y
#todas las notas van a ser superiores a 70. El estudiante tiene derecho a la beca si el promedio de las notas de las
#materias del cuatrimestre es igual o superior a noventa, y si ninguna nota está por debajo de 8. También podría
#tener derecho a la beca si el promedio de las materias del cuatrimestre es igual a superior a 85, fue asistente
#durante el cuatrimestre y la calificación que se le otorgó como asistente fue de una A o una B. Si su calificación
#como asistente fue de una C no tiene derecho a beca, sin importar el promedio.

materia1 = 0
materia2 = 0
materia3 = 0
materia4 = 0
sumatoria_total = 0
total_nota = 0
cantidad_materias = 0
asistente = ''


cantidad_materias = int(input('ingrese la cantidad de materias a llevar:'))
sumatoria_total = (materia1 + materia2 + materia3 + materia4)
 
materia1 = int(input('ingrese nota 1:'))
materia2 = int(input('ingrese nota 2:'))
materia3 = int(input('ingrese nota 3:'))
materia4 = int(input('ingrese nota 4:'))

asistente = input('ingrese nota de asistencia A,B o C:')

total_nota = (materia1 + materia2 + materia3 + materia4)

promedio = total_nota/cantidad_materias

print(promedio)

if (promedio >= 85) and (sumatoria_total >= 280):
    if (asistente == 'A' or asistente == 'B'):
        print('gano la beca')
    else:
        print('perdio la beca')