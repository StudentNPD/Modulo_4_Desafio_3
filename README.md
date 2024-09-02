# Modulo_4_Desafio_3

Este proyecto consiste en el desarrollo de un backend para una aplicación de compra y reparto de productos, utilizando Python y el paradigma de programación orientada a objetos. Como primer prototipo, se ha implementado una aplicación de consola donde los valores se ingresan mediante `input`.

## Descripción del Proyecto

El objetivo de este proyecto es diseñar e implementar la arquitectura de clases para la entidad principal "Tienda". Actualmente, se han implementado tres tipos de tiendas: **Restaurante**, **Supermercado**, y **Farmacia**. Cada tienda posee un nombre, un listado de productos, y un costo de delivery, y ofrece funcionalidades para ingresar productos, listar productos existentes, y realizar ventas.

### Características de las Tiendas

- **Restaurante**: Permite ingresar productos, listarlos, y realizar ventas sin restricciones de stock.
- **Supermercado**: Maneja productos con restricciones de stock y avisa cuando el stock es bajo.
- **Farmacia**: Maneja productos con restricciones de stock, permite venta de hasta 3 unidades por producto, y ofrece envío gratis para productos con un precio mayor a 15,000.

## Estructura del Proyecto

### Archivos Principales

1. **`programa.py`**:
   - Contiene el flujo principal del programa, manejando la creación de tiendas y la interacción del usuario con las opciones de listar productos, ingresar productos, y realizar ventas.

2. **`producto.py`**:
   - Define la clase `Producto` y contiene métodos para gestionar los atributos de un producto, como nombre, precio, y stock.
   - Métodos principales:
     - `get_nombre()`: Retorna el nombre del producto.
     - `get_precio()`: Retorna el precio del producto.
     - `get_stock()`: Retorna el stock disponible del producto.
     - `set_stock(valor)`: Modifica el stock del producto.
     - `validar_nombre(valor)`, `validar_precio(valor)`, `validar_stock(valor)`: Validan los valores ingresados para nombre, precio y stock respectivamente.

3. **`tienda.py`**:
   - Define la clase abstracta `Tienda` y las clases concretas `Restaurante`, `Supermercado`, y `Farmacia`.
   - Métodos principales en `Tienda`:
     - `ingresar_producto()`: Método abstracto para ingresar productos a la tienda.
     - `listar_productos()`: Método abstracto para listar productos disponibles.
     - `realizar_venta()`: Método abstracto para realizar una venta.
   - Las subclases implementan los métodos para su tipo específico de tienda, gestionando las particularidades de los productos y las ventas.

### Variables Principales

- **`nombre`** (str): Nombre de la tienda.
- **`costo_delivery`** (float): Costo de servicio de entrega.
- **`_lista_productos`** (list): Lista de productos disponibles en la tienda.
- **`Producto`** (class): Clase que define los productos, con atributos `nombre`, `precio`, y `stock`.

## Prerequisitos

- **Sistema Operativo**: Windows 10/11, Linux, macOS
- **Python**: Versión 3.12

## Ejecución

Para ejecutar el programa, sigue las instrucciones según tu sistema operativo:

### Windows

```bash
python programa.py
```
------------------------------------------
## Colaboradores
- [Francisco Colomer](https://github.com/Cy5k0) 
- [Francisco Monroy](https://github.com/fmonroy75)
- [Natalia Peña](https://github.com/StudentNPD)
