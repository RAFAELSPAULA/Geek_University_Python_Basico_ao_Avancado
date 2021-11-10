with open("arquivo.txt", mode='r', encoding='UTF-8') as arq:
    linhas = arq.readlines()
    linhas.reverse()
    print(linhas)

with open("arquivo_reverso.txt", mode='w', encoding='UTF-8') as arq2:
    for i in linhas:
        uni = ''.join(list(reversed(i)))
        arq2.write(uni)