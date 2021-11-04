import random


def soma():
    matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    soma = 0
    for l in range(0, 4):
        for c in range(0, 4):
            matriz[l][c] = random.randint(0, 10)

    print('-=' * 30)

    for l in range(0, 4):
        for c in range(0, 4):
            print(f'[{matriz[l][c]:^5}]', end='')
            soma += matriz[l][c]
        print()
    print(soma)


soma()
