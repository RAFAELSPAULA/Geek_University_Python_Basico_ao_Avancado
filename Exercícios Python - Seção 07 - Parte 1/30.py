conjunto = []
conjunto1 = []

for c in range(10):
    conjunto.append(int(input(f'Informe o {c+1}° valor: ')))

for c in range(10):
    conjunto1.append(int(input(f'Informe o {c+1}° valor: ')))

a = set(conjunto)
b = set(conjunto1)

ambos1 = a.intersection(b)

print(ambos1)
