from unittest import TestCase

from fibonacci import fib2


class TesteFibonacci(TestCase):
    def testa_fib2_entrada_invalida(self):
        sequencia = fib2(-1)
        self.assertEqual(sequencia, [])

    def testa_fib2(self):
        sequencia = fib2(100)
        self.assertEqual(sequencia, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
