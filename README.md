# Modulo_4_Desafio_3

Te encuentras participando de un proyecto de emprendimiento que consiste en una
aplicación móvil de compra y reparto de productos. El equipo ha decidido hacer el backend
de la aplicación utilizando Python y el paradigma orientado a objetos. Para el primer prototipo
de entrega, se solicita realizar una aplicación de consola en Python, donde los ingresos de
valores se hagan mediante input.
El equipo te ha solicitado diseñar e implementar la arquitectura de clases que involucra a la
entidad principal “Tienda”. Estas son las consideraciones que se deben tener en cuenta
respecto de las tiendas:
● Existen por el momento 3 tipos de tienda (en el futuro podría haber más), los cuales
son: “Restaurante”, “Supermercado” y “Farmacia”.
● Todas las tiendas deben poder ingresar un producto, listar los productos existentes, y
realizar ventas.
● Cada tienda creada, independiente de su tipo, posee un nombre, un listado de
productos y un costo de delivery. Al momento de crear una nueva tienda, se debe
solicitar el nombre y el costo de delivery (todas las tiendas se crean inicialmente sin
productos). En una tienda ya existente, no se puede modificar el nombre ni el costo de
delivery, pero sí se puede modificar los productos (mediante el ingreso de un producto,
o mediante la realización de ventas).
● Los productos tienen un nombre, un precio y un stock. Los 3 valores se deben solicitar
al momento de crear un producto nuevo, pero si no se indica stock, se asume que es
1. No se puede modificar el nombre ni el precio de un producto, solo su stock. Si se
intenta modificar el stock por un valor menor a 0, se debe asignar 0 en su lugar. De
cada producto se puede obtener su nombre, su precio o su stock.

------------------------------------------

## Prerequisitos

- Sistema Operativos: Windows 10, 11, Linux, iOS
- Python 3.12

## Ejecución

***Windows***

`python programa.py`

***Linux & iOS***

`python3 programa.py`

------------------------------------------
## Colaboradores
- [Francisco Colomer](https://github.com/Cy5k0) 
- [Francisco Monroy](https://github.com/fmonroy75)
- [Natalia Peña](https://github.com/StudentNPD)
