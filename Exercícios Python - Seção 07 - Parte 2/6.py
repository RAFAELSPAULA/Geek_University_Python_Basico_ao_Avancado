matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matriz1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matriz2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
maior = 0

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input(f'Digite um valor para Matriz A [{l}, {c}]: '))

print('-=' * 30)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^5}]', end='')

    print()

for l in range(0, 4):
    for c in range(0, 4):
        matriz1[l][c] = int(input(f'Digite um valor para Matriz B [{l}, {c}]: '))

print('-=' * 30)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz1[l][c]:^5}]', end='')

    print()

print('-=' * 30)

for l in range(0, 4):
    for c in range(0, 4):
        matriz2[l][c] = matriz[l][c] + matriz1[l][c]
        print(f'[{matriz2[l][c]:^5}]', end='')

    print()