"""
Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
"""

num1 = float(input('Primeiro Valor: '))
num2 = float(input('Segundo Valor: '))
num3 = float(input('Terceiro Valor: '))

soma = num1 + num2 + num3
quadrado = soma ** 2
print(f'Soma dos quadrados: {quadrado}')
