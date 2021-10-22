"""
Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.
"""
a = int(input('Digite um valor: '))
r = a % 2

if r == 0:
    print('Número e par')
else:
    print('Número e ímpar')
