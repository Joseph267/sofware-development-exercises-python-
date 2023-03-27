#entradas para el triangulo 

ladoa=0.0
ladob= 0.0
ladoc= 0.0


#asignacion

ladoa= int(input('Ingrese el tamanno de este lado: '))
ladob= int(input('Ingrese el tamanno de este lado: '))
ladoc= int(input('Ingrese el tamanno de este lado: '))

#proceso 

if (ladoa + ladob) > ladoc:
    if (ladob+ladoc)> ladoa:
        if (ladoc+ladoa) > ladob:
            print ('Los valores brindados son ',ladoa, ladob, ladoc, 'y estos numero si pueden formar un triangulo')
        else:
            print ('Valores no compatibles para formar el traingulo')
    else:
        print ('Valores no compatibles para formar el traingulo')
else:
    print ('Valores no compatibles para formar el traingulo')
