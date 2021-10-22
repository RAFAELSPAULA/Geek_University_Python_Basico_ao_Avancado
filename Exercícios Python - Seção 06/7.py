soma = 0
base = 0


for i in range(1, 11):
    n = float(input(f'Digite o {i}° Valor: '))
    if n > 0:
        soma = soma + n
        base = base + 1

media = soma / base
print(f'Media: {media}')
