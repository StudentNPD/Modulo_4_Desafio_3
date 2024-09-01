def get_nombre(self):
    """Obtiene el nombre del producto.

    Returns:
        str: El nombre del producto.
    """
    return self.nombre  # __nombre. No está definido así en el constructor, por eso no lo pilla


def get_precio(self):
    """Obtiene el precio del producto.

    Returns:
        int: El precio del producto.
    """
    return self.precio  # __precio. No está definido así en el constructor, por eso no lo pilla


def get_stock(self):
    """Obtiene la cantidad de stock disponible del producto.

    Returns:
        int: La cantidad de stock disponible.
    """
    return self.stock  # __stock. No está definido así en el constructor, por eso no lo pilla


def set_stock(self, valor):
    """Establece la cantidad de stock disponible del producto.

    Valida que el stock sea un número entero positivo.

    Args:
        valor (int): La cantidad de stock a establecer.

    Raises:
        ValueError: Si `valor` no es un entero positivo.
    """
    self.validar_stock(valor)
    self.__stock = valor


def validar_nombre(self, valor):
    """Valida que el nombre sea una cadena de caracteres.

    Args:
        valor (str): El nombre a validar.

    Raises:
        ValueError: Si `valor` no es una cadena de caracteres.
    """
    if not isinstance(valor, str):
        raise ValueError("El nombre debe ser una cadena de caracteres")


def validar_precio(self, valor):
    """Valida que el precio sea un entero positivo.

    Args:
        valor (int): El precio a validar.

    Raises:
        ValueError: Si `valor` no es un entero positivo.
    """
    if not isinstance(valor, int) or valor < 0:
        raise ValueError("El precio debe ser un entero positivo")


def validar_stock(self, valor):
    """Valida que el stock sea un entero positivo.

    Args:
        valor (int): La cantidad de stock a validar.

    Raises:
        ValueError: Si `valor` no es un entero positivo.
    """
    if not isinstance(valor, int) or valor < 0:
        raise ValueError("El stock debe ser un entero positivo")



