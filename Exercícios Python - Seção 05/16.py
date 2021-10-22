"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este número.
Isto é, janeiro se 1, fevereiro se 2 e assim por diante.
"""
mesTotal = ['Janeiro',
            'Fevereiro',
            'Março',
            'Abril',
            'Maio',
            'Junho',
            'Julho',
            'Agosto',
            'Setembro',
            'Outubro',
            'Novembro',
            'Dezembro']

mes = int(input('Digite o Mês desejado \n'))

if (mes < 1) or (mes > 12):
    print('Mês inválido')
else:
    print(f'O Mês selecionado é: {mesTotal[mes - 1]}')
