from servicios import *



while True:

    print("****************************************")
    selector = int(input(f"\n  1.Agregar producto\n  2.Mostrar inventario\n  3.buscar\n  4.actualizar\n  5.eliminar\n  6.Calcular estadísticas\n  7.Guardar Csv\n  8.Cargar Csv\n  9.Salir\n  --->"))
    print("****************************************")
    #try:
    if selector == 1:
        agregarProducto()
    elif selector == 2:
        mostrarInventario()
    elif selector== 3:
        buscar()
    elif selector == 4:
        actualizar()
    elif selector == 5:
        eliminar()
    elif selector == 6:
        calcularEstadistica()
    elif selector == 7:
        guardarCsv()
    elif selector == 8:
        cargarcsv()
    elif selector == 9:
        print("Saliendo ... ")
        break    
    else:
        print("Ingresar solo datos del 1 al 9")
    # except ValueError:
    #     print("ISolo SE PERMITEN NUMEROS")
