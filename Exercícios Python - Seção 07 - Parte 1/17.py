lista = []

while len(lista) < 10:
    n = int(input('Digite um número: '))
    if n < 0:
        lista.append(0)
    else:
        lista.append(n)


print(lista)
