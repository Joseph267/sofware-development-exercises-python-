#precio de cada producto con el 13% de iva 
#ejemplo  

producto = ""
impuestoIVA = 0.0
total_IVA = 0.0


producto = input("ingrese el nombre del producto: " )
precio_producto = float(input("Ingrese el precio: "))
impuestoIVA =0.13
total_IVA = precio_producto * impuestoIVA
monto_total = precio_producto + total_IVA

print ("producto seleccionado: ", producto)
print ("IVA  : ", total_IVA)
print ("el monto total a pagar es: ", monto_total ) 


