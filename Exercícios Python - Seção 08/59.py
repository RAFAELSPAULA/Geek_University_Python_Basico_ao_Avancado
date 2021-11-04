n = int(input('Quantos valores vai ter cada vetor? '))

vet1: [float] = [0 for x in range(n)]
vet2: [float] = [0 for x in range(n)]
vet3: [float] = [0 for x in range(n)]

print('Digite os valores do vetor A:')
for i in range(0, n):
    vet1[i] = float(input())

print('Digite os valores do vetor B:')
for i in range(0, n):
    vet2[i] = float(input())


def vetor():
    print('VETOR RESULTANTE:')
    for i in range(0, n):
        vet3[i] = vet1[i] + vet2[i]
        print(vet3[i])


vetor()
