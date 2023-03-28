"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Milene Granda
"""
# no hay comprehensions!! acuerdate

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
        Multiplicación Hadamard o multiplicación de vector por escalar
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 * 2
        Vector([2, 4, 6])
        >>> v1 * v2
        Vector([4, 10, 18])
        """
        if isinstance(other, (int, float, complex)): # Para añadir método a '*'
            return Vector(uno * other for uno in self)
        else:
            return Vector(uno * otro for uno, otro in zip(self, other))
    
    def __rmul__(self, other):
        """
        Método reflejado de la multiplicación Hadamard o multiplicación de vector por escalar
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> 2 * v1
        Vector([2, 4, 6])
        >>> v2 * v1
        Vector([4, 10, 18])
        """
        return self.__mul__(other)    
   
    def __matmul__(self, other):
        """
        Producto escalar de dos vectores
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 @ v2
        32
        """
        if isinstance(other, Vector) and len(self): # Para añadir método a '@'
            result = sum(x * y for x, y in zip(self, other))
            return result
        else:
            return None
        
    __rmatmul__=__matmul__ #Método reflejado para el producto escalar
   
    def __floordiv__(self, other):
        """
       Obtención de componente tangencial
        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 // v2
        Vector([1.0, 2.0, 1.0])
        """
        if isinstance(other, Vector) : # Para añadir método a '//'
            return Vector([(sum(x * y for x, y in zip(self,other) )// (sum(x ** 2 for x in other) **0.5)) * y for  y in  other])
        else:
            return None
    
    def __rfloordiv__(self, other):
        """
       Método reflejado de obtención de componente tangencial
        """
        if isinstance(other, Vector) : # Para añadir método a '//'
            return Vector([(other * y // (sum(x ** 2 for x in self) **0.5)) * y for  y in  self])
        else:
            return None
    
    def __mod__(self, other):
        """
       Obtención de componente normal
        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 % v2
        Vector([1.0, -1.0, 1.0])
        """
        return self-self // other
    
    def __rmod__(self, other):
        """
       Método reflehado de obtención de componente normal
        """
        return other.mod(self)
    



# Para realizar los tests unitarios:
import doctest
doctest.testmod()