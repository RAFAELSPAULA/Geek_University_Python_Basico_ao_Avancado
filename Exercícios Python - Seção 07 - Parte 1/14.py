lista = []
igual = []


while len(lista) < 10:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if lista.count(n) == 2:
        igual.append(n)

print(lista)
print(igual)

