import unittest


def soma(a, b):
    return a + b


class TestaSoma(unittest.TestCase):
    def testa_soma(self):
        self.assertEqual(soma(0, 0), 0)
        self.assertEqual(soma(1, 10), 11)
        self.assertEqual(soma(-5, 3), -2)


def test_soma():
    assert soma(0, 0) == 0
    assert soma(1, 10) == 11
    assert soma(-5, 3) == -2
