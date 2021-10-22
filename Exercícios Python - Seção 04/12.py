"""
Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de conversão é: K = 1.61 * M, sendo K a
distância em quilômetros e M em milhas.
"""
m = float(input('Digite um valor em milhas: '))
k = 1.61 * m
print(f'Valor em quilômetros: {k}')
