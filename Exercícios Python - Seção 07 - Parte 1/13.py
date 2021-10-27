lista = []

for i in range(5):
    lista.append(float(input('Digite valor: ')))

print(max(lista))
print(lista.index(max(lista)))
print(min(lista))
print(lista.index(min(lista)))
