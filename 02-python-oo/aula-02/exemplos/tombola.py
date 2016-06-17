"""
Tômbola - sortear elementos de uma sequência de forma aleatória sem
repetição.

 Interface:
    - Carregar itens
    - Misturar itens
    - Sortear um item
    - Indicar se há mais itens

>>> t = Tombola()
>>> t.carrega_itens([1, 2, 3, 4, 5])
>>> t.itens
[1, 2, 3, 4, 5]
>>> t.mistura_itens()
>>> t.itens != [1, 2, 3, 4, 5]
True
>>> t.sorteia_item() in [1, 2, 3, 4, 5]
True
>>> len(t.itens)
4
>>> len(t.itens) != 0
True
>>> t.vazia()
False
>>> t.sorteia_item() in [1, 2, 3, 4, 5]
True
>>> t.sorteia_item() in [1, 2, 3, 4, 5]
True
>>> t.sorteia_item() in [1, 2, 3, 4, 5]
True
>>> t.sorteia_item() in [1, 2, 3, 4, 5]
True
>>> t.vazia()
True
"""
import random


class Tombola:
    def carrega_itens(self, itens):
        self.itens = itens

    def mistura_itens(self):
        random.shuffle(self.itens)

    def sorteia_item(self):
        return self.itens.pop()

    def vazia(self):
        return len(self.itens) == 0
