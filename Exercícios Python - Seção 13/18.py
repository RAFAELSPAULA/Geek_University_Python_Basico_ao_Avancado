with open('arq.txt', 'r', encoding='UTF-8') as f1:
    linhas = f1.readlines()
    print(linhas)
    total = 0
    for linha in linhas:
        palavras = linha.strip().split(' ')
        preco = float(palavras[-1])
        total += preco
print(f'O total da compra é {total}')