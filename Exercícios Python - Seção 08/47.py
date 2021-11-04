def matriz():
    matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    maior = 0

    for l in range(0, 4):
        for c in range(0, 4):
            matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

    print('-=' * 30)

    for l in range(0, 4):
        for c in range(0, 4):
            print(f'[{matriz[l][c]:^5}]', end='')
            if matriz[l][c] > 10:
                maior += 1
        print()

    print(f'Tem um total de {maior}')


matriz()