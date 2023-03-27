#haga un programa que dado el número de capítulos de un libro leídos por día, imprima el
#total de capítulos leídos y el número de días en que terminó el libro. El programa debe leer
#el número de capítulos leídos por día hasta que el usuario termine el libro. Ejemplo: si los
#datos dados por el usuario son los siguientes, el programa se comporta de esta manera:


capitulos_diarios = 0 
dias = 0
pregunta = ''
suma_total = 0 


while (pregunta != 'S' or  pregunta != 's'):
    capitulos_diarios= int(input('cuantos capitulos leyo hoy?:'))
    pregunta = (input('termino el libro? (S) o (N):'))
    suma_total += capitulos_diarios
    dias += 1
print ('Felicidades, usted leyó un libro de ', suma_total, ' capitulos en', dias, 'dias')

