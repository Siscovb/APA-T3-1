"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Clara Barba Armengol
"""
import math 
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
    Retorna la multiplicació de un vector por un vector (element per element)
    >>> v1 = Vector([1, 2, 3]) 
    >>> v2 = Vector([4, 5, 6])
    >>> v3 = v1 * v2
    >>> print(v3.vector)
    [4, 10, 18]
            """
        if isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Els vectors han de tenir la mateixa longitut")
            return Vector([self.vector[i] * other.vector[i] for i in range(len(self.vector))])
        elif isinstance(other, (int, float)):
            return Vector([other * value for value in self.values])
        else:
            raise TypeError("No és possible multiplicar el vector per aquest objecte (ha de ser vector * vector)")
    
    def __rmul__(self, other):
        """
        Devuelve
    >>> v1 = Vector([1, 2, 3]) 
    >>> v3 = 2 * v1
    >>> print(v3.vector)
    [2, 4, 6]
        """
        if isinstance(other, (int, float)):
            return Vector([other * value for value in self.vector])
        else:
            raise TypeError("No és possible multiplicar el vector per aquest objecte (ha de ser vector * escalar)")
        
    
    def __matmul__(self, other):
        """
        Devuelve
    >>> v1 = Vector([1, 2, 3]) 
    >>> v2 = Vector([4, 5, 6])
    >>> v3 = v1 @ v2 
    >>> print(v3)
    32
        """
        if isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Els vectors han de tenir la mateixa longitut")
            return sum([self.vector[i] * other.vector[i] for i in range(len(self.vector))])
        else:
            raise TypeError("No és possible multiplicar el vector per aquest objecte")
    
    def __rmatmul__(self, other):
        """
        Devuelve
    >>> v1 = Vector([1, 2, 3]) 
    >>> v2 = Vector([4, 5, 6])
    >>> v3 = v1 @ v2
    >>> print(v3)
    32
        """
        if isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Els vectors han de tenir la mateixa longitut")
            return sum([other.vector[i] * self.vector[i] for i in range(len(self.vector))])
        else:
            raise TypeError("No és possible multiplicar el vector per aquest objecte")

    def __floordiv__(self, other):
        """
        Devuelve
    >>> v1 = Vector([2, 1, 2]) 
    >>> v2 = Vector([0.5, 1, 0.5])
    >>> v3 = v2 // v1
    >>> print(v3)
    [1.0, 2.0, 1.0]
        """
        if isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Els vectors han de tenir la mateixa longitut")
            
            # Calculem direcció tangencial
            producte_escalar = self @ other
            modul = math.sqrt(sum([value ** 2 for value in self.vector]))
            e_tangencial = Vector([self.vector[i] / modul for i in range(len(self.vector))])
            
            # Calculem component tangencial del vector
            component_tangencial = (other @ e_tangencial) * e_tangencial
            return component_tangencial
        else:
            raise TypeError("No és possible multiplicar el vector per aquest objecte")  
        
    def __rfloordiv__(self, other):
        """
        Devuelve
    >>> v1 = Vector([2, 1, 2]) 
    >>> v2 = Vector([0.5, 1, 0.5])
    >>> v3 = v2 // v1
    >>> print(v3)
    [1.0, 2.0, 1.0]
        """
        if isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Els vectors han de tenir la mateixa longitut")
            
            # Calculem direcció tangencial
            producte_escalar = self @ other
            modul = math.sqrt(sum([value ** 2 for value in other.vector]))
            e_tangencial = Vector([other.vector[i] / modul for i in range(len(other.vector))])
            
            # Calculem component tangencial del vector
            component_tangencial = (self @ e_tangencial) * e_tangencial
            return component_tangencial
        else:
            raise TypeError("No és possible multiplicar el vector per aquest objecte")  

    def __mod__(self, other):
        """
        Devuelve
    >>> v1 = Vector([2, 1, 2]) 
    >>> v2 = Vector([0.5, 1, 0.5])
    >>> v3 = v1 % v2
    >>> print(v3)
    [1.0, -1.0, 1.0]
        """
        if isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Els vectors han de tenir la mateixa longitut")
            
            # Calculem direcció tangencial
            producte_escalar = self @ other
            modul = math.sqrt(sum([value ** 2 for value in other.vector]))
            e_tangencial = Vector([other.vector[i] / modul for i in range(len(other.vector))])
            
            # Calculem component tangencial i component normal del vector
            component_tangencial = self // other
            component_normal = self - component_tangencial
            
            return component_normal
        else:
            raise TypeError("No és possible calcular el mòdul del vector per aquest objecte")  
        
    def __rmod__(self, other):
        """
        Devuelve
    >>> v1 = Vector([2, 1, 2]) 
    >>> v2 = Vector([0.5, 1, 0.5])
    >>> v3 = v1 % v2
    >>> print(v3)
    [1.0, -1.0, 1.0]
        """
        if isinstance(self, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Els vectors han de tenir la mateixa longitut")
            
            # Calculem direcció tangencial
            producte_escalar = other @ self
            modul = math.sqrt(sum([value ** 2 for value in self.vector]))
            e_tangencial = Vector([self.vector[i] / modul for i in range(len(self.vector))])
            
            # Calculem component tangencial i component normal del vector
            component_tangencial = other // self
            component_normal = other - component_tangencial
            
            return component_normal
        else:
            raise TypeError("No és possible calcular el mòdul del vector per aquest objecte") 

import doctest
doctest.testmod()
    
    

