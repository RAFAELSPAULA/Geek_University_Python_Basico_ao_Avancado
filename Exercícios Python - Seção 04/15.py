"""
Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão é: G = R * 180/pi, sendo G o ângulo
em graus e r em radianos e pi = 3.14;
"""
r = float(input('Digite um valor em radianos: '))
g = r * 180/3.14
print(f'Valor ângulo em graus: {g}')
