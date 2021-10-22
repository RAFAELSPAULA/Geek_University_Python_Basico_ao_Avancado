n = int(input('Digite um número entre 100 a 999: '))

while True:
    if n < 100 or n > 999:
        print('Número Invalido tente novamente: ')
        n = int(input('Digite um número entre 100 a 999: '))
    else:
        break

lista = str(n)
print(f'Parte um: {lista[0]}'
      f'\nParte dois: {lista[1]}'
      f'\nParte Três: {lista[2]}')
