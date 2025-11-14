
biblioteca = [
    {
        "nombre" : "harry potter",
        "categoria" : "fantasia",
        "disponible" : "si"
    },
    {
        "nombre" : "el señor de los anillos",
        "categoria" : "fantasia",
        "disponible" : "no"
    },
]

#biblioteca = []

def guardar(nombreLibro,nombreCategoria,disponibilidad):

    guardar = {
                "nombre" : nombreLibro,
                "categoria" : nombreCategoria,
                "disponible" : disponibilidad
                
    }  
    biblioteca.append(guardar)
    print("✅ Libro agregado correctamente.\n")


def agregarLibros():
  
        while True:
                nombreLibro = input("Ingrese el libro: ").lower()
                if nombreLibro:
                    break
                print("guardado")
                    
        while True:
            nombreCategoria = input("Ingrese la categoria: ").lower()
            if nombreCategoria:
                print("guardadooo")
                break
            else:
                print("libro esta vacio")
                    
        while True:
            disponibilidad = input("Ingrese la disponibilidad: ").lower()
            if disponibilidad == "si":
                print("Se puede prestar")
                break
            else:
                print("libro ya prestado")
                break
      
        guardar(nombreLibro,nombreCategoria, disponibilidad)
        
       

 

    
def estado(libro):
    
    if libro["disponible"] == "si":
         libro["estado"] = "Libre"
    else:
        libro["estado"] = "Prestado"

    return libro["estado"]

def verLibros():
    
    if not biblioteca:
        print("  lista de libros vacia  ")
    else:
        
        for i,libro in enumerate(biblioteca, start=1):
            print(f"{i} | Nombre del libro = {libro['nombre']} | Genero = {libro['categoria']} | disponibilidad = {libro['disponible']} | estado_actual = {estado(libro)}")
            








            
while True:
    try:
        print("****************************************")
        selector = int(input(f"\n  1. Agregar Libro\n  2.Mostrar Libros\n  3.Salir\n  --->"))
        print("****************************************")
    except ValueError():
        print("solo se permite numeros ")
        continue    

    if selector == 1:
        agregarLibros()
    elif selector == 2:
        verLibros()
    elif selector == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Ingresar solo datos del 1 al 4")
        # except ValueError:
        #     print("ISolo SE PERMITEN NUMEROS")
