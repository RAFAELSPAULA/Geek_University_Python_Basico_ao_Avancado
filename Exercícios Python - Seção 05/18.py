"""
Faça um programa que mostre ao usuário um menu com 4 opções de operações matemática (as básicas, por exemplo). O usuário
escolhe uma das opções e o seu programa então pede dois valores numérico e realiza a operação, mostrando o resultado e
saindo.
"""
option = int(input('Digite a opção desejada, sendo 1 Soma, 2 Subtração, 3 Divisão e 4 Multiplicação: '))

if option == 1:
    valor1 = float(input('Digite primeiro valor: '))
    valor2 = float(input('Digite segundo valor: '))
    soma = valor1 + valor2
    print(soma)
elif option == 2:
    valor1 = float(input('Digite primeiro valor: '))
    valor2 = float(input('Digite segundo valor: '))
    sub = valor1 - valor2
    print(sub)
elif option == 3:
    valor1 = float(input('Digite primeiro valor: '))
    valor2 = float(input('Digite segundo valor: '))
    div = valor1/valor2
    print(div)
elif option == 4:
    valor1 = float(input('Digite primeiro valor: '))
    valor2 = float(input('Digite segundo valor: '))
    mult = valor1 * valor2
    print(mult)
else:
    print('Opção Inválida')
