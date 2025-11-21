
""" 3. Tienda “LoopShop” – Descuentos acumulados
Como vendedor, quiero una función aplicar_descuentos() que pida varios precios hasta que el usuario escriba 0.
Si el precio supera 50.000, aplicar 10% de descuento.
Al final, mostrar la suma total de las compras con descuento. """


def descuentos():
    listaprecios =[]
    contador = 0

    while True:
        val = int(input("ingresar un valor, para salir marque cero o 0: "))
        
        if val != 0:
            print("hacer todooo")
            listaprecios.append(val)
        else:
        #print("se fuee")
            break

    for i in (listaprecios):
        contador = contador + i

    print(contador)

    if contador > 50000:
        descuento = contador * 0.10
        total = contador - descuento
        print(f"El Total a pagar es: {total} | el descuento es: {descuento} ")



descuentos()