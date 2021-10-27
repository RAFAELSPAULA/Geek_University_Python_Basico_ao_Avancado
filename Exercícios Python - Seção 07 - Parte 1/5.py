lista = []
count = 0

for i in range(10):
    lista.append(float(input('Digite valor: ')))

print(lista)

for i in range(10):
    if lista[i] % 2 == 0:
        count += 1

print(count)
