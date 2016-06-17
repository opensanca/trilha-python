class Cão:
    qtd_patas = 4
    carnívoro = True
    nervoso = False

    def __init__(self, nome, data_nascimento=None):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def latir(self, vezes=1):
        """ Latir do cão. Quanto mais nervoso mais late. """

        vezes += self.nervoso * vezes
        latido = 'Au! ' * vezes
        print('{}: {}'.format(self.nome, latido))


class GoldenRetriever(Cão):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.itens = []

    def pega(self, item):
        """ busca/pega um item quando ordenado """
        self.itens.append(item)
        print('{} pegou {}'.format(self.nome, item))

    def devolve(self, item):
        """ devolve um item, caso o item não seja especificado retorna o último que pegou """
        if not self.itens:
            raise ValueError('{} não está segurando item algum!'.format(self.nome))

        if item not in self.itens:
            raise ValueError('{} não está segurando {}!'.format(self.nome, item))

        self.itens.remove(item)
        print('{} devolve {}'.format(self.nome, item))
        return item

    def devolve_ultimo(self):
        if not self.itens:
            raise ValueError('{} não está segurando item algum!'.format(self.nome))

        return self.itens.pop()


class Pinscher(Cão):
    nervoso = True

    def latir(self, vezes=1):
        vezes *= 2
        super().latir(vezes)


class SãoBernardo(Cão):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.doses = 10

    def servir(self):
        if self.doses == 0:
            raise ValueError('Cabô a cachaça!')

        self.doses -= 1
        print('Alguém está começando a ficar bebado (restam {} doses)'.format(self.doses))
