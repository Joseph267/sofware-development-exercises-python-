#calcular si estudiante puede reciber beca 

total_materias= 0
nota1=0.0
nota2=0.0
nota3=0.0
nota4=0.0
sumatoria=0.0
promedio=0.0

#proceso


asistente= int(input ('Indique si fue assistente digitando (0 para Si) o (1 para No) '))
nota_como_asistente= int(input('Indique la nota obtenida como asistente (0 para A) (1 para B) (2 para C) o  un numero de 3 a 9  para descartar'))

total_materias = int(input('Ingrese el la cantidad de materias: '))
nota1= int(input('Ingrese la nota: '))
nota2= int(input('Ingrese la nota: '))
nota3= int(input('Ingrese la nota: '))
nota4= int(input('Ingrese la nota: '))

if (nota1>70, nota2>70, nota3>70, nota4 > 70):
    print (nota1,nota2,nota3,nota4)
    sumatoria= nota1+nota2 + nota3 + nota4
    print (sumatoria)
    promedio = sumatoria / total_materias
    print (promedio)
    print ('Tiene derecho a la beca')
elif(promedio >90) and (nota1,nota2,nota3>60):
    print ('Por tener promedio mayor a 90 y notas superiores a 80 tiene derecho a beca')
elif(promedio >85) and (asistente ==0):
    nota_como_asistente <=1
    print('como fue asistente y obtuvo nota superio a B tiene beca')
else:
    print ('No tiene ninguno de los criterios para aplicar por la beca')

