
valorProducto = 2000

unidades = int(input("Ingrese la cantidad de productos: \n"))

if unidades >= 0 and unidades <= 10:

    descuento = 0.05
    subtotal = unidades * valorProducto
    total = subtotal -(subtotal*descuento)
    print("primer total",total)
    if total <= 50000:
        envio = 5000
        total = total + envio
        print("valor 1 dentro de if 1",total)

elif unidades >= 30:
    descuento = 0.15
    subtotal = unidades * valorProducto
    total = subtotal -(subtotal*descuento)
    print("segundo total",total)
    
    if total <= 50000:
        envio = 5000
        total = total + envio
        print("valor 2 dentro de if 2",total)

else:
    total= unidades * valorProducto
    print("valor 3",total)
    