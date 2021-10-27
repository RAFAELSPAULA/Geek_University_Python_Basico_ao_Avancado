lista = []

while len(lista) < 6:
    n = int(input('Digite um valor par: '))
    if n % 2 == 1:
        print('Valor não é par!!')
        n = int(input('Digite um valor par: '))
    lista.append(n)

lista.reverse()
print(lista)
