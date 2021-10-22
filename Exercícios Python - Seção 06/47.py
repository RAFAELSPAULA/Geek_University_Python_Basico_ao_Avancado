menu = int(input('Escolha uma das seguintes opções '
                 '\n 1 - Adição'
                 '\n 2 - Subtração'
                 '\n 3 - Multiplicação'
                 '\n 4 - divisão'
                 '\n 5 - Sair \n'))

while True:
    if menu != 1 and menu != 2 and menu != 3 and menu != 4:
        print('Opção Inválida, tente novamente!')
        menu = int(input('Escolha uma das seguintes opções '
                         '\n 1 - Adição'
                         '\n 2 - Subtração'
                         '\n 3 - Multiplicação'
                         '\n 4 - divisão'
                         '\n 5 - Sair \n'))
    if menu == 1:
        n = int(input('Digite Primeiro Valor: '))
        n1 = int(input('Digite Segundo Valor: '))
        soma = n + n1
        print(f'Valor da soma: {soma}')
        menu = int(input('Escolha uma das seguintes opções '
                         '\n 1 - Adição'
                         '\n 2 - Subtração'
                         '\n 3 - Multiplicação'
                         '\n 4 - divisão'
                         '\n 5 - Sair \n'))
    if menu == 2:
        n = int(input('Digite Primeiro Valor: '))
        n1 = int(input('Digite Segundo Valor: '))
        sub = n - n1
        print(f'Valor da sub: {sub}')
        menu = int(input('Escolha uma das seguintes opções '
                         '\n 1 - Adição'
                         '\n 2 - Subtração'
                         '\n 3 - Multiplicação'
                         '\n 4 - divisão'
                         '\n 5 - Sair \n'))
    if menu == 3:
        n = int(input('Digite Primeiro Valor: '))
        n1 = int(input('Digite Segundo Valor: '))
        mult = n * n1
        print(f'Valor da multiplicação: {mult}')
        menu = int(input('Escolha uma das seguintes opções '
                         '\n 1 - Adição'
                         '\n 2 - Subtração'
                         '\n 3 - Multiplicação'
                         '\n 4 - divisão'
                         '\n 5 - Sair \n'))
    if menu == 4:
        n = int(input('Digite Primeiro Valor: '))
        n1 = int(input('Digite Segundo Valor: '))
        div = n / n1
        print(f'Valor da divisão: {div}')
        menu = int(input('Escolha uma das seguintes opções '
                         '\n 1 - Adição'
                         '\n 2 - Subtração'
                         '\n 3 - Multiplicação'
                         '\n 4 - divisão'
                         '\n 5 - Sair \n'))
    if menu == 5:
        break
