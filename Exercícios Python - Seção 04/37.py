"""
Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%
"""
v = float(input('Digite o valor: '))
d = v * 0.12
vf = v - d
print(f'Valor com desconto: {vf}')
