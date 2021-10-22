"""
Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formados pelos
dígitos invertidos do número lido. Exemplo:

Número lido = 123
Número gerado = 321
"""
nl = int(input('Digite um número: '))
invertido = str(nl)[::-1]
print(f'Número Invertido: {invertido}')
