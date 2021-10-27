lista = []
soma = 0
count = 0

while len(lista) < 10:
    n = float(input('Digite valor: '))
    lista.append(n)

for i in range(10):
    if lista[i] > 0:
        soma += lista[i]
    if lista[i] < 0:
        count += 1

print(soma)
print(count)
