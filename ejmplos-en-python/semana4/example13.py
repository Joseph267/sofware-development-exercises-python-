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

if nota1 > 70:
    if nota2 > 70:
        if nota3 > 70:
            if nota4 > 70:
                sumatoria = nota1+nota2 + nota3 + nota4
                promedio = sumatoria / total_materias
                print ('Tiene derecho a la beca')
            else:
                if (promedio >90) and (nota1>80):
                    print ('Por tener promedio mayor a 90 y notas superiores a 80 tiene derecho a beca')
                else:
                    if(promedio >=85) and  (asistente == 0):

                        if  (nota_como_asistente== 0 ):
                            print ('debido a  que su promedio es  igual o mayor a 85 y sucalificacion como asistente es A tiene beca')
                        else:
                            if (nota_como_asistente== 1 ):
                                print ('debido a  que su promedio es  igual o mayor a 85 y sucalificacion como asistente es B tiene beca')
                            else: 
                                (nota_como_asistente>= 2 )
                                print ('por el  la nota obtenida como  asistente no califica para la beca')
                    else:
                        print ('no aplica para beca')
        else:
            print ('no aplica para beca')
    else:
        print ('no aplica para beca')
else:
    print ('no aplica para beca')


