n = int(input('Digite um valor: '))

c = 0
razao = 0
h = 0

for i in range(0, n):
    c += 1
    razao = 1 / c
    h += razao

print(f'Valor da H({n}): {h}')
