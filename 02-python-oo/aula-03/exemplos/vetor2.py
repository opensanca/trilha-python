"""
Implementa um vetor bidimensional (versão 2 - mais completa)
"""
from numbers import Real
import math


class Vetor:
    """
    Vetor bidimensional que implementa soma, subtração, multiplicação por escalar etc.

    >>> v1 = Vetor(3, -2)
    >>> v1
    Vetor(3, -2)
    >>> v2 = Vetor(1, 1)
    >>> v2
    Vetor(1, 1)
    >>> v1 + v2
    Vetor(4, 1)
    >>> v1 - v2
    Vetor(2, -3)
    >>> v1 * 3
    Vetor(9, -6)
    >>> 5 * v2
    Vetor(5, 5)
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self): return 'Vetor({!r}, {!r})'.format(self.x, self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __add__(self, outro):
        if isinstance(outro, Vetor):
            return Vetor(self.x + outro.x, self.y + outro.y)
        else:
            return NotImplemented

    def __bool__(self):
        return bool(self.x or self.y)

    def __eq__(self, outro):
        if isinstance(outro, Vetor):
            return self.x == outro.x and self.y == outro.y
        else:
            return NotImplemented

    def __iter__(self):
        yield self.x
        yield self.y

    def __matmul__(self, outro):
        return self.x * outro.x + self.y * outro.y

    def __mul__(self, escalar):
        if isinstance(escalar, Real):
            return Vetor(self.x * escalar, self.y * escalar)
        else:
            return NotImplemented

    def __rmul__(self, outro):
        return self * outro

    def __neg__(self):
        return self * -1

    def __pos__(self):
        return self

    def __sub__(self, outro):
        return Vetor(self.x - outro.x, self.y - outro.y)


class VetorMutavel(Vetor):
    """
    Versão mutável do Vetor bidimensional.  Não tem muita utilidade no mundo real, serve
    mais para demonstrar como funciona `__iadd__` e `__imul__`
    """

    def __repr__(self):
        return 'VetorMutavel({!r}, {!r})'.format(self.x, self.y)

    def __iadd__(self, outro):
        if isinstance(outro, Vetor):
            self.x += outro.x
            self.y += outro.y
            return self
        return NotImplemented

    def __imul__(self, outro):
        if isinstance(outro, Real):
            self.x *= outro
            self.y *= outro
            return self
        return NotImplemented
