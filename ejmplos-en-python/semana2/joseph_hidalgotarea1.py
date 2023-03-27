#En este ejemplo vamos a suponer que el trabajador gana 350.000 colones mensuales

salario_mensual = 350.000
total = 0.0
salario_pendiente = 0
preaviso = 0.0
cesantia = 0.0
aguinaldo_proporcional = 0.0
vacaciones_no_gozadas = 0.0


#el monto del preaviso corresponde a un mes de salario ya que el trabajador no va a laborar los días de preaviso y que el trabajador tiene dos años de
#trabajar en la empresa
preaviso = 350.000

salario_pendiente = int(input('Ingrese la cantidad de meses de salario pendientes:'))
salarios_pendientes = salario_pendiente * salario_mensual

#el trabajador no ha tomado vacaciones en
#el último año, por lo que de acuerdo con la ley este monto se obtiene dividiendo entre 30 el salario mensual y
#multiplicándolo por 14.
vacaciones_no_gozadas = (salario_mensual / 30 ) * 14 

#el trabajador recibió en Diciembre su aguinaldo completo, por lo que el aguinaldo
#proporcional en este caso se calcula teniendo en cuenta sólo el monto del último mes (mes de Enero)

aguinaldo_proporcional = salario_mensual / 12 
cesantia = ((salario_mensual / 30)* 20)*2

total = salarios_pendientes + vacaciones_no_gozadas + aguinaldo_proporcional + cesantia + preaviso
print('El total de la liquidazion seria de', total,'colones')


# comprovacion del codigo, al final todo deberia sumar 1,359.000 
#350.000 = salario mensual pendiente 
#466.000 = cesantia
#29.000 = aguinaldo proporcional
#163.000 = vacaciones no gozadas 
#350.000 = preaviso 
