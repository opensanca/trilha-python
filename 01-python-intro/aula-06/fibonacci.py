""" Módulo de números da sequência de Fibonacci """


def fib(n):
    """
    Exibe na tela a sequência de Fibonacci até n

    >>> fib(10)
    1 1 2 3 5 8 
    >>> fib(-1)
    <BLANKLINE>
    """
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n):   # return Fibonacci series up to n
    """
    Retorna uma lista contendo os números da sequência de Fibonacci até n

    >>> fib2(10)
    [1, 1, 2, 3, 5, 8]
    >>> fib2(-1)
    []
    """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])
    fib(n)
