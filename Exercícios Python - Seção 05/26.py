"""
Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em
Km/l e escreva uma mensagem de acordo  com a  tabela abaixo:

Menor que  8 - Venda o carro!
entre 8 e 14 - Econômico!
Maior que 14 - Super Econômico!
"""
km = float(input('Digite a distância: '))
litros = float(input('Digite gasolina consumida: '))
p = km/litros
print(p)

if p < 8:
    print('Venda o carro!')
elif (p > 8) and (p < 14):
    print('Econômico')
else:
    print('Super Econômico')

