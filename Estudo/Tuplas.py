"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda a operação em uma tupla gera
uma nova tupla.
------------------------------------------------------------------------------------------------------------------------
- Cuidado 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)

tupla2 = 1, 2, 3, 4, 5 ,6 - Também e uma tupla

- Cuidado 2: Tuplas com um elemento

tupla3 = (4) - Para Python isso e um int

tupla4 = (4,) - Isso e uma tupla!

- Conclusão: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso dos parênteses.

(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla
------------------------------------------------------------------------------------------------------------------------
- Podemos gerar uma tupla dinamicamente com range(inicio,fim, passo)

Exemplo 1:

tupla = tuple(range(11))
------------------------------------------------------------------------------------------------------------------------
- Desempacotamento de tupla

Exemplo 2:

tupla = ('Geek  University', 'Programação em Python: Essencial')

escola, curso = tupla

OBS: Gera erro (ValueError) se colocarmos um número diferentes de elementos para desempacotar.
------------------------------------------------------------------------------------------------------------------------
- Métodos para adição e remoção de elementos para tuplas não existem, dado o fato das tuplas serem imutáveis.
------------------------------------------------------------------------------------------------------------------------
- Soma*, valor Máximo*, Valor Mínimo* e Tamanho
* Se os valores forem todos inteiros ou reais

Exemplo 3:

tupla = (1, 2, 3, 4)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
------------------------------------------------------------------------------------------------------------------------
- Concatenação de tuplas

Exemplo 4:

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print(tupla1 + tupla2) - Tuplas são imutáveis
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

tupla1 = tupla1 + tupla2 - Tuplas são imutáveis, mas podemos sobrescrever seus valores
------------------------------------------------------------------------------------------------------------------------
- Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)

print(3 in tupla)
------------------------------------------------------------------------------------------------------------------------
- Iterando sobre uma tupla

tupla = (1, 2, 3)

for i in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)
------------------------------------------------------------------------------------------------------------------------
- Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))
------------------------------------------------------------------------------------------------------------------------
- Dicas na utilização de tuplas

- Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção.

Exemplo:

meses = ('Janeiro', 'Fevereiro', ...)
------------------------------------------------------------------------------------------------------------------------
- O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])
------------------------------------------------------------------------------------------------------------------------
- Iterar com while

i = 0

while i < len(meses):
    print(meses[i])
    i += 1
------------------------------------------------------------------------------------------------------------------------
- Verificamos em qual índice um elemento está na tupla

print(meses.index('Junho'))

OBS: Caso o elemento não exista, será dado erro ValueError.
------------------------------------------------------------------------------------------------------------------------
- Slicing

- Tupla[ínicio:fim:passo]

print(meses[5:9])
------------------------------------------------------------------------------------------------------------------------
- Por quê utilizar tuplas?

- Tuplas são mais rápidas do que listas.
- Tuplas deixam seu código mais seguro*
* Isso porque trabalhar com elementos imutáveis traz segurança para o código.
------------------------------------------------------------------------------------------------------------------------
- Copiando uma tupla para outra.

tupla = (1, 2, 3)

nova = tupla - Na tupla não temos o problema de Shallow Copy
"""