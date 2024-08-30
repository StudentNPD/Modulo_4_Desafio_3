# from producto import Producto
from tienda import Restaurante  # ,supermercado,farmacia

# INSTANCIAR LA CLASE TIENDA
# mi_tienda = Tienda(tipo,nombre,precio)

# while True:
#     print("Menu: \n1)Listar Productos\n2)Ingresar Producto\n3)Realizar Venta\n4)Salir\n")
#     opcion = int(input("Ingrese Opcion\n"))
#     if opcion == 1:
#         print("Listando Productos\n")
#     elif opcion == 2:
#         print("Ingresar Producto\n")
#     elif opcion == 3:
#         print("Realizar venta\n")
#     elif opcion == 4:
#         print("Gracias por ingresar a la tienda!\n")
#         break
#     else:
#         print("Ingrese una opcón válida\n")

# producto_nuevo = input("Ingrese un producto").title()


# Menu
def menu_principal(tienda):
    while True:
        print("\n1. Listar productos")
        print("2. Realizar venta")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print(tienda.listar_productos())
        elif opcion == "2":
            nombre_producto = input("Ingresa nombre del producto: ")
            cantidad = int(input("Ingresa cantidad: "))
            print(tienda.realizar_venta(nombre_producto, cantidad))
        elif opcion == "3":
            print("Se cierra la aplicacioon.")
            break
        else:
            print("Opción no válida.")


# Crear tienda
def crear_tienda():
    tipo = input(
        "Ingrese el tipo de tienda (Restaurante/Supermercado/Farmacia): "
    ).lower()
    nombre = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))

    # validacion de tipo
    if tipo == "restaurante":
        return Restaurante(nombre, costo_delivery)
    elif tipo == "supermercado":
        return Supermercado(nombre, costo_delivery)  # clase por crear en tienda
    elif tipo == "farmacia":
        return Farmacia(nombre, costo_delivery)  # clase por crear en tienda
    else:
        print("Tipo de tienda no válido")
        return None
