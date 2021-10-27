lista = []

for i in range(10):
    lista.append(float(input('Digite valor: ')))

print(max(lista))
print(lista.index(max(lista)))
