v = []
v1 = []
v2 = []

for c in range(10):
    v.append(int(input(f'Informe o {c+1}° valor: ')))

for elemento in v:
    if elemento % 2 == 1:
        v1.append(elemento)
    else:
        v2.append(elemento)

print(f'Pares: {v2}\nÍmpares: {v1}')
