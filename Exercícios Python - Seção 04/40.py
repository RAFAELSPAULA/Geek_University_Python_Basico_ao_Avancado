"""
Uma empresa contrata um encanador a R$ 30.00 por dia. Faça um programa que solicite o número de dias trabalhados pelo
encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para IR.
"""
v = 30.00
d = float(input('Dias trabalhados: '))
s = v * d
ir = s * 0.08
salario = s - ir
print(f'Salário Final: {salario}')
