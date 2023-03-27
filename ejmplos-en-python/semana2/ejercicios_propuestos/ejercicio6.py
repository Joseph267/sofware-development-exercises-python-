#El Gobierno ha decidido que todas aquellas personas que tienen un salario igual a superior
#a un millón de colones deben pagar un impuesto del 10%. Calcule el salario neto de un
#trabajador. El sistema recibe el salario del trabajador como entrada.


salario = 0 
impuesto = 0.1

salario =  int(input('ingrese su salario:'))

if salario > 100:
    salario_impuesto = salario - (salario * impuesto)
    print('su salario es:',salario_impuesto)
else:
    print('su salario es:', salario)

