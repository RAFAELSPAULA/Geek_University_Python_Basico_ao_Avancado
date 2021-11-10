with open('arq.txt', 'r') as arquivo_existente, open('arqN1.txt', 'w') as novo_arquivo:
    for linha in arquivo_existente.readlines():
        novo_arquivo.write(linha.upper())

