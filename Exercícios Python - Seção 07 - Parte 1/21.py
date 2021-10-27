lista1 = []
lista2 = []
lista3 = []

while len(lista1) < 10:
    n = int(input('Digite um valor para lista a: '))
    lista1.append(n)

while len(lista2) < 10:
    y = int(input('Digite um valor para lista b: '))
    lista2.append(y)

for i in range(10):
    c = lista1[i] - lista2[i]
    lista3.append(c)

print(lista3)

