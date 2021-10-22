"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:

* Número digitado ao quadrado
* A raiz quadrada do número digitado.
"""
a = float(input('Digite um número real: '))
r = a ** 0.5
e = a ** 2

if a > 0:
    print(f'Número ao quadrado: {e}')
    print(f'Raiz Quadrada: {r}')
else:
    print('Não é positivo.')
