matriz = []
dados = ['matrícula', 'média das provas', 'média dos trabalhos']
maiornota, matriculamaiornota = 0, 0

for x in range(5):
    matriz.append([])
    for info in range(3):
        matriz[x].append(str(input(f'Digite a {dados[info]} do {x + 1}º aluno: ')))
    matriz[x].append((float(matriz[x][1]) + float(matriz[x][2])))

print('\n')
for m in matriz:
    print(m)
    if m[3] > maiornota:
        maiornota = m[3]
        matriculamaiornota = m[0]
print('\n')

print(f'Aluno com maior nota é: {matriculamaiornota}, com a nota {maiornota}\n')
print('MÉDIA FINAL')
for i in matriz:
    print(f'Aluno: {i[0]} / Média: {i[3] / 2:.1f}')
