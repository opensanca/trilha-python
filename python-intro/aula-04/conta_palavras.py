"""
Este arquivo apresenta diferentes formas de contar as palavras de uma frase
usando dicts e o módulo collections (https://docs.python.org/2/library/collections.html)
"""

from collections import Counter, defaultdict


def conta_palavras(frase):
    """
    Recebe uma palavra e retorna um dicionário em que a chave é uma palavra
    e seu valor a quantidade de vezes que essa palavra está presente na frase
    """

    d = {}
    for palavra in frase.lower().split():
        if palavra in d:
            d[palavra] += 1
        else:
            d[palavra] = 1
    return d


def conta_palavras(frase):
    d = defaultdict(int)
    for palavra in frase.lower().split():
        d[palavra] += 1
    return d


def conta_palavras(frase):
    return Counter(frase.lower().split())


# seu código estará correto se nenhuma das linhas abaixo levantar exceção
assert conta_palavras("quod dolore dolore dolore modi sapiente quod ullam nostrum ullam") == {'ullam': 2, 'sapiente': 1, 'quod': 2, 'nostrum': 1, 'dolore': 3, 'modi': 1}
assert conta_palavras("soluta Soluta sapiente sapiente nostrum Sapiente dolore nostrum modi ullam") == {'ullam': 1, 'sapiente': 3, 'nostrum': 2, 'dolore': 1, 'soluta': 2, 'modi': 1}
assert conta_palavras("quod dolore dolore soluta sapiente sapiente dolore quod sapiente modi") == {'dolore': 3, 'quod': 2, 'soluta': 1, 'modi': 1, 'sapiente': 3}
assert conta_palavras("dolore Dolore quis quod dolore nostrum quod Nostrum sapiente soluta") == {'sapiente': 1, 'quod': 2, 'nostrum': 2, 'soluta': 1, 'dolore': 3, 'quis': 1}
assert conta_palavras("sapiente sapiente quod soluta quis ullam nostrum soluta ullam ullam") == {'ullam': 3, 'sapiente': 2, 'quod': 1, 'nostrum': 1, 'soluta': 2, 'quis': 1}
assert conta_palavras("modi Sapiente dolore Soluta sapiente quis soluta modi dolore ullam") == {'ullam': 1, 'sapiente': 2, 'quis': 1, 'dolore': 2, 'soluta': 2, 'modi': 2}
assert conta_palavras("quis quis nostrum nostrum sapiente quis nostrum quod quis dolore") == {'sapiente': 1, 'quod': 1, 'quis': 4, 'nostrum': 3, 'dolore': 1}
assert conta_palavras("nostrum sapiente quis ullam ullam quod ullam nostrum ullam soluta") == {'ullam': 4, 'sapiente': 1, 'quod': 1, 'nostrum': 2, 'soluta': 1, 'quis': 1}
assert conta_palavras("sapiente ullam quod quis dolore modi Quis quod dolore nostrum") == {'ullam': 1, 'sapiente': 1, 'quod': 2, 'quis': 2, 'nostrum': 1, 'dolore': 2, 'modi': 1}
assert conta_palavras("modi nostrum ullam Quis Soluta modi quis ullam modi ullam") == {'ullam': 3, 'soluta': 1, 'modi': 3, 'nostrum': 1, 'quis': 2}
