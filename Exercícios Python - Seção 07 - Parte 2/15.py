from random import choice

matriz = [[0, 0, 0, 0, 0] for i in range(10)]
gabarito = ['a', 'b', 'c', 'd', 'd', 'a', 'a', 'b', 'c', 'c']
questoes = ['a', 'b', 'c', 'd']
nota_aluno = [0, 0, 0, 0, 0]

for i in range(10):
    for j in range(5):
        matriz[i][j] = input(f'Digite a resposta [{i},{j}]:\n')

for i in range(10):
    for j in range(5):
        if matriz[i][j] == gabarito[i]:
            nota_aluno[j] = nota_aluno[j] + 1

for i in range(10):
    for j in range(5):
        print(f'[{matriz[i][j]}]', end=' ')
    print()

print('-=' * 30)
print(nota_aluno)