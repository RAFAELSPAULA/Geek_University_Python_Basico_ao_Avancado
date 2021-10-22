"""
Um Produto vai sofrer aumento de acordo com a tabela abaixo: Leia o preço antigo, calcule e escreva o preço novo, e
escreva uma mensagem em função do preço novo (de acordo com a segunda tabela)

até R$ 50 - Aumento 5%
Entre R$ 50 e R$ 100 - Aumento 10%
Acima de R$ 100 - Aumento 15%

Preço novo até 80 - Barato
Entre 80 e 120 (Inclusive) - Normal
Entre 120 e 200 (inclusive) - Caro
Acima de 200 - Muito Caro
"""
p = float(input('Digite valor: '))

if p <= 50:
    pn = p + p * 0.05
elif (p > 50) and (p < 100):
    pn = p + p * 0.10
elif p > 100:
    pn = p + p * 0.15

if pn < 80:
    print(f'Valor Novo: {pn} - Barato')
elif (pn > 80) and (pn <= 120):
    print(f'Valor Novo: {pn} - Normal')
elif (pn > 121) and (pn <= 200):
    print(f'Valor Novo: {pn} - Caro')
elif pn > 201:
    print(f'Valor Novo: {pn} - Muito Caro')
