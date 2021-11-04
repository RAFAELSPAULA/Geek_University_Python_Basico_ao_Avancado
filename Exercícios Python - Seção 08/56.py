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


def soma_linha_matrix(vet, linha):
    return sum(vet[linha - 1][0::])


linha = int(input('Digite a linha da matriz a ser somada: '))

print(f'A soma da linha {linha} da matriz é {soma_linha_matrix(vet, linha)}')
