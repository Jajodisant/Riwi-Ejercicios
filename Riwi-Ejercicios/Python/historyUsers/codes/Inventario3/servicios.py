
Inventario =[]

def agregarProducto():


    while True: # Permite que cada uno de los productos se pidan nuevamente
        
      
        while True:       
                nombreProducto = input("ingrese el nombre de un producto: ").lower()  #solicita un nombre y lo transforma a minusculas               
                for letra in nombreProducto:
                    if letra in "áéíóú": 
                        print("No se permiten tildes")
                        break 

                    elif not letra.isalnum() and letra != " ":  
                        print("No se permiten caracteres especiales")
                        break 
                else: # se ejecuta solo si el for continua, en este caso se pone para salir del while
                     break # sale del while
       
        while True:
            try:
                precioProducto = float(input("ingrese el precio del producto: "))           
                if precioProducto > 0:
                    break                  
                else:
                    precioProducto = round(precioProducto,2)
            except ValueError:
                print("solo valores numericos")

        while True:
            cantidadProducto = int(input("Ingrese la cantidad: "))
            if cantidadProducto > 0:
                break
            else:
                print("---- El cantidad no puede ser negativo o 0 -----\n")

        #se crea un dicionario para pushearlo o ingresarlo dentro del inventario
        guardar(nombreProducto,precioProducto,cantidadProducto)
        break


def guardar(nombre,producto,cantidad):
    producto= {
            "nombre": nombre,
            "precio": producto,
            "cantidad": cantidad
            }
    Inventario.append(producto) # se agrega el diccionario dentro de la lista o array
    print("\n ** ** ** Producto agregado correctamente! ** ** ** \n ")


def mostrarInventario():
    if not Inventario:# veriffica si el inventario esta vacio
        print(" # * # * El inventario esta vacio * # * #")
    else:
        for i,producto in enumerate(Inventario, start = 1):#enumerate recorre una lista y me devuelve su key-value -- :.2findica que solo muestre 2 valores despues del punto
            print(f"{i} | El nombre del producto es {producto["nombre"]} | El valor es {producto["precio"]:.2f} | la cantidad es {producto['cantidad'] }\n   ")

def buscar():
    
    try:
        if not Inventario:
            print(" # * # * El inventario esta vacio * # * #")
        else:
            mostrarInventario()
            id_buscar = int(input("Ingrese el ID del producto a buscar: "))
            if 1 <= id_buscar <= len(Inventario):
                producto = Inventario[id_buscar - 1]  #resta 1 para ajustar al indice de la lista
                print(f"El producto encontrado es: {producto['nombre']} | Precio: {producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
            else:
             print("ID de producto no válido.")
    except ValueError:
        print("ID invalido. Por favor ingrese un numero valido.")
            
def actualizar():
    try:
        if not Inventario:
            print(" # * # * El inventario esta vacio * # * #")
        else:
           
            opción= input("¿Qué desea actualizar? (nombre/precio/cantidad): ").lower()
            mostrarInventario()
            if opción == "nombre":
                id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))
                if 1 <= id_actualizar <= len(Inventario):
                    nuevo_nombre = input("Ingrese el nuevo nombre del producto: ").lower()
                    Inventario[id_actualizar - 1]['nombre'] = nuevo_nombre
                    print("Nombre actualizado correctamente.")
                else:
                    print("ID de producto no válido.")
            elif opción == "precio":
                id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))
                if 1 <= id_actualizar <= len(Inventario):
                    nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                    Inventario[id_actualizar - 1]['precio'] = nuevo_precio
                    print("Precio actualizado correctamente.")
                else:
                    print("ID de producto no válido.")
            elif opción == "cantidad":
                id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))
                if 1 <= id_actualizar <= len(Inventario):
                    nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                    Inventario[id_actualizar - 1]['cantidad'] = nueva_cantidad
                    print("Cantidad actualizada correctamente.")
                else:
                    print("ID de producto no válido.")
    except ValueError:
        print("Entrada inválida. Por favor ingrese un valor válido.")  

