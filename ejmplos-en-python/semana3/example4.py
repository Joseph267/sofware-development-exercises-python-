# entradas 


edad_ana = 0 
edad_abuela_ana = 0
edad_abuelo_ana = 0
anno_de_matrimonio = 0
anno_actual = 0 

# proceso

anno_de_matrimonio = int(input('ingrese el ann de matrimonio: '))
anno_actual = 2023
edad_abuelo_ana = anno_actual - anno_de_matrimonio + 25
edad_abuela_ana = edad_abuelo_ana - 7
print ('La abuela de ana tiene: ', edad_abuela_ana, 'annos de edad')