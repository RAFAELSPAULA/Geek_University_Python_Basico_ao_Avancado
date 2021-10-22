n = int(input('Digite um número: '))
contador = 1
pares = 0

while True:
    if n == 1000:
        break
    else:
        n = int(input('Digite um número: '))
        contador += 1
        if n % 2 == 0:
            pares += 1

print(f'Total de números: {contador}'
      f'\nTotal de Pares: {pares}')
