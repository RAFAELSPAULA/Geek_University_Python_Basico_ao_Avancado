import random

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = random.randint(0, 20)

matriz1 = matriz
print('-=' * 30)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^5}]', end='')
        if l < c:
            matriz1[l][c] *= 0
    print()

print('-=' * 30)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz1[l][c]:^5}]', end='')
    print()

