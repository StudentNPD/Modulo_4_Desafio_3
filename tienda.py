import producto
from abc import ABC, abstractmethod

class Tienda(ABC):
    def __init__(self, nombre, costo_delivery):
        self._nombre = nombre
        self._costo_delivery = costo_delivery
        self._lista_productos = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def costo_delivery(self):
        return self._costo_delivery

    @abstractmethod
    def ingresar_producto(self):
        pass
    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self):
        pass
    
    
class Restaurante(Tienda):
    def ingresar_producto(self):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        producto = producto(nombre, precio, 0)

        for prod in self._lista_productos:
            if prod == producto:
                print("El producto ya existe y no se modifica el stock.")
                return

        self._lista_productos.append(producto)
        print("Producto ingresado exitosamente.")

    def listar_productos(self):
        cadena="" 
        for prod in self._lista_productos
            cadena=cadena + "\n" +"Producto: " + prod.nombre +", Precio: $" + prod.precio 
        return cadena
        
    def realizar_venta(self):
        nombre = input("Ingrese el nombre del producto a vender: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))

        for prod in self._lista_productos:
            if prod.nombre == nombre:
                print("Venta realizada.")
                return
        print("Producto no encontrado.")


