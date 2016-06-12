""" Módulo de números da sequência de Fibonacci """


def fib(n):
    """ Exibe na tela a sequência de Fibonacci até n """
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

    
def fib2(n):   # return Fibonacci series up to n
    """ Retorna uma lista contendo os números da sequência de Fibonacci até n """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
