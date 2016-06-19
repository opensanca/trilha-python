from unittest import TestCase

from vetor import Vetor, soma_vetor, subtrai_vetor


class TestaVetor(TestCase):
    def testa_vetor(self):
        v = Vetor(x=1, y=-1)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, -1)

    def testa_soma(self):
        v1 = Vetor(5, 1)
        v2 = Vetor(0, 3)
        v = soma_vetor(v1, v2)
        self.assertEqual(v, Vetor(5, 4))

    def testa_subtrai(self):
        v1 = Vetor(5, 1)
        v2 = Vetor(2, 3)
        v = subtrai_vetor(v1, v2)
        self.assertEqual(v, Vetor(3, -2))
