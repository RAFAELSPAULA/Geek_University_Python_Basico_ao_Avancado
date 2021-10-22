"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido". Se o número for positivo,
calcular o logaritmo deste número.
"""
import math

n = int(input('Digite um número: '))

if n < 0:
    print('Número inválido')
else:
    print(math.log10(n))
