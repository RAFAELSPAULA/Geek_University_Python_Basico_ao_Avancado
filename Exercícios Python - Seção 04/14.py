"""
Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: R = G * pi/180, sendo G o ângulo
em graus e R em radianos e pi = 3.14.
"""
g = float(input('Digite um valor em ângulo em graus: '))
r = g * 3.14/180
print(f'Valor em radianos: {r}')
