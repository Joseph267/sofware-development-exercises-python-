#A usted le piden realizar un programa que, recibiendo el día, el mes y el año de la fecha de hoy, calcule e imprima
#la fecha del día de mañana.

Dia_hoy = ''
mes = 0
anno = 0

Dia_hoy = int(input('igrese el dia de hoy:'))
mes = input('igrese el mes actual:')
anno = int(input('igrese el ano actual:'))

if Dia_hoy >=31:
    Dia_hoy - 30
    print(Dia_hoy + 1,mes + 1,anno)

if Dia_hoy >=1:
    print(Dia_hoy + 1,mes,anno)


#if Dia_hoy >=31:
    Dia_hoy - 30
    print(Dia_hoy + 1,mes,anno)