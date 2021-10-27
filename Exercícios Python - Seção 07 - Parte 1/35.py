a = list()
b = list()

while True:
    numero = int(input('Digite um número de 1 a 9999: '))
    if numero > 9999:
        print('Número inválido')
    else:
        break

while True:
    numero2 = int(input('Digite um número de 1 a 9999: '))
    if numero2 > 9999:
        print('Número inválido')
    else:
        break

unidade = numero // 1 % 10
unidade_2 = numero2 // 1 % 10

dezena = numero // 10 % 10
dezena_2 = numero2 // 10 % 10

centena = numero // 100 % 10
centena_2 = numero2 // 100 % 10

milhar = numero // 1000 % 10
milhar_2 = numero2 // 1000 % 10

a.append(unidade)
a.append(dezena)
a.append(centena)
a.append(milhar)

b.append(unidade_2)
b.append(dezena_2)
b.append(centena_2)
b.append(milhar_2)

print(a)
print(b)

soma_das_listas = list()

for i, v in enumerate(a):
    soma = v + b[i]

    if soma >= 10:
        if not i == len(a) - 1:
            soma -= 10
            a[i + 1] += 1
        soma_das_listas.append(soma)
    else:
        soma_das_listas.append(soma)

lista_str = []

for v in soma_das_listas:
    valor = str(v)
    lista_str.append(valor)

lista_str = lista_str[::-1]
print(lista_str)

m, c, d, u = lista_str

valor_soma = m + c + d + u

print(f'O valor das listas somadas é igual a: {valor_soma}')
