import random


def soma():
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    somaP = 0
    somaS = 0
    for l in range(0, 3):
        for c in range(0, 3):
            matriz[l][c] = random.randint(0, 10)

    print('-=' * 30)

    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[{matriz[l][c]:^5}]', end='')
            if l == c:
                somaP += matriz[l][c]
            if l + c == 3 - 1:  # 3 e a ordem da matriz
                somaS += matriz[l][c]

        print()
    print(somaP)
    print(somaS)


soma()
