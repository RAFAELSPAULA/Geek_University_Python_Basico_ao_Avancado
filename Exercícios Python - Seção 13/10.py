entrada = input("Digite o nome do arquivo a ser aberto: ")
saida = input("Digite o nome do arquivo a ser gerado: ")

with open(f"{entrada}") as arq1, open(f"{saida}", "w") as arq2:
    # Copiando o texto
    linhas = arq1.readlines()

    # criando um dicionario vazio para receber vada cidade e habitantes
    res_linha = {}

    # Um for em cada linha do texto
    for linha in linhas:
        # Usando o split(' ') na linha separamos as todos os espaços vazios,
        split_linha = linha.split(' ')

        # Usando o filter() com a função None eliminamos os elementos vazios sobrando assim um alista com duas strings
        filtro_linha = list(filter(None, split_linha))

        # Como temos uma lista com duas str, adicionamos ao dicionario a chave = indice[0] e o valor = indice[1]
        res_linha[filtro_linha[0]] = int(filtro_linha[1])

    # Pegaremos a chave que contem o maior valor
    maior_cidade = max(res_linha, key=res_linha.get)

    # Agora que temos a chave que tem o maior valor podemos escrever no novo aquivo a cidade que tem a maior população
    arq2.write(f"{maior_cidade}: {res_linha[maior_cidade]}")