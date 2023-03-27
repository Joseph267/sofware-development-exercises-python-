total_estudiantes = 0
becados = 0
no_becados = 0
equipos = ''
becas_deportivas = 0
becas_academicas = 0
baloncesto=0
natacion=0
ajedrez=0
no_equipo=0
nivel1=0
nivel2=0
nivel3=0
nivel4=0
nivel5=0



i=True
while i:
    nivel = int(input('Ingrese el nivel del estudiante entre (1/5): '))
    equipo = input('Ingrese el equipo al que quiere pertenecer el estudiante (baloncesto, natación, ajedrez o ninguno): ')
    beca = input('¿Tiene beca el estudiante? (s/n): ')
    total_estudiantes += 1



    if beca == 's':
        tipo_beca = input('¿La beca es académica o deportiva? (a/d): ')
        if tipo_beca == 'a':
            becas_academicas += 50000
            becados += 1
        elif tipo_beca == 'd':
            becas_deportivas += 80000
            becados += 1
    else:
        no_becados += 1
    
   
    if nivel == 1:
        nivel1 += 1
    elif nivel == 2:
        nivel2 += 1
    elif nivel == 3:
        nivel3 += 1
    elif nivel == 4:
        nivel4 += 1
    else:
        nivel5 += 1

    if equipo == 'baloncesto':
        baloncesto +=1
    elif equipo == 'natacion':
        natacion +=1
    elif equipo == 'ajedrez':
        ajedrez  += 1
    else:
        equipo== 'ninguno'
        no_equipo += 1

    respuesta = input("¿Quieres agregar otro estudiante? (s/n): ")
    if respuesta == "n":
        i=False

print("Total de estudiantes encuestados: ")
print("Nivel 1: ", nivel1)
print("Nivel 2: ", nivel2)
print("Nivel 3: ", nivel3)
print("Nivel 4: ", nivel4)
print("Nivel 5: ", nivel5)

print("Porcentaje de estudiantes becados:", (becados/total_estudiantes)*100, "%")
print("Porcentaje de estudiantes no becados:", (no_becados/total_estudiantes)*100, "%")

print("Monto total mensual otorgado por becas deportivas:", becas_deportivas)
print("Monto total anual otorgado por becas deportivas:", becas_deportivas*11)

print("Monto total mensual otorgado por becas académicas:", becas_academicas)
print("Monto total anual otorgado por becas académicas:", becas_academicas*11)

print("Total de estudiantes en baloncesto:", baloncesto)
print("Total de estudiantes en natación:", natacion)
print("Total de estudiantes en ajedrez:", ajedrez)
print("Total de estudiantes en ningún equipo:", no_equipo)