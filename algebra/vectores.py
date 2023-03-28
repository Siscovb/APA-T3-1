"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Kirian Rodriguez Alonso
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

    
    def __mul__(self, other):
        """
        Multiplica vector con vector o numero
        """

        if isinstance(other,(int, float, complex)):
            return Vector([valor * other for valor in self])
        else:
            return Vector([valor * otro for valor, otro in zip(self, other)])
    
    __rmul__ = __mul__


    def __matmul__(self, other):
        """
        Calculo producto escalar de 2 vectores
        """
        prod_escalar= Vector([valor * otro for valor, otro in zip(self, other)])
        return prod_escalar

    __rmatmul__ = __matmul__


    def __floordiv__(self, other):
        """
        Calcula componente tangencial
        """
        return ((self @ other) / (other @ other)) * other
    
    __rfloordiv__ = __floordiv__


    def __mod__(self, other):
        """
        Calcula componente normal
        """
        return self - (self // other)
    
    __rmod__ = __mod__

    import doctest
    doctest.testmod()
