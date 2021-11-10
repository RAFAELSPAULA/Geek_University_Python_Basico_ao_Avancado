while True:
    try:
        num_alunos = int(input('Informe o número de alunos                                : '))
        break
    except ValueError:
        print('Valor invalidor!')

nomes = []
notas = []
x = 1

while x < num_alunos + 1:
    nome = input(f'Informe o nome do {x}° aluno                                : ')
    if len(nome) > 40:
        print('Nome não pode ter mais que 40 caracteres!')
    else:
        y = 40 - len(nome)
        nome += " " * y
        nomes.append(nome)
        x += 1
        while True:
            try:
                nota = float(input(f'Informe a nota de {nome}: '))
            except ValueError:
                print('Valor invalido')
            else:
                notas.append(nota)
                break

with open('arq_exe20_saida.txt', 'w') as arq:
    for n in range(len(nomes)):
        arq.write(f'{nomes[n]}: {notas[n]}')
        arq.write('\n')
