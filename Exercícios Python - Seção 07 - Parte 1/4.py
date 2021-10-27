lista = []

for i in range(8):
    lista.append(int(input('Digite valor: ')))

x = int(input('Digite valor de x: '))
while x >= 8:
    print('Index Maior que permitido')
    x = int(input('Digite valor de x: '))

y = int(input('Digite valor de y: '))
while y >= 8:
    print('Index Maior que permitido')
    y = int(input('Digite valor de y: '))

soma = lista[x] + lista[y]

print(soma)
