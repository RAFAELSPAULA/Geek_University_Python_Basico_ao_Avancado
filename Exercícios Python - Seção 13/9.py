with open('arq.txt', 'r') as arquivo_existente, open('arqN.txt', 'r') as arquivo_existente1, open('arqN2.txt', 'a') as novo_arquivo:
    for linha in arquivo_existente.readlines():
        novo_arquivo.write(linha)
    for linha in arquivo_existente1.readlines():
        novo_arquivo.write(linha)
