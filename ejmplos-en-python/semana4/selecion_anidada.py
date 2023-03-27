
#declaratoria
ingles = 'I'
portugues = 'P'
edadMinima = 18
ExperienciaRequerida = 1

#entrada
idioma = (input('ingrese Idioma (I) para Inglés ó (P) para Portugués:'))
edad = int(input('Ingrese edad: '))
experiencia = int(input('Ingrese años de experiencia: '))

#proceso/salida
if (idioma == 'I' or idioma == 'P'):
    if (edad >= edadMinima):
        if (experiencia >= experiencia):
            print('Si califica.')
        else:
            print('No califica')
    else:
        print('No califica.')
else:
    (idioma != 'I' or idioma != 'P')
    print('No califica.')
