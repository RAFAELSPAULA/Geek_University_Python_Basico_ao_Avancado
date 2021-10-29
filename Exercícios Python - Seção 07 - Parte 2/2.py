matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
coluna = 0

for l in range(0, 5):
    matriz[l][coluna] = 1
    coluna += 1

print('-=' * 30)

for l in range(0, 5):
    for c in range(0, 5):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
