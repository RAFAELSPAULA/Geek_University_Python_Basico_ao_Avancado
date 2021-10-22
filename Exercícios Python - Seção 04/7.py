"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A fórmula de conversão é:
C = 5.0 * (F - 32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
"""
f = float(input('Temperatura em graus Fahrenheit: '))
c = 5.0 * (f - 32.0)/9.0
print(f'temperatura em graus Celsius: {c}')
