lista = []

while len(lista) < 10:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor Já digitado')
    else:
        lista.append(n)

print(lista)
