matriz = []
soma = [0, 0, 0]

for x in range(3):
    matriz.append([])
    for y in range(3):
        matriz[x].append(int(input(f'Digite o {y + 1}º valor da {x + 1}ª linha da matriz: ')))
print(f'\n')

for i in matriz:
    print(f'{i}')
    for n in range(3):
        soma[n] += i[n]

print(f'{soma} SOMA')