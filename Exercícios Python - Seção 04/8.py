"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula de conversão é: C = K - 273,15
sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""

k = float(input('Temperatura em Kelvin: '))
c = k - 273.15
print(f'Temperatura em Celsius: {c}')
