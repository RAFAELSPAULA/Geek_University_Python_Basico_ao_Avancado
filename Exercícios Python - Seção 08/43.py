from random import randint


def random(a, b, c, d):
    dicionario = {a, b, c, d}
    return dicionario


print(random(randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5)))