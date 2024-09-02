from producto import Producto  # agregado
from abc import ABC, abstractmethod

class Tienda(ABC):
    def __init__(self, nombre, costo_delivery):
        """
        Inicializa una instancia de la clase Tienda.

        Args:
            nombre (str): El nombre de la tienda.
            costo_delivery (float): El costo del servicio de entrega.
        """
        self._nombre = nombre
        self._costo_delivery = costo_delivery
        self._lista_productos = []

    @property
    def nombre(self):
        """
        Obtiene el nombre de la tienda.

        Returns:
            str: El nombre de la tienda.
        """
        return self._nombre

    @property
    def costo_delivery(self):
        """
        Obtiene el costo del servicio de entrega.

        Returns:
            float: El costo de delivery.
        """
        return self._costo_delivery

    @abstractmethod
    def ingresar_producto(self):
        """
        Método abstracto para ingresar un producto a la tienda.
        """
        pass

    @abstractmethod
    def listar_productos(self):
        """
        Método abstracto para listar los productos disponibles en la tienda.

        Returns:
            str: Una cadena con la lista de productos y sus detalles.
        """
        pass

    @abstractmethod
    def realizar_venta(self):
        """
        Método abstracto para realizar una venta de un producto.

        Returns:
            None
        """
        pass


class Restaurante(Tienda):
    def ingresar_producto(self):
        """
        Ingresa un nuevo producto al restaurante.
        
        Solicita al usuario el nombre y el precio del producto, y lo añade a la lista de productos si no existe ya.

        Returns:
            None
        """
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        producto = Producto(nombre, precio, 0)

        for prod in self._lista_productos:
            if prod == producto:
                print("El producto ya existe y no se modifica el stock.")
                return

        self._lista_productos.append(producto)
        print("Producto ingresado exitosamente.")

    def listar_productos(self):
        """
        Lista los productos disponibles en el restaurante.

        Returns:
            str: Una cadena que contiene la lista de productos con sus nombres y precios.
        """
        cadena = "" 
        for prod in self._lista_productos:
            cadena = cadena + "\n" + "Producto: " + prod.nombre + ", Precio: $" + str(prod.precio)
        return cadena
        
    def realizar_venta(self):
        """
        Realiza una venta de un producto del restaurante.

        Solicita al usuario el nombre del producto y la cantidad a vender, y realiza la venta si el producto existe.

        Returns:
            None
        """
        nombre = input("Ingrese el nombre del producto a vender: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))

        for prod in self._lista_productos:
            if prod.nombre == nombre:
                print("Venta realizada.")
                return
        print("Producto no encontrado.")


class Farmacia(Tienda):
    def ingresar_producto(self):
        """
        Ingresa un nuevo producto a la farmacia.
        
        Solicita al usuario el nombre, precio y stock del producto, y lo añade a la lista de productos si no existe ya.
        Si el producto existe, se actualiza su stock.

        Returns:
            None
        """
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        producto = Producto(nombre, precio, stock)

        for prod in self._lista_productos:
            if prod == producto:
                prod + stock
                print("Stock actualizado.")
                return

        self._lista_productos.append(producto)
        print("Producto ingresado exitosamente.")

    def listar_productos(self):
        """
        Lista los productos disponibles en la farmacia.

        Returns:
            str: Una cadena que contiene la lista de productos con sus nombres, precios y posibles beneficios de envío.
        """
        cadena = "" 
        for prod in self._lista_productos:
            cadena = cadena + "\n" + "Producto: " + prod.nombre + ", Precio: $" + str(prod.precio)
            if prod.precio > 15000:
                cadena = cadena + '(Envío gratis al solicitar este producto) '
        return cadena

    def realizar_venta(self):
        """
        Realiza una venta de un producto de la farmacia.

        Solicita al usuario el nombre del producto y la cantidad a vender. Si la cantidad solicitada es mayor a 3 o el stock es insuficiente, la venta no se realiza.

        Returns:
            None
        """
        nombre = input("Ingrese el nombre del producto a vender: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))

        if cantidad > 3:
            print("No se puede solicitar más de 3 unidades.")
            return

        for prod in self._lista_productos:
            if prod.get_nombre() == nombre:
                vendida = prod.get_stock() - cantidad
                if vendida > 0:
                    print(f"Venta realizada. Cantidad vendida: {vendida}")
                else:
                    print("Stock insuficiente.")
                return
        print("Producto no encontrado.")


class Supermercado(Tienda):
    def ingresar_producto(self):
        """
        Ingresa un nuevo producto al supermercado.
        
        Solicita al usuario el nombre, precio y stock del producto, y lo añade a la lista de productos si no existe ya.
        Si el producto existe, se actualiza su stock.

        Returns:
            None
        """
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        producto = Producto(nombre, precio, stock)

        for prod in self._lista_productos:
            if prod == producto:
                prod + stock
                print("Stock actualizado.")
                return

        self._lista_productos.append(producto)
        print("Producto ingresado exitosamente.")

    def listar_productos(self):
        """
        Lista los productos disponibles en el supermercado.

        Returns:
            str: Una cadena que contiene la lista de productos con sus nombres, precios, stock, y un aviso si el stock es bajo.
        """
        cadena = "" 
        for prod in self._lista_productos:
            cadena = cadena + "\n" + "Producto: " + prod.nombre + ", Precio: $" + str(prod.precio) + ", Stock: " + str(prod.stock)
            if prod.stock < 10:
                cadena = cadena + '(Pocos productos disponibles)'
        return cadena
        
    def realizar_venta(self):
        """
        Realiza una venta de un producto del supermercado.

        Solicita al usuario el nombre del producto y la cantidad a vender. Si el stock es insuficiente, la venta no se realiza.

        Returns:
            None
        """
        nombre = input("Ingrese el nombre del producto a vender: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))

        for prod in self._lista_productos:
            if prod.nombre == nombre:
                vendida = prod.stock - cantidad
                if vendida > 0:
                    print(f"Venta realizada. Cantidad vendida: {vendida}")
                else:
                    print("Stock insuficiente.")
                return
        print("Producto no encontrado.")

