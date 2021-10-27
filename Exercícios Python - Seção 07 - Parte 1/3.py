lista1 = []

while len(lista1) < 6:
    n = float(input('Digite um Valor real: '))
    lista1.append(n)

lista2 = []

print(lista1)

for lista1 in lista1:
    lista2.append(lista1*lista1)

print(lista2)
