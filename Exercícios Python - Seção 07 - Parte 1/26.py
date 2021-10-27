lista = []
n = 8
soma = 0
var = 0

for i in range(n):
    lista.append(int(input(f'Digite o {i + 1}º valor: ')))
    soma += lista[i]

m = soma / n

for j in lista:
    var += (j - m) ** 2
s = var / (n - 1)

d = s ** 0.5
print(d)
