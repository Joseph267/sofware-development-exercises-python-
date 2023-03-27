saldo_cuenta=0
monto_retiro=0
i= True
saldo_cuenta= int(input('Por favor escriba el saldo inicial: '))
while i:
    if (saldo_cuenta >0) and saldo_cuenta <= saldo_cuenta:
        monto_retiro= int(input('Por favor escriba su retiro: '))
        subtotal = saldo_cuenta - monto_retiro
        print ('sus fondos en la cuenta son de', subtotal, 'colones')
        saldo_cuenta-= monto_retiro

    else:
        i= False 
        print('Se terminaron sus fondos.')
