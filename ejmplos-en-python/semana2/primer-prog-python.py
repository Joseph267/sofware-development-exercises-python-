nombre = ''
estatura = 0.0
peso = 0.0
msj = ''

nombre = input('Ingrese su nombre: ')
estatura = float(input('Ingrese su estatura en metros: '))
peso = float(input('Ingrese su peso en kilos: '))

imc = peso / pow(estatura, 2)
msj = 'Saludos ' + nombre + ' su imc es de : '

print(msj)
print(imc)