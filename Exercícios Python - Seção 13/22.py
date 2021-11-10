arq_1 = input('Informe o nome do arquivo que queres abrir: ')
arq_2 = input('Informe o nome do arquivo de saida: ')
notas = []
lista = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'

with open(f'{arq_1}') as arq_a:
    cont_arq_a = list(arq_a)
    x = cont_arq_a[0].split(':')
    for y in x[1]:
        if y in lista:
            notas.append(int(y))
    notas.sort()

with open(f'{arq_2}', 'w') as arq_b:
    arq_b.write(f'{x[0]}: {notas[0]}, {notas[1]}, {notas[2]}')