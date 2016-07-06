import unittest

from baralho import Baralho, Carta


class TestaBaralho(unittest.TestCase):
    def setUp(self):
        self.baralho = Baralho()

    def testa_acesso_por_indice(self):
        self.assertEqual(self.baralho[0], Carta('2', 'copas'))
        self.assertEqual(self.baralho[-1], Carta('K', 'espadas'))

    def testa_acesso_invalido(self):
        with self.assertRaises(IndexError):
            self.baralho[52]

    def testa_fatiamento(self):
        cartas = [Carta('2', 'copas'), Carta('2', 'ouros'), Carta('2', 'paus')]
        self.assertEqual(self.baralho[:3], cartas)

    def testa_fatiamento_vazio(self):
        self.assertEqual(self.baralho[52:100], [])
