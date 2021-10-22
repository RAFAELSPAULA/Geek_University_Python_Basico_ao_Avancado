"""
Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algoritmos.
Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número não for maior que zero, programa terminará
com a mensagem "Número inválido".
"""
n = int(input('Digite um número: '))
n1 = str(n)

if n > 0:
    s = int(n1[0]) + int(n1[1]) + int(n1[2])
    print(f'Soma: {s}')
else:
    print('Número inválido')
