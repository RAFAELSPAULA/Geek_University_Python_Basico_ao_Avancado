"""
Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre qual
a classificação dessa pessoa.

Altura menor que 1.20 - Peso até 60 (A) - Entre 60 e 90 (D) - acima de 90 (G)
De 1.20 a 1.70 - B - E - H
Maior que 1.70 - C - F - I
"""
a = float(input('Digite sua Altura: '))
p = float(input('Digite seu Peso: '))

if a < 1.20:
    if p <= 60:
        print('A')
    elif (p > 60) and (p <= 90):
        print('D')
    else:
        print('G')
elif (a > 1.20) and (a < 1.70):
    if p <= 60:
        print('B')
    elif (p > 60) and (p <= 90):
        print('E')
    else:
        print('H')
else:
    if p <= 60:
        print('C')
    elif (p > 60) and (p <= 90):
        print('F')
    else:
        print('I')
