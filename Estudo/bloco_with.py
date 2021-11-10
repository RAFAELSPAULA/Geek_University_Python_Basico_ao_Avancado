"""
O Bloco with

Passos para se trabalhar com arquivos.

1 - Abrimos o arquivo
2 - Manipulando o arquivo
3 - Fechamos o arquivo

O block with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with

arquivos = open('texto.txt')
"""

# o block with - Forma Pythônica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())

# print(arquivo.read())

print(arquivo.closed)
