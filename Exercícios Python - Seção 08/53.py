import random

n = random.randint(2, 4)
vet = []
for i in range(n):
    vet.append(random.sample(range(10, 99), n))

for i in range(len(vet)):
    for x in range(len(vet)):
        vet[i][x] = 0

dig = random.randint(1, 3)
if dig == 2:
    x = 0
elif dig == 3:
    x = n - 1

if dig == 1:
    for i in range(n):
        for x in range(n):
            if random.randint(1, 3) % 2 == 0:
                vet[i][x] = 1
else:
    for i in range(n):
        if dig == 2:
            vet[i][x] = 1
            x += 1
        elif dig == 3:
            vet[i][x] = 1
            x -= 1

print()
for i in range(len(vet)):
    for x in range(len(vet)):
        print(vet[i][x], end=' ')
    print()
print()


def eh_matriz_identidade(vet):
    def conta(vet, elm):
        soma = 0
        for element in vet:
            soma += element.count(elm)
        return soma

    if conta(vet, 1) == len(vet):
        conta_dig_p = 0
        conta_dig_s = 0
        x = 0
        y = len(vet) - 1
        for i in range(len(vet)):
            if vet[i][x] == 1:
                conta_dig_p += 1
            if vet[i][y] == 1:
                conta_dig_s += 1
            x += 1
            y -= 1

        if (conta_dig_p == len(vet) or conta_dig_s == len(vet)) and \
                (conta(vet, 0) == (len(vet) ** 2) - conta_dig_p or conta(vet, 0) == (len(vet) ** 2) - conta_dig_s):
            return True

        return False

    return False


if eh_matriz_identidade(vet):
    print('É matriz identidade')
else:
    print('Não é matriz identidade')
