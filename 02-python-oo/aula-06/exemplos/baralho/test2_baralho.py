import pytest

from baralho import Baralho, Carta


@pytest.fixture(scope='module')
def baralho():
    return Baralho()


def testa_acesso_por_indice(baralho):
    assert baralho[0] == Carta('2', 'copas')


@pytest.mark.teste_lento
def testa_acesso_invalido(baralho):
    with pytest.raises(IndexError):
        baralho[52]


@pytest.mark.teste_legado
def testa_fatiamento(baralho):
    assert baralho[:2] == [Carta('2', 'copas'), Carta('2', 'ouros')]


def testa_fatiamento_vazio(baralho):
    assert baralho[52:100] == []