def eliminar():
    try: 
        if not Inventario:
            print(" # * # * El inventario esta vacio * # * #")
        else:
            mostrarInventario()

            eliminar_id = int(input("Ingrese el ID del producto a eliminar: "))
            if 1 <= eliminar_id <= len(Inventario):
                Inventario.pop(eliminar_id - 1)  #resta 1 para ajustar al indice de la lista
                print("Producto eliminado correctamente.")
    except ValueError:
        print("ID invalido. Por favor ingrese un numero valido.")

def calcularEstadistica():
    try:
        if not Inventario:
            print(" # * # * El inventario esta vacio * # * #")
        else:
            total_productos = len(Inventario)
            valor_total_inventario = 0
            for producto in Inventario:
                valor_total_inventario += (producto['precio'] * producto['cantidad'])

            producto_mas_caro =max(Inventario,key = lambda x:x['precio'])
            
            producto_mas_barato = min(Inventario, key=lambda x: x['precio'])    
            
            print(f"Total de productos en el inventario: {total_productos}")
            print(f"Valor total del inventario: {valor_total_inventario:.2f}")
            print(f"Producto más caro: {producto_mas_caro['nombre']} | Precio: {producto_mas_caro['precio']:.2f}")
            print(f"Producto más barato: {producto_mas_barato['nombre']} | Precio: {producto_mas_barato['precio']:.2f}")
            

     
    except ValueError:
        print("Error al calcular estadísticas. Por favor, verifique los datos del inventario.")



def guardarCsv():

    import csv # permite trabajar con los archivos csv
    import os # permite trabajar con rutas y archivos del sistema operativo

    if not Inventario: # valido si el inventario esta vacio
        print(" # * # * El inventario esta vacio * # * #")
        return 
    
    carpeta = "csv" # nombre de la carpeta donde se guardara el archivo
    ruta_carpeta = os.path.join(os.getcwd(), carpeta)# obtiene la ruta completa de la carpeta
    ruta_archivo= os.path.join(carpeta,"inventario.csv")# une la ruta de la carpeta con el nombre del archivo


    if not  os.path.exists(ruta_carpeta):# verifica si la carpeta no existe
        os.mkdir(ruta_carpeta)# crea la carpeta
    
    if os.path.exists(ruta_archivo):# verifica si el archivo ya existe
        print("El archivo inventario.csv ya existe y será sobrescrito.")
        modo = "a"
    else:
        modo = "w"

    
    with open(ruta_archivo, mode=modo, newline='') as archivo_csv:# abre el archivo en modo escritura
            campos = ['nombre', 'precio', 'cantidad']# nombres de las columnas del archivo csv
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos)# crea un objeto escritor de diccionarios
            if modo == "w":
                escritor.writeheader()# escribe los nombres de las columnas en el archivo

            for producto in Inventario:
                if (not producto['nombre'] or producto['nombre'] is None or
                    producto['precio'] is None or
                    producto['cantidad'] is None):
                    raise ValueError("Los campos del producto no pueden estar vacíos o ser None.")
                escritor.writerow(producto)
            
    print("Inventario guardado en inventario.csv correctamente.")
        


def cargarcsv():
    import csv
    import os

    #carpeta = input("como se llama ela carpeta donde esta el archivo: ")
    carpeta = os.path.join(os.getcwd(), "csv")# obtiene la ruta completa de la carpeta
    nombre = input("como se llama el archivo (con la extención .csv): ")# nombre del archivo
    ruta = os.path.join(carpeta, nombre)# une la ruta de la carpeta con el nombre del archivo


    try:
        with open(ruta, mode='r') as archivo_csv:# abre el archivo en modo lectura
            lector = csv.DictReader(archivo_csv)# crea un objeto lector de diccionarios
            #Inventario.clear()  # Limpiar el inventario actual antes de cargar nuevos datos
            for fila in lector:# recorre cada fila en el archivo
                producto = {# crea un diccionario con los datos de la fila
                    'nombre': fila['nombre'],
                    'precio': float(fila['precio']),
                    'cantidad': int(fila['cantidad'])
                }
                Inventario.append(producto)# agrega el producto al inventario
        print("Inventario cargado desde inventario.csv correctamente.")
    except FileNotFoundError:# si el archivo no existe
        print("El archivo inventario.csv no existe.")

