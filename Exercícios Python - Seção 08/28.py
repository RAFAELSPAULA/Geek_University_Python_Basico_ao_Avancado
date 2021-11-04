import math


def cos(x, n):
    formula = lambda k: (-1) ** k * x ** (2 * k) / math.factorial(2 * k)
    soma = 0

    for k in range(n + 1):
        soma += formula(k)

    return soma


print(cos(0.5, 10))
