"""
Loop For

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.
------------------------------------------------------------------------------------------------------------------------
C ou Java

for(int i = 0; i < limitador: i++){
    //execução do loop
}
------------------------------------------------------------------------------------------------------------------------
Python

For item in iterável:
    //execução do loop

Utilizamos loops para iterar sobre sequência ou sobre valores iteráveis

Exemplo de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    números = range(1, 10)
------------------------------------------------------------------------------------------------------------------------
# Exemplo de for 1 (Iterando em uma string)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #Temos que transformar em uma lista

for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)
OBS: O Valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 -  Não

for numero in range(1, 10):
    print(numero)
------------------------------------------------------------------------------------------------------------------------
Enumerate:

((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'u')....)

for indice, letras in enumerate(nome)
    print(nome[indice])

for indice, letra in enumerate(nome)
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizamos um underline(_)
------------------------------------------------------------------------------------------------------------------------
for valor in enumerate(nome): # para trazer índice com a letra
    print(valor)

------------------------------------------------------------------------------------------------------------------------
OBS: para ver total cheio devemos colocar +1 no final do range.

qtd = int(input('Quantas vezes esse loop deve rodar? '))

for n in range(1, qtd): #vai trazer -1 do que usuário digitou
    print(f'Imprimindo {n}')

for n in range(1, qtd+1):
    num = int(input(f'informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'Soma é {soma}')
------------------------------------------------------------------------------------------------------------------------
OBS: Pula linha já vem por default no Python, para não ocorrer isso devemos colocar end='' no final do print

for letra in nome:
    print(letra, end='')
------------------------------------------------------------------------------------------------------------------------
OBS: CTRL + Clique em cima do print você consegue acessar help
------------------------------------------------------------------------------------------------------------------------
Terminal

nome = 'Geek'
nome + 'University'
'Geek University'
Isso e chamado de concatenação de string
nome * 3 (vai repetir o nome quantas vezes desejar)
------------------------------------------------------------------------------------------------------------------------
Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode

#Original: U+1F60D
#Modificado: U0001F60D -> Copio a letra U e depois substitui + por 3 zero e copia resto do código

for num in range(1, 11):
    print('\U0001F60D' * num)

\ e um caractere de escape
------------------------------------------------------------------------------------------------------------------------
"""

