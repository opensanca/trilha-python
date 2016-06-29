import abc


# Python 3.5
class Tombola(abc.ABC):
    """ Globo de bingo
    - Carregar itens
    - Inspecionar itens
    - Saber se está vazia
    - Sortear itens
    - Misturar itens

    A tombola deve armazenar seus itens num atributo chamado itens.
    """

    @abc.abstractmethod
    def carrega(self, itens):
        """ Adiciona itens a partir de um iterável. """

    @abc.abstractmethod
    def sorteia(self):
        """ Remove o último item

        Deve levantar um `LookupError` quando a instancia estiver vazia.
        """

    def vazia(self):
        return bool(self.inspeciona())

    def inspeciona(self):
        itens = []
        if isinstance(self.itens, list):
            return tuple(self.itens)
        while True:
            try:
                itens.append(self.sorteia())
            except LookupError:
                break
        self.carrega(itens)
        return tuple(itens)


class GaiolaBingo(Tombola):
    def __init__(self, itens):
        self.itens = list()
        self.carrega(itens)

    def carrega(self, itens):
        self.itens.extend(itens)

    def sorteia(self):
        return self.itens.pop()
