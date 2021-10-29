tam = 10  # Quantidade de questões
ta = 3  # Total de Alunos

gabarito = []
alunos = []
nota = []
totalnota = 0
respostas = []

for i in range(tam):
    resgab = input(f'Resposta Gabarito Questão {i + 1}: ').lower()
    while resgab != 'a' and resgab != 'b' and resgab != 'c' and resgab != 'd' and resgab != 'e':
        resgab = input(f'\nResposta inválida!\nResposta da questão {i + 1}: ')
    gabarito.append(resgab)

aux = 0
while aux < ta:
    try:
        alunos.append(int(input(f'\nNúmero Matrícula Aluno {aux + 1}: ').lower()))
    except ValueError:
        print('Erro: A matrícula deve ser um número inteiro.')
    else:
        totalnota = 0
        for j in range(tam):
            res = input(f'Resposta Aluno {aux + 1} Questão {j + 1}: ').lower()
            while res != 'a' and res != 'b' and res != 'c' and res != 'd' and res != 'e':
                res = input(f'\nResposta inválida!\nResposta da questão {j + 1}: ')
            respostas.append(res)
            if gabarito[j] == res:
                totalnota += 1
        nota.append(totalnota)
        aux += 1

inicio = 0
fim = tam
aprovados = 0

for i in range(ta):
    if nota[i] >= 7:
        aprovados += 1
    print(f'Aluno: {alunos[i]} Respostas: {respostas[inicio:fim]} Nota: {nota[i]}')
    inicio += tam
    fim += tam
print(f'Porcentagem de Aprovados: {aprovados * 100 / ta:.2f}%')