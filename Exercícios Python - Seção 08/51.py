def matriz():
    matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    soma = 0

    for l in range(0, 3):
        for c in range(0, 3):
            matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

    print('-=' * 30)

    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[{matriz[l][c]:^5}]', end='')
            if l + c == 3 - 1:  # 3 e a ordem da matriz
                soma += matriz[l][c]
        print()

    print(soma)


matriz()
