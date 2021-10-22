maior = 0
rep = 0

n = int(input('Digite um número: '))

for i in range(1, n+1):
    n = float(input(f'Digite o {i}° Valor: '))
    if n >= maior:
        maior = n
        rep += 1


print(f'Maior Número: {maior}'
      f'\nQuantidade de vezes repetida: {rep}')
