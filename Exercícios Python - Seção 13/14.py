data_atual = '12 12 2020'.split(' ')
ano_atual = int(data_atual[len(data_atual) - 1])
mes_atual = int(data_atual[len(data_atual) - 2])
dia_atual = int(data_atual[len(data_atual) - 3])
nome_idade = dict()
with open('nascimentos.txt', 'r', encoding='UTF-8') as f1:
    linhas = f1.readlines()
    for linha in linhas:
        palavras = linha.strip().split(' ')
        ano = int(palavras[len(palavras) - 1])
        mes = int(palavras[len(palavras) - 2])
        dia = int(palavras[len(palavras) - 3])
        idade = ano_atual - ano
        if mes_atual < mes:
            idade -= 1
        elif mes_atual == mes:
            if dia_atual < dia:
                idade -= 1
        nome_idade[' '.join(palavras[0: len(palavras) - 3])] = idade

with open('idades.txt', 'w', encoding='UTF-8') as f2:
    for i in nome_idade:
        f2.write(i), f2.write(' '), f2.write(str(nome_idade[i])), f2.write('\n')

# Entrada de texto (nome = nascimentos.txt)

