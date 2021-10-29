matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
cont = achar = 0

x = int(input('Digite um valor para procurar : '))

for l in range(0, 5):
    for c in range(0, 5):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 30)

for l in range(0, 5):
    for c in range(0, 5):
        print(f'[{matriz[l][c]:^5}]', end='')

    print()

for l in matriz:
    cont += 1
    if x in l:
        print(f'Posição [{cont}, {l.index(x)}]')
    else:
        achar += 1
