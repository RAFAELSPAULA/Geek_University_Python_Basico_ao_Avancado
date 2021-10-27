lista = []

while len(lista) < 10:
    n = float(input('Digite um número: '))
    lista.append(n)

for i in lista:
    novo = sorted(lista)

print(novo)
