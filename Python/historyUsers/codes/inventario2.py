
"""  Inventario = [ {
        "nombre" : '',
        'precio' : 0.0,
        'cantidad' : 0
        }  ] """
Inventario =[]

def agregarProducto():
            while True:
                nombreProducto = input("ingrese el nombre de un producto: ")
                
                while True:
                    precioProducto = float(input("ingrese el precio del producto: "))
                    if precioProducto > 0:
                        #print(" valor correcto")
                        #va el push al diccionario
                        break
                    else:
                        print("---- El precio no puede ser negativo o 0 -----\n")
                    
                
                while True:
                    cantidadProducto = int(input("Ingrese la cantidad: "))
                    if cantidadProducto > 0:
                        #print("cantidad correcta")
                        #va el push al diccionario
                        break
                    else:
                        print("---- El cantidad no puede ser negativo o 0 -----\n")
                

                producto= {"nombre": nombreProducto, "precio": precioProducto, "cantidad": cantidadProducto }
                Inventario.append(producto)
                break

def mostrarInventario():
     #print("logica para mostrar el inventario")
        
        if not Inventario:
            print("El inventario esta vacio")
        else:
            for i,producto in enumerate(Inventario, start = 1):
                print(f"{i} | El nombre del producto es {producto["nombre"]} | El valor es {producto["precio"]} | la cantidad es {producto['cantidad']}     ")
                
def calcularEstadistica():
    if not Inventario:
            print("El inventario esta vacio")
    else:
        sub =0            
        total = 0
        for i in Inventario:
            sub = sub + (i["precio"] * i["cantidad"])
            total = sub
            
        print(f"la suma total de la factura es : {total} | ")

""" def cerrarPrograma():
    print("Nos vemos pronto")
    break """





while True:

    print("******************************")
    selector = int(input(f"\n 1. Agregar producto\n 2.Mostrar inventario\n 3.Calcular estadísticas\n 4.Salir\n --->"))
    print("******************************")
    if selector == 1:
            agregarProducto()
    elif selector == 2:
        mostrarInventario()

    elif selector== 3:
       calcularEstadistica()

    else:
        print("Nos vemos pronto")
        break

