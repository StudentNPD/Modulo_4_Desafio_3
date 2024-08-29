#from producto import Producto
#from tienda import Tienda

#INSTANCIAR LA CLASE TIENDA
#mi_tienda = Tienda(tipo,nombre,precio)

while True:
    print("Menu: \n1)Listar Productos\n2)Ingresar Producto\n3)Realizar Venta\n4)Salir\n")
    opcion = int(input("Ingrese Opcion\n"))
    if opcion == 1:
        print("Listando Productos\n")
    elif opcion == 2:
        print("Ingresar Producto\n")
    elif opcion == 3:
        print("Realizar venta\n")
    elif opcion == 4:
        print("Gracias por ingresar a la tienda!\n")
        break
    else:
        print("Ingrese una opcón válida\n")

    #producto_nuevo = input("Ingrese un producto").title()
    
    
    
