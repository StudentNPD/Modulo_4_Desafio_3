from tienda import Tienda, Farmacia, Restaurante #,Supermercado

tipo_tienda = int(input("Ingrese el tipo de tienda: \n1)Supermercado\n2)Farmacia\n3)Restaurante\n"))
nombre_tienda = input("Ingrese el nombre de la tienda:\n")
delivery = input("Ingrese costo de delivery:\n")

mi_tienda = Tienda

if tipo_tienda == 1:
    print("Supermercado")
    mi_tienda = Supermercado(nombre_tienda,delivery)
elif tipo_tienda == 2:
    mi_tienda = Farmacia(nombre_tienda,delivery)
elif tipo_tienda == 3:
    mi_tienda = Restaurante(nombre_tienda,delivery)
else: 
    print("Por favor ingrese la opción: 1,2 o 3")

while True:
    print("Menu: \n1)Listar Productos\n2)Ingresar Producto\n3)Realizar Venta\n4)Salir\n")
    opcion = int(input("Ingrese Opcion\n"))
    if opcion == 1:
        print(mi_tienda.listar_productos())
    elif opcion == 2:
        mi_tienda.ingresar_producto()
    elif opcion == 3:
        mi_tienda.realizar_venta()
    elif opcion == 4:
        print("Gracias por ingresar a la tienda!\n")
        break
    else:
        print("Ingrese una opcón válida\n")
