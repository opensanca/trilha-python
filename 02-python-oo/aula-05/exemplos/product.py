"""
Cria uma classe Product para representar um produto.
Encapsula o preço do produto definindo-o como property e cria setters e deleters.
"""


class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.__price = price
        self.description = description

    @property
    def price(self):
        return 'R${:.2f}'.format(self.__price)

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            new_price = 0
        self.__price = new_price

    @price.deleter
    def price(self):
        del self.__price

    @property
    def delivered(self):
        # código complicado que consulta os correios para saber
        # se o produto foi, de fato, entregue
        return False
