#cuidadno puede votar si tiene mas de 18 
edad= 0

edad= int(input ("Ingrese su edad aqui: "))

if edad >= 18:
    print ("Es mayor de edad y si puede votar.")
else:
    print ('No puede votar porque no cumpple con la edad minima para ese proposito.')