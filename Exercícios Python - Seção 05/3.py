"""
Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o número ao quadrado.
"""
a = float(input('Digite um número real: '))
r = a ** 0.5
e = a ** 2

if a > 0:
    print(f'Raiz Quadrada: {r}')
else:
    print(f'Número ao quadrado: {e}')
