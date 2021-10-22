"""
Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a
mensagem número iguais.
"""
a = float(input('Digite um valor: '))
b = float(input('Digite um valor: '))

if a > b:
    print(f'Maior Valor: {a}')
elif b > a:
    print(f'Maior Valor: {b}')
else:
    print('Número Iguais')