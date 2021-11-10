from collections import Counter

alfa = ['A', 'Á', 'À', 'Ã', 'Â', 'a', 'á', 'à', 'ã', 'â',
          'E', 'É', 'Ê', 'e', 'é', 'ê', 'I', 'Í', 'i', 'í',
          'O', 'Ó', 'Ô', 'Õ', 'o', 'ó', 'õ', 'ô', 'U', 'Ú', 'u', 'ú',
        'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s',
        't','v','w','x','y','z']

with open('arq.txt', 'r', encoding='utf-8') as arquivo:
    letras = [char for char in arquivo.read() if char in alfa]
    diciasc = Counter(letras)
    print(diciasc)
