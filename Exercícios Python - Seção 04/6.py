"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é:
F = C*(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""
c = float(input('Temperatura em Celsius: '))
f = c*(9.0/5.0)+32.0
print(f'Valor de Fahrenheit: {f}')