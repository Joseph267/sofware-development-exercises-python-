#Se quiere hacer un programa para un colegio que quiere administrar las becas y los equipos deportivos de
#los estudiantes. Para esto el colegio está haciendo una encuesta a todos los estudiantes de los cinco niveles del
#colegio, en la cual pregunta el nivel en el que se encuentra el estudiante, a cuál equipo quiere pertenecer: baloncesto,
#natación, ajedrez o ninguno, y si el estudiante cuenta con beca o no. En caso de contar con una beca, ésta puede ser
#académica o deportiva, si el estudiante cuenta con beca académica el monto que corresponde a la beca es de 50.000
#colones por mes, pero si el estudiante cuenta con beca deportiva el monto que corresponde a la beca es de 80.000
#colones por mes. 


nivel_pregunta = 0
equipo_eleccion = ''
beca_pregunta = ''
cantidad_estudiantes = 0
i = True
becados_deportivos= 0
becados_academicos=0
becas_academicas = 0
becas_deportivas = 0 
tipo_de_beca = ''
becados=0
no_becados = 0 
nivel_1 = 0
nivel_2 = 0
nivel_3 = 0
nivel_4 = 0
nivel_5 = 0
ajedrez = 0
natacion = 0 
baloncesto = 0
ninguno = 0



while i: 

    
    nivel_pregunta = int(input('en que nivel esta?:'))
    print('ajedrez \nnatacion\nbaloncesto\nninguno')
    equipo_eleccion = input('que equipo elije?:')
    beca_pregunta= input('tiene beca? (s)(n):')
    cantidad_estudiantes +=1


    if beca_pregunta == 's':
        tipo_de_beca = input('cuenta con beca academica(a)  deportiva(d)?')
        if tipo_de_beca == 'a':
            becas_academicas += 50000
            becados+=1
        elif tipo_de_beca == 'd':
            becas_deportivas += 80000
            becados+=1
    else:
        no_becados += 1

    if nivel_pregunta == 1:
        nivel_1+=1
    elif nivel_pregunta == 2:
        nivel_2+=1
    elif nivel_pregunta == 3:
        nivel_3+=1
    elif nivel_pregunta == 4:
        nivel_4+=1
    else:
        nivel_5+=1

    if equipo_eleccion == 'ajedrez':
        ajedrez +=1
    elif equipo_eleccion == 'baloncesto':
        baloncesto +=1
    elif equipo_eleccion == 'natacion':
        natacion+=1
    else:
        ninguno+1

    pregunta_final = input('desea agregar otro estudiante? (s)(n):')

    if pregunta_final == 'n':
        i=False

print('REPORTE FINAL')
print('Estudiantes encuestados:')
print('Nivel 1: ', nivel_1)
print('Nivel 2: ', nivel_2)
print('Nivel 3: ', nivel_3)
print('Nivel 4: ', nivel_4)
print('Nivel 5: ', nivel_5)

print('Porcentaje de estudiantes becados:', (becados/cantidad_estudiantes)*100, "%")
print('Porcentaje de estudiantes no becados:', (no_becados/cantidad_estudiantes)*100, "%")

print('estudiantes en baloncesto:', baloncesto)
print('estudiantes en natación:', natacion)
print('estudiantes en ajedrez:', ajedrez)
print('estudiantes en ningún equipo:', ninguno)

print('Monto mensual por becas deportivas:', becas_deportivas)
print('Monto mensual por becas académicas:', becas_academicas)

print('Monto anual otorgado por becas deportivas:', becas_deportivas*11)
print('Monto anual otorgado por becas académicas:', becas_academicas*11)


    