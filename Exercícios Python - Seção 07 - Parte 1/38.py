
lista = []

while len(lista) < 10:
    n = int(input('Digite um valor: '))
    lista.append(n)
    for i in lista:
        novo = sorted(lista)

    print(novo)

