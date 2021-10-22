"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este
número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.
"""
diaSemana = ['domingo',
             'segunda',
             'terça',
             'quarta',
             'quinta',
             'sexta',
             'sábado']

dia = int(input('Digite o dia da semana \n'))

if (dia < 1) or (dia > 7):
    print('Dia inválido')
else:
    print(f'O Dia selecionado é: {diaSemana[dia - 1]}')
