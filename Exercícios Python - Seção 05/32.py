"""
Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade. O programa
deve calcular o valor a ser pago por aquele lanche. Considere que a cada execução somente será calculado um pedido.
O cardápio da lanchonete segue o padrão abaixo:

Cachorro Quente - 100  - 1.20
Bauru Simples - 101 - 1.30
Bauru com Ovo - 102 - 1.50
Hambúrguer - 103 - 1.20
Cheeseburger - 104 - 1.70
Suco - 105 - 2.20
Refrigerante - 106 - 1.00
"""
c = int(input('Digite o Código: '))


if c == 100:
    q = int(input('Digite Quantidade: '))
    vp = 1.20 * q
    print(f'Valor a pagar: {vp}')
elif c == 101:
    q = int(input('Digite Quantidade: '))
    vp = 1.30 * q
    print(f'Valor a pagar: {vp}')
elif c == 102:
    q = int(input('Digite Quantidade: '))
    vp = 1.50 * q
    print(f'Valor a pagar: {vp}')
elif c == 103:
    q = int(input('Digite Quantidade: '))
    vp = 1.20 * q
    print(f'Valor a pagar: {vp}')
elif c == 104:
    q = int(input('Digite Quantidade: '))
    vp = 1.70 * q
    print(f'Valor a pagar: {vp}')
elif c == 105:
    q = int(input('Digite Quantidade: '))
    vp = 2.20 * q
    print(f'Valor a pagar: {vp}')
elif c == 106:
    q = int(input('Digite Quantidade: '))
    vp = 1.00 * q
    print(f'Valor a pagar: {vp}')
else:
    print('Produto Inválido')
