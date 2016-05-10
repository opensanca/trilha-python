import timeit

vezes = 100
print('tamanho  | tempo set + for | tempo set + & | for vs &')
for tamanho in (10 ** i for i in range(2, 7)):
    setup = """\
from faker import Factory

faker = Factory.create('pt_BR')

nomes = {{faker.name() for _ in range({})}}
buscas = {{faker.name() for _ in range(1000)}}\
    """
    setup = setup.format(tamanho)

    codigo_for = """\
presentes = []
for busca in buscas:
    if busca in nomes:
        presentes.append(busca)
    """
    tempo = timeit.timeit(codigo_for, setup=setup, number=vezes)
    media_for = tempo / vezes

    tempo = timeit.timeit('buscas & nomes', setup=setup, number=vezes)
    media_set = tempo / vezes

    msg = '{:<9}| {:<16}| {:<14}| & é {:<}x + rápido'
    msg = msg.format(tamanho, round(media_for, 8), round(media_set, 8),
                     round(media_for / media_set, 2))
    print(msg)
