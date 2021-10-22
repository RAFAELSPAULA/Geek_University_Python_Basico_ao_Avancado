"""
Faça um programa que leia o valor da hora trabalhada (em reais) e número de horas trabalhadas no mês. Imprima o valor a
ser pago ao funcionário, adicionando 10% sobre valor calculado.
"""
v = float(input('Digite valor por hora: '))
q = float(input('Digite tempo trabalhado: '))
s = v * q
add = s * 0.10
sn = s + add
print(f'Salário devido é de: {sn}')