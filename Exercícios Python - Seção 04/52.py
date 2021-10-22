"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um deu
para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima
quanto cada um ganharia do prêmio .
"""
valorP = float(input('Digite Valor do Prêmio: '))

n1 = float(input('Jogo do primeiro participante: '))
n2 = float(input('Jogo do segundo participante: '))
n3 = float(input('Jogo do terceiro participante: '))

total = n1 + n2 + n3

p1 = n1/total
p2 = n2/total
p3 = n3/total

g1 = p1 * valorP
g2 = p2 * valorP
g3 = p3 * valorP

print(f'Ganho do Primeiro Participante: {g1:.2f}'
      f'\nGanho do Segundo Participante: {g2:.2f}'
      f'\nGanho do Terceiro Participante: {g3:.2f}')
