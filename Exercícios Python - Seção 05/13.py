"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova têm peso 1 e a
terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para
aprovação deve ser igual ou superior a 60 pontos.
"""
n1 = float(input('Digite valor da primeira nota: '))
n2 = float(input('Digite valor da segunda nota: '))
n3 = float(input('Digite valor da terceira nota: '))

media = ((1 * n1) + (1 * n2) + (2 * n2))/(1 + 1 + 2)

if media >= 60:
    print(f'Media : {media}')
    print('Aprovado')
else:
    print(f'Media : {media}')
    print('Reprovado')
