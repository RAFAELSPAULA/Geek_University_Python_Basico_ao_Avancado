"""
Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem como o preço do metro de tela p.
Imprima o custo para cercar este mesmo terreno com tela.
"""
c = float(input('Valor do Comprimento: '))
la = float(input('Valor da Largura: '))
t = c * la
p = float(input('Valor da Tela: '))
custo = p * t
print(f'Custo para cercar o terreno: {custo}')
