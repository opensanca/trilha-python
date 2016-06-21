"""
Implementa uma tombola (gaiola de bingo)
"""
import random


class TombolaExpansivel:
    def __init__(self, itens=None):
        if not itens:
            itens = []
        self._itens = itens

    def __add__(self, other):
        if isinstance(other, TombolaExpansivel):
            return TombolaExpansivel(self.inspeciona() + other.inspeciona())
        else:
            return NotImplemented

    def __idadd__(self, outro):
        if isinstance(outro, TombolaExpansivel):
            outro_iteravel = outro.inspeciona()
        else:
            try:
                outro_iteravel = iter(outro)
            except TypeError:
                msg = "operando da direita no += deve ser {!r} ou um iterável"
                raise TypeError(msg.format(type(self).__name__))
        self.carrega(outro_iteravel)
        return self

    def __call__(self):
        return self.sorteia()

    def carrega(self, itens):
        self._itens = list(itens)

    def inspeciona(self):
        return tuple(self._itens)

    def mistura(self):
        random.shuffle(self._itens)

    def sorteia(self):
        return self._itens.pop()

    def vazia(self):
        return len(self._itens) == 0
