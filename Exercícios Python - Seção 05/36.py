"""
Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor. Para calcular a
comissão, considere a tabela abaixo:

Maior ou igual a R$100.000,00 - R$ 700,00 + 16% das vendas
Menor que R$100.000,00 e maior ou igual a R$ 80.000,00 - R$ 650,00 + 14% das vendas
Menor que R$80.000,00 e maior ou igual a R$ 60.000,00 - R$ 600,00 + 14% das vendas
Menor que R$60.000,00 e maior ou igual a R$ 40.000,00 - R$ 550,00 + 14% das vendas
Menor que R$40.000,00 e maior ou igual a R$ 20.000,00 - R$ 500,00 + 14% das vendas
Menor que R$ 20.000,00 - R$ 400,00 + 14% das vendas
"""
v = float(input('Digite valor da venda: '))

if v < 20.000:
    vn = 400 + v * 0.14
    print(vn)
elif 20.000 <= v < 40.000:
    vn = 500 + v * 0.14
    print(vn)
elif 40.000 <= v < 60.000:
    vn = 550 + v * 0.14
    print(vn)
elif 60.000 <= v < 80.000:
    vn = 600 + v * 0.14
    print(vn)
elif 80.000 <= v < 100.000:
    vn = 650 + v * 0.14
    print(vn)
elif v >= 100.000:
    vn = 700 + v * 0.16
    print(vn)

