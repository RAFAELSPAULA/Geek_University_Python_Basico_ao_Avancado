import math


def neperiano(n):
    soma = 0
    for i in range(0, n):
        soma = soma + (1 / math.factorial(i))
    return soma


print(neperiano(5))
