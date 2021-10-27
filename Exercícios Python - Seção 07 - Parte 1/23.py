lista = []
lista2 = []
lista3 = []


while len(lista) < 5:
    n = float(input('Digite um número para lista a: '))
    lista.append(n)

while len(lista2) < 5:
    y = float(input('Digite um número para lista b: '))
    lista2.append(y)

print(lista)
print(lista2)

for i in range(5):
    c = lista[i] * lista2[i]
    lista3.append(c)

print(lista3)
print(sum(lista3))
