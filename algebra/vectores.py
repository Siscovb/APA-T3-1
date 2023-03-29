"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: RAfael A. Echevarria Silva

    >>> Vector([1, 2, 3]) * 2
    Vector([2, 4, 6])

    >>> 2 * Vector([1, 2, 3])
    Vector([2, 4, 6])

    >>> Vector([1, 2, 3]) * Vector([4, 5, 6])
    Vector([4, 10, 18])

    >>> Vector([1, 2, 3]) @ Vector([4, 5, 6])
    32

    >>> Vector([2, 1, 2]) // Vector([0.5, 1, 0.5])
    Vector([1.0, 2.0, 1.0])

    >>> Vector([2, 1, 2]) % Vector([0.5, 1, 0.5])
    Vector([1.0, -1.0, 1.0])

"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other
    
    #PRÁCTICA 03 

    def __mul__(self, other):
        """
        Multiplicación de los elementos de dos vectores (Hadamard) o de un vector por un escalar
        """
        if isinstance(other, Vector):
            return Vector([a * b for a, b in zip(self, other)])
        elif isinstance(other, (int, float, complex)):
            return Vector([other * x for x in self])

    __rmul__ = __mul__

    def __matmul__(self, other):
        """
        Método para implementar el producto escalar de dos vectores.
        """
        return sum([a * b for a, b in zip(self, other)])
        
    __rmatmul__ = __matmul__
    
    def __floordiv__(self, other):
        """
        Método para que devuelva la componente tangencial.
        """     
        return Vector([(sum(a * b for a, b in zip(self, other)) // (sum(a ** 2 for a in other) ** 0.5)) * b for b in other])

    __rfloordiv__ = __floordiv__

    def __mod__(self, other):
        """
        Método para que devuelva la componente normal o perpendicular.
        """
        return self - self // other
    
    __rmod__ = __mod__

import doctest

doctest.testmod()