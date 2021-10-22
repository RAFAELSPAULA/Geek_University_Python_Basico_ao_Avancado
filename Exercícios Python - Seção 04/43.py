"""
Escreva um programa de ajuda para vendedores. A partir de um valor total liso, mostre:

* O total a pagar com desconto de 10%;
* O valor de cada parcela, no parcelamento de 3x sem juros;
* A comissão do vendedor, no caso de venda ser a vista (5% sobre o valor com desconto)
* A comissão do vendedor, no caso  da venda ser parcelado (5% sobre o valor total)
"""
vt = float(input('Valor total do produto: '))
desconto = vt - (vt * 0.10)
par = desconto / 3
cv = desconto * 0.5
cp = vt * 0.5
print(f'Valor total {vt}'
      f'\nValor com Desconto: {desconto}'
      f'\nValor da parcela em 3x: {par}'
      f'\nComissão a vista : {cv}'
      f'\nComissão a prazo: {cp}')