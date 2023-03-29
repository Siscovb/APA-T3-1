"""
    Tercera tarea de APA - manejo de vectores
    Nombre y apellidos: Oriol Garcia Moreiras
   
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
        Constructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
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

# MÉTODOS NUEVOS:
# Argumentos utilizados
# self --> Es el propio vector (él mismo).
# other --> Es otro vector realizando la propia operación.

    def __mul__(self, other):
        """
        Funcion para multiplicar un vector con otro vector o vector por escalar
        """
        if isinstance(other,(int,float,complex)):
            return Vector([valor * other for valor in self])
        else:
            return Vector([valor * other for valor, other in zip(self, other)])
    
    __rmul__ = __mul__
 
    def __matmul__(self,other):
        """
        Función para calcular el producto escalar de dos vectores
        """
        v = Vector([valor * other for valor, other in zip(self, other)])
        escalar = 0
        for i in range(len(v)):
            escalar += v[i]
        return escalar 

    __rmatmul__ = __matmul__ 

    def __floordiv__(self, other):
        """
        Función para calcular la componente tangencial de dos vector
        """
        return ((self @ other ) / (other @ other)) * other 
    
    def __rfloordiv__(self, other):
        """
        Función para calcular la componente tangencial de dos vector
        """
        return ((other @ self ) / (self @ self)) * self
    
    def __mod__(self, other):
        """
        Función para calcular la componente normal de dos vector
        """
        return self - (self // other)

    def __rmod__(self, other):
        """
        Función para calcular la componente normal de dos vectores
        """
        return other - (other // self)
        
import doctest
doctest.testmod()
