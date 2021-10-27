lista = []
lista2 = []

while len(lista) < 3:
    n = int(input('Digite um número: '))
    if (n < 0) or (n > 50):
        print('Número invalido! Gentileza digitar um número de 0 a 50')
    else:
        lista.append(n)

print(lista)

for i in lista:
    if i % 2 == 1:
        lista2.append(i)

print(lista2)
