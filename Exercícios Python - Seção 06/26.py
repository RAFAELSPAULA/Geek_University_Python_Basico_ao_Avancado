numero = int(input('Digite um numero: '))

while True:
    numero += 1
    if numero % 11 == 0 or numero % 13 == 0 or numero % 17 == 0:
        print(f'O próximo numero divisível por 11, 13 ou 17 eh {numero}')
        break
