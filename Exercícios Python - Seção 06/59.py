hab = int(input('Digite quantos habitantes existem nessa cidade:'))
kwh = int(input('Digite o valor R$ do KWH dessa cidade:'))
print('\n')
print('-' * 30)
print(f'VALOR DO KWH DESSA CIDADE: {kwh} R$\n'
      f'QUANTIDADE DE HABITANTES DA CIDADE: {hab}\n')
print('-' * 30)
print('TABELA DE CÓDIGOS')
print('-' * 30)
print('1 - RESIDENCIAL\n'
      '2 - COMERCIAL\n'
      '3 - INDUSTRIAL\n')

cons = cont = maior = menor = cod1 = cod2 = cod3 = med = 0
while cont < hab:
    for y in range(1, hab + 1):
        cont += 1
        cons = int(input(f'Qual o consumo do mês em R$ do habitante {y}:'))
        cod = int(input(f'Qual o código do habitante {y}:'))

        med += cons

        if menor == 0:
            menor = cons
        if cons < menor:
            menor = cons
        if cons > maior:
            maior = cons

        if cod <= 0 or cod > 3:
            print('código inválido')
            break
        else:
            print('\n')
            if cod == 1:
                cod1 += cons
            elif cod == 2:
                cod2 += cons
            elif cod == 3:
                cod3 += cons
med = med / hab
print(f'O maior consumo de um habitante foi de: {int(maior / kwh)} Horas e {maior} R$')
print(f'O menor consumo de um habitante foi de: {int(menor / kwh)} Horas e {menor} R$')
print(f'A média de consumo dos habitantes foi de: {int(med / kwh)} Horas e {med} R$')
print(f'O total de consumo residencial foi de: {int(cod1 / kwh)} Horas e {cod1} R$')
print(f'O total de consumo comercial foi de: {int(cod2 / kwh)} Horas e {cod2} R$')
print(f'O total de consumo industrial foi de: {int(cod3 / kwh)} Horas e {cod3} R$')