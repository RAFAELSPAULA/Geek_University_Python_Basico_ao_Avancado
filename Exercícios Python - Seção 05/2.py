"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for
negativo, mostre uma mensagem dizendo que o número é inválido.
"""
a = float(input('Digite um valor: '))
r = a ** 0.5

if a < 0:
    print('Número invalido.')
else:
    print(f'Valor da Raiz Quadrada: {r}')