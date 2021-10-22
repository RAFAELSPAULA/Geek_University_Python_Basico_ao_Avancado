"""
Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo que funcionário tem uma
gratificação de 5% sobre salário base. Além disso, ele paga 7% de imposto sobre o salário base.
"""
s = float(input('Digite salário bruto: '))
ad = s * 0.05
ir = s * 0.07
sf = s + ad - ir
print(f'Salário líquido: {sf}')