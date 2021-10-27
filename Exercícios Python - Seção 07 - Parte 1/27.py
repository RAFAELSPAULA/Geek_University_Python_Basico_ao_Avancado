lista = []
primo = []
q = 1
cont = 0

while len(lista) < 10:
    valor = int(input(f'Digite o {q}º valor inteiro do vetor: '))
    lista.append(valor)
    q += 1

for x in range(1, 101):
    cont = 0
    for y in range(1, x+1):
        if x % y == 0:
            cont += 1
    if cont == 2:
        primo.append(x)

a = set(lista)
b = set(primo)

ambos1 = a.intersection(b)
primoLista = list(ambos1)

print(lista)
print(primoLista)

for x in range(1, 101):
    cont = 0
    for y in range(1, x+1):
        if x % y == 0:
            cont += 1
    if cont == 2:
        print(lista.index(x))



