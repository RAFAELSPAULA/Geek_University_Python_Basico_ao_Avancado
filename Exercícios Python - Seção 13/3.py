from collections import Counter

vogais = ['A', 'Á', 'À', 'Ã', 'Â', 'a', 'á', 'à', 'ã', 'â',
          'E', 'É', 'Ê', 'e', 'é', 'ê', 'I', 'Í', 'i', 'í',
          'O', 'Ó', 'Ô', 'Õ', 'o', 'ó', 'õ', 'ô', 'U', 'Ú', 'u', 'ú']

with open('arq.txt', 'r', encoding='utf-8') as arquivo:
    letras = [char for char in arquivo.read() if char in vogais]
    diciasc = Counter(letras)
    print(diciasc)
    total = sum(diciasc.values())
    print(f'Existem {total} vogais')

# ----------------------------------------------------------------------------------------------------------------------
# with open('arq.txt', 'r', encoding='utf-8') as arquivo:
#     vogais = filter(lambda x: x in 'aeiouAEIOU', arquivo.read())
#     print(len(list(vogais)))
