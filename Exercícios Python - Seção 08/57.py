import random

print()
vet = []

for i in range(7):
    vet.append(random.sample(range(10, 99), 6))

for i in range(len(vet)):
    for x in range(6):
        print(vet[i][x], end=' ')
    print()
print()


def soma_coluna_matriz(vet, coluna):
    soma = 0
    for i in range(len(vet)):
        soma += vet[i][coluna - 1]
    return soma


coluna = int(input('Digite um número para a coluna de 1 a 6: '))

print(f'A soma da coluna {coluna} da matriz é: {soma_coluna_matriz(vet, 2)}')
