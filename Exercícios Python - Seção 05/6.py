"""
Escreva um programa que, dados dois número inteiros, mostre na tela o maior deles, assim como a diferença existente
entre ambos.
"""
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
d1 = a - b
d2 = b - a

if a > b:
    print(f'Maior Número: {a}')
    print(f'Diferença: {d1}')
else:
    print(f'Maior Número: {b}')
    print(f'Diferença: {d2}')
