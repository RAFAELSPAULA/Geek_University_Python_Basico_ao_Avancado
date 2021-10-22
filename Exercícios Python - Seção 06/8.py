maior = 0
menor = 9999

for i in range(1, 11):
    n = float(input(f'Digite o {i}° Valor: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n

print(f'Maior Número: {maior}'
      f'\nMenor Número: {menor}')
