"""
Implementa um vetor bidimensional (versão 2 - mais completa)
"""
from numbers import Real
import math


class Vetor:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self): return 'Vetor({!r}, {!r})'.format(self.x, self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __eq__(self, outro):
        if isinstance(outro, Vetor):
            return self.x == outro.x and self.y == outro.y
        else:
            return NotImplemented

    def __iter__(self):
        return iter((self.x, self.y))

    def __neg__(self):
        return self * -1

    def __pos__(self):
        return self

    def __sub__(self, outro):
        return Vetor(self.x - outro.x, self.y - outro.y)

    def __mul__(self, escalar):
        if isinstance(escalar, Real):
            return Vetor(self.x * escalar, self.y * escalar)
        else:
            return NotImplemented

    def __rmul__(self, outro):
        return self * outro
