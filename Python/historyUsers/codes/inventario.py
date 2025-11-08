

#ingreso de los datos y sus tipos
nombre = input("ingresa el nombre del producto: ")
precio = float(input("Ingresar el precio: "))
cantidad = int(input("ingrese la cantidad a comprar: "))






costo_total = precio * cantidad




print("----------------------")
print(" -- La Factura es --")
print(f'Nombre del producto : {nombre}\nPrecio unitario : {precio}\nCantidad : {cantidad}\nCosto total calculado : {costo_total}')