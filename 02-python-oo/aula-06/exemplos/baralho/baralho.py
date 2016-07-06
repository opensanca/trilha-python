from collections import namedtuple


Carta = namedtuple('Carta', ['valor', 'naipe'])


class Baralho:
    """
    Defiine um baralho que possui todas as cartas de A até K dos naipes uibsp

    >>> baralho = Baralho()
    >>> baralho[0]
    Carta(valor='2', naipe='copas')
    >>> baralho[:2]
    [Carta(valor='2', naipe='copas'), Carta(valor='2', naipe='ouros')]
    >>> baralho[-2:]
    [Carta(valor='K', naipe='paus'), Carta(valor='K', naipe='espadas')]
    """
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
