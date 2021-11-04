import numpy as np


def fracao(a, b, c, d):
    f1 = a / b
    f2 = c / d
    return print(f1, f2)


fracao(1, 2, 1, 2)


def mmc():
    return np.lcm(2, 2)


print(mmc())


def calculadora(a, b, c, d):
    soma = (a / b) + (c / d)
    sub = (a / b) - (c / d)
    mult = (a / b) * (c / d)
    div = (a / b) / (c / d)
    return soma, sub, mult, div


print(calculadora(1, 2, 1, 2))
