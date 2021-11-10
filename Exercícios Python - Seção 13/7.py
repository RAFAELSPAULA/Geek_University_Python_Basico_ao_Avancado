import fileinput

with open('arq.txt', 'r') as arquivo_existente, open('arqN.txt', 'w') as novo_arquivo:
    for linha in arquivo_existente.readlines():
        novo_arquivo.write(linha)


with fileinput.FileInput('arqN.txt', inplace=True) as file:
    for line in file:
        print(line.replace('a', '*'), end='')
with fileinput.FileInput('arqN.txt', inplace=True) as file:
    for line in file:
        print(line.replace('e', '*'), end='')
with fileinput.FileInput('arqN.txt', inplace=True) as file:
    for line in file:
        print(line.replace('i', '*'), end='')
with fileinput.FileInput('arqN.txt', inplace=True) as file:
    for line in file:
        print(line.replace('o', '*'), end='')
with fileinput.FileInput('arqN.txt', inplace=True) as file:
    for line in file:
        print(line.replace('u', '*'), end='')
