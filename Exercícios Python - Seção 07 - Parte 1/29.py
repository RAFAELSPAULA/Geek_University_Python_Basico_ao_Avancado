v = []
v1 = []
v2 = []
soma = 0
cont = 0

for c in range(6):
    v.append(int(input(f'Informe o {c+1}° valor: ')))

for elemento in v:
    if elemento % 2 == 1:
        v1.append(elemento)
        cont += 1
    else:
        v2.append(elemento)
        soma += elemento

print(f'Pares: {v2} - Soma: {soma}\nÍmpares: {v1} - Quantidade: {cont}')
