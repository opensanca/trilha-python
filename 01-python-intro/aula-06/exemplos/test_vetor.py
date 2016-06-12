from unittest import TestCase

from vetor import Vetor, soma_vetor, subtrai_vetor


class TesteVetor(TestCase):
    def test_soma(self):
        result = soma_vetor(Vetor(1, 1), Vetor(1, 2))
        self.assertEqual(result, Vetor(x=2, y=3))


    def test_subtrai(self):
        result = subtrai_vetor(Vetor(-1, 5), Vetor(0, 3))
        self.assertEqual(result, Vetor(x=-1, y=2))
