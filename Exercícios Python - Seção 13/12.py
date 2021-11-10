import string

nome_arquivo = input('Digite o nome do arquivo. Formato nome.extensão: ')
extensao = '.txt'
dicionario = dict()

with open(f'{nome_arquivo}{extensao}', 'r', encoding="UTF-8") as arquivo:
    caracter = str(arquivo.read())
    arquivo.seek(0)
    palavra = arquivo.read().split()
    arquivo.seek(0)
    print(f'A quantidade de caracteres: {len(caracter)}')
    print(f'A quantidade de linhas: {len(arquivo.readlines())}')
    print(f'A quantidade de palavras: {len(palavra)}')
    print(f'A quantidade de cada letra do alfabeto no texto (caracteres acentuados serão ignorados): ')
    [dicionario.update({letra: caracter.lower().count(letra)}) for letra in caracter.lower() if
     letra in string.ascii_letters]
    for key, value in sorted(dicionario.items()):
        print(f'{key} - {value}')