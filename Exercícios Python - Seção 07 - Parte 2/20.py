import random

matriz = [[], [], []]

for l in range(3):
    for c in range(6):
        matriz[l].append(random.randint(0, 20))

for linha in range(3):
    for coluna in range(6):
        print(f'[{matriz[linha][coluna]:^5}]', end='')

    print()

print('-' * 30)
soma_imp = 0
for l in range(3):
    for c in range(0, 5, 2):
        soma_imp += matriz[l][c]

print(f'A soma de todos os elementos das colunas ímpares é {soma_imp}')

print('-' * 30)
media_arit = 0
for l in range(3):
    for c in range(1, 4, 2):
        media_arit += matriz[l][c]

print(f'A média aritmética dos elementos da segunda e quarta coluna é {media_arit / 2:.1f}')

print('-' * 30)
soma = 0
for l in range(3):
    for c in range(0, 2):
        soma += matriz[l][c]

for l in range(3):
    for c in range(5, 6):
        matriz[l][c] = soma

print('Substituindo os valores da sexta coluna pela soma dos valores da coluna 1 e 2:\n')
for linha in range(3):
    for coluna in range(6):
        print(f'[{matriz[linha][coluna]:^5}]', end='')

    print()
