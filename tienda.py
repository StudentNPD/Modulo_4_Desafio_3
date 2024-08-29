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
    
