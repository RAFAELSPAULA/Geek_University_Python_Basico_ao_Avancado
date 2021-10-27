lista = []

while len(lista) < 5:
    n = float(input('Digite um valor: '))
    lista.append(n)

print(lista)
print(max(lista))
media = sum(lista) / 5
print(media)
