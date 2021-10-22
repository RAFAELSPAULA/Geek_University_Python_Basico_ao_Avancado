"""
Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos
dois.
"""
n = int(input('Digite um número: '))

if n % 3 == 0 and n % 5 == 0:
    print('Item inválido, divisível por ambos')
elif n % 3 == 0 or n % 5 == 0:
    print('Divisível por 3 ou 5')
else:
    print('Número não é divisível nem por 3 ou 5')
