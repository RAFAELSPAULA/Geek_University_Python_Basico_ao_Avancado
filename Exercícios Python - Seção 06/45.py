menu = str(input('Digite M para m/s, K para km/h ou sair para finalizar: '))

while True:
    if menu != 'M' or menu != 'K' or menu != 'sair':
        print('Opção Inválida')
        menu = str(input('Digite M para m/s, K para km/h ou sair para finalizar: '))
    if menu == 'M':
        n = float(input('Digite valor: '))
        metro = n * 3.6
        print(f'Valor em m/s {metro}')
        menu = str(input('Digite M para m/s, K para km/h ou sair para finalizar: '))
    if menu == 'K':
        n = float(input('Digite valor: '))
        ki = n / 3.6
        print(f'Valor em Km/h {ki}')
        menu = str(input('Digite M para m/s, K para km/h ou sair para finalizar: '))
    if menu == 'sair':
        break

