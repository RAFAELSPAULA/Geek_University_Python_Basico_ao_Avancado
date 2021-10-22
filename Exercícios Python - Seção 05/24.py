"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto sobre
o produto (MG 7%; SP 12%; RJ 15%; MS 8%;). Faça um programa em que o usuário entre com o valor e o estado destino do
produto e o programa retorne o preço final do produto
"""
produto = float(input('Insira o valor do produto: '))
estado = str(input('Insira o Estado: '))

if estado == 'MG':
    produtoMG = produto + (produto * 0.07)
    print(f'Valor do Produto Final: {produtoMG}')
elif estado == 'SP':
    produtoSP = produto + (produto * 0.12)
    print(f'Valor do Produto Final: {produtoSP}')
elif estado == 'RJ':
    produtoRJ = produto + (produto * 0.15)
    print(f'Valor do Produto Final: {produtoRJ}')
elif estado == 'MS':
    produtoMS = produto + (produto * 0.08)
    print(f'Valor do Produto Final: {produtoMS}')
else:
    print('Estado Inválido')
