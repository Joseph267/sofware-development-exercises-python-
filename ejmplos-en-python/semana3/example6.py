#validar si estudiante perdio curso 

nota = 0.0

nota = float(input ('Ingrese  la nota obtenida en este curso: '))

if nota <70:
    print ('con la nota indicada usted no aprueba este curso.')
else:
    print ('con la nota indicada usted aprueba el curso.')