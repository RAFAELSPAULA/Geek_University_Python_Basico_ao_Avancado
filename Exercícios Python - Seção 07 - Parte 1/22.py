lista = []
lista2 = []
par = []
impar = []

while len(lista) < 10:
    n = int(input('Digite um número para lista a: '))
    lista.append(n)

while len(lista2) < 10:
    y = int(input('Digite um número para lista b: '))
    lista2.append(y)


for i in lista:
    if i % 2 == 0:
        par.append(i)

for i in lista2:
    if i % 2 == 1:
        impar.append(i)

print(f'Lista par {par}')
print(f'lista ímpar {impar}')
