lista = []
lista2 = []

while len(lista) < 5:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if lista.count(n) != 2:
        lista2.append(n)

print(lista2)
