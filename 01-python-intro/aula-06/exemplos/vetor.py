""" Este módulo oferece um vetor espacial e operações de vetor

Fornece uma classe `Vetor` que armazena as posições x e y em uma `namedtuple`
e funções de soma (soma_vetor) e subtração (subtrai_vetor)

>>> v1 = Vetor(1, 1)
>>> v1
Vetor(x=1, y=1)
>>> v2 = Vetor(2, 3)
>>> Vetor(x=2, y=3) Vetor(x=2, y=3)
>>> soma_vetor(v1, v2)
Vetor(x=3, y=4)
>>> subtrai_vetor(v1, v2)
Vetor(x=-1, y=-2)
>>> subtrai_vetor(v2, v1)
Vetor(x=1, y=2)
"""


from collections import namedtuple

Vetor = namedtuple('Vetor', ['x', 'y'])


def soma_vetor(v1, v2):
    """
    Retorna a soma dos vetores v1 e v2 (v1 + v2)

    >>> soma_vetor(Vetor(1, 1), Vetor(1, 2))
    Vetor(x=2, y=3)
    """
    return Vetor(v1.x + v2.x, v1.y + v2.y)


def subtrai_vetor(v1, v2):
    """
    Retorna a subtração dos vetores v1 e v2 (v1 - v2)

    >>> subtrai_vetor(Vetor(3, 2), Vetor(1, 2))
    Vetor(x=2, y=0)
    """
    return Vetor(v1.x - v2.x, v1.y - v2.y)
