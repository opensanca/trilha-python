"""
Define um gerador que produz os números da sequência de fibonacci (em teoria) infinitamente
"""


def fib():
    a, b = 0, 1
    while True:
        a, b = b, b + a
        yield b
