import math


def soma_algarismo(n):
    if n > 0:
        return sum([int(i) for i in list(str(n))])
    else:
        return 'Número inválido!'


print(soma_algarismo(math.factorial(4)))

