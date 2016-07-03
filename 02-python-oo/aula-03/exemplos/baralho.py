from collections import namedtuple
from collections.abc import MutableSequence


Carta = namedtuple('Carta', ['valor', 'naipe'])


class Baralho:
    valores = [str(n) for n in range(2, 11)] + list('AJQK')
    naipes = 'copas ouros paus espadas'.split()

    def __init__(self):
        self.cartas = [Carta(v, n) for v in self.valores for n in self.naipes]

    def __len__(self):
        return len(self.cartas)

    def __getitem__(self, pos):
        return self.cartas[pos]

    def __setitem__(self, pos, carta):
        self.cartas[pos] = carta
