"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
"""

num = int(input('Digite um Número inteiro: '))
sucessor = (num - 1) * 3
ante = (num + 1 ) * 2
soma = sucessor + ante
print(f'Soma: {soma}')
