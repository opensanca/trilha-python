"""
Implementa um vetor bidimensional (versão 1 - mais simples)
"""
from numbers import Real
import math


class Vetor:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vetor({!r}, {!r})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

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

    def __sub__(self, outro):
        return Vetor(self.x - outro.x, self.y - outro.y)

    def __mul__(self, scalar):
        if isinstance(scalar, Real):
            return Vetor(self.x * scalar, self.y * scalar)
        else:
            return NotImplemented
