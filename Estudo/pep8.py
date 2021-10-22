"""
PEP8 - Python enchant proposal

São propostas de melhorias para a liguagem python

The zen of Python

import this

A ideia da PEP8 e que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel case para nomes de classes;

Sempre inicial maiúscula e se for nome composto utilizar mesma regra.

class Calculadora:
    pass

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;


def soma_dois():
    pass

[3] - Utilize 4 espaços para identação! (Não use TAB)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
-Separar Funções e Definições de classe com duas linhas em branco;
-Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports

-Imports devem ser sempre feitos em linhas separadas;

# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo  pacote, recomenda-se fazer:

from types import(
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
# antes de constantes ou variáveis globais.

# Não Faça:

funcao( algo[ 1 ], { outro: 2 })

# Faça:

funcao(algo[1], {outro: 2})

# Não Faça:

algo (1)

# Faça:

algo(1)

# Não faça:

dict ['chave '] = list [indice]

# Faça:

dict['chave'] = lista[indice]

# Não Faça:

x   =  1
y   =  1

#Faça:

x = 1
y = 1

[7] - Termine sempre uma instrução com uma nova linha
"""




