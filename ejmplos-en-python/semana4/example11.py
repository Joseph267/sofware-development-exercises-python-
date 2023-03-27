# calcular fecha de manana con datos del dia de hoy 

dia_de_mes = 0
mes= 0
anno= 0


#proceso

dia_de_mes = int (input("Ingrese  el dia del mes: "))
mes= int (input('Ingrese el mes que estamos en numero de el 1 a el 12: '))
anno = int (input('Ingrese el anno que estamos: '))

if (dia_de_mes >=1 and dia_de_mes<=30):
    if (mes>=1 and mes<=12):
        dia_de_manana= dia_de_mes + 1
    print ("la fecha de manana sera {0}/{1} de {2}".format(dia_de_manana,mes,anno))
else:
    dia_de_manana = ("No es posible hacer el calculo del dia de la fecha de manana")
print (dia_de_manana)