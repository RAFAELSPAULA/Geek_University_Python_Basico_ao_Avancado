"""
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = raiz quadrada(a² + b².
Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação. Imprima o resultado
dessa operação.
"""


a = float(input('Insira valor de a: '))
b = float(input('Insira valor de b: '))

h = (a ** 2 + b ** 2) ** 0.5
print(f'Hipotenusa: {h}')