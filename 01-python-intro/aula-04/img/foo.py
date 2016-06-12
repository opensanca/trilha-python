def inverte_numero(n, pot=None):
    if pot is None:
        num = n
        pot = -1
        while num > 0:
            num = num // 10
            pot += 1
    div, mod = divmod(n, 10)
    num = mod * (10 ** pot)
    if div == 0:
        return num
    return inverte_numero(div, pot - 1) + num


def inverte(s):
    char = s[0]
    if len(s) == 1:
        return char
    return inverte(s[1:]) + char


def imprime_ate(n):
    if n == 0:
        return
    imprime_ate(n - 1)
    print(n)


print(inverte_numero(123456))
print(inverte("alo"))
imprime_ate(20)
