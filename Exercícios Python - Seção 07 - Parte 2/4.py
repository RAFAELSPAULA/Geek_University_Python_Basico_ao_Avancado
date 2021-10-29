matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
maior = 0

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 30)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^5}]', end='')

    print()

for c in range(0, 4):
    if c == 0:
        mai = matriz[l][c]
    elif matriz[l][c] > mai:
        mai = matriz[l][c]


print(f'O maior valor da segunda linha é [{l}, {c}]: {mai}.')
