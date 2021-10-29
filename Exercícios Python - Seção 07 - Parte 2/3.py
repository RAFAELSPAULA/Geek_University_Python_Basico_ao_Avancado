matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
produto = 0

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = (l+1) * (c+1)

print('-=' * 30)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^5}]', end='')

    print()
