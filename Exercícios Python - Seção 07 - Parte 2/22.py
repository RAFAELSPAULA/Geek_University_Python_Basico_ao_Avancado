matriza = []
matrizb = []
matrizc = []

for x in range(3):
    matriza.append([])
    matrizb.append([])
    matrizc.append([])
    for y in range(3):
        matriza[x].append(int(input(f'Digite o valor da posição ({y}, {x}) da MATRIZ A: ')))
        matrizb[x].append(int(input(f'Digite o valor da posição ({y}, {x}) da MATRIZ B: ')))

soma = 0
for h in range(3):
    for i in range(3):
        for j in range(3):
            soma += matriza[i][j] * matrizb[j][h]
        matrizc[i].append(soma)
        soma = 0

print('MATRIZ A', 'MATRIZ B'.center(25), 'MATRIZ C'.center(35))
for n in range(3):
    print(f'{matriza[n]}   X', f'{matrizb[n]}   ='.center(22), f'{matrizc[n]}'.center(36))
