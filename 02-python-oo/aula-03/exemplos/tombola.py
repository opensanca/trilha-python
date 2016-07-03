"""
Implementa uma tombola (gaiola de bingo)
"""
import random


class Tombola:
    def __init__(self, itens=None):
        self._itens = []
        self.carrega(itens)

    def __call__(self):
        return self.sorteia()

    def carrega(self, itens):
        self._itens.extend(itens)

    def inspeciona(self):
        return tuple(self._itens)

    def mistura(self):
        random.shuffle(self._itens)

    def sorteia(self):
        return self._itens.pop()

    def vazia(self):
        return len(self._itens) == 0


class TombolaExpansivel(Tombola):
    def __add__(self, other):
        if isinstance(other, Tombola):
            return TombolaExpansivel(self.inspeciona() + other.inspeciona())
        else:
            return NotImplemented

    def __iadd__(self, outro):
        if isinstance(outro, Tombola):
            outro_iteravel = outro.inspeciona()
        else:
            try:
                outro_iteravel = iter(outro)
            except TypeError:
                msg = "operando da direita no += deve ser {!r} ou um iterável"
                raise TypeError(msg.format(type(self).__name__))
        self.carrega(outro_iteravel)
        return self
