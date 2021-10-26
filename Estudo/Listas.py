"""
Listas

Listas em Python funcional como vetores/matrizes (arrays) em outra linguagens, com a diferença de serem dinâmicos e
também de podermos colocar qualquer tipo de dados.
------------------------------------------------------------------------------------------------------------------------
Linguagens C/Java: Arrays
    - Possuem tamanho e tipo  de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será sempre do tipo
    inteiro e poderá ter sempre no máximo 5 valores.
------------------------------------------------------------------------------------------------------------------------
Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos enquanto
tiver memoria;
- Qualquer tipo de dados: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representada por colchetes: []
------------------------------------------------------------------------------------------------------------------------
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')
------------------------------------------------------------------------------------------------------------------------
- Podemos facilmente checar se determinado valor está contido na lista

Exemplo 1:

if 8 in lista4:
    print('Encontrei o número 8')
else:
    print('Não encontrei o número 8')
------------------------------------------------------------------------------------------------------------------------
Exemplo 2:

num = 18
if num in lista4:
    print('Encontrei o número {num}')
else:
    print('Não encontrei o número {num}')
------------------------------------------------------------------------------------------------------------------------
Exemplo 3:

if 'e' in lista5:
    print('Encontrei a letra e')
else:
    print('Não encontrei a letra e')
------------------------------------------------------------------------------------------------------------------------
- Podemos facilmente ordenar uma lista

Exemplo 4:

lista1.sort()
print(lista1)
------------------------------------------------------------------------------------------------------------------------
- Podemos facilmente contar o número de ocorrência de um valor em uma lista

Exemplo 5:

print(lista1.count(1)
print(lista5.count('e'))
------------------------------------------------------------------------------------------------------------------------
- Adicionando elemento em listas
- Para adicionar elemento em listas, utilizamos a função append
OBS: Com append, nós só conseguimos adicionar um elemento por vez

Exemplo 6:

print(lista1)
lista1.append(42)
print(lista1)

lista1.append(12, 34, 58) # Erro
lista1.append([8, 3, 1]) # Coloca a lista como elemento único (sub-lista)

- Forma correta de adicionar mais elementos e com extend

lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como um valor adicional á lista.
print(lista1)

OBS: Com extend, não aceita valor único.
------------------------------------------------------------------------------------------------------------------------
- Podemos inserir um novo elemento na lista informando a posição do índice.
OBS: Isso não substitui valor inicial. O mesmo será deslocado para direita da lista.

Exemplo 7:

lista1.insert(2, 'Novo Valor')
print(lista1)
------------------------------------------------------------------------------------------------------------------------
- Podemos facilmente juntar duas listas

Exemplo 8:

lista6 = lista1 + lista2
lista1 = lista1 + lista2 # Outra forma de fazer
lista.extend(lista2) # outra forma de fazer
print(lista6)
------------------------------------------------------------------------------------------------------------------------
- Podemos facilmente inverter uma lista

Exemplo 9:

lista1.reverse()
print(lista1)
print(lista1[::-1]) # Outra forma de fazer (Slice)
------------------------------------------------------------------------------------------------------------------------
- Copiar uma lista

Exemplo 10:

lista6 = lista2.copy()
print(lista6)
------------------------------------------------------------------------------------------------------------------------
- Para saber quantos elemento tem na lista

Exemplo 11:

print(len(lista2))
------------------------------------------------------------------------------------------------------------------------
- Podemos remover facilmente o último elemento de uma lista
OBS: o pop não somente remove o último elemento mas também o retorna

Exemplo 12:

lista5.pop()
print(lista5)

- Podemos remover um elemento pelo índice
OBS: Os elemento á direita deste índice serão deslocados para a esquerda.
OBS: Se não houver elemento no índice informado, teremos o erro IndexError.

Exemplo 13:

lista5.pop(2)
print(lista5)
------------------------------------------------------------------------------------------------------------------------
- Podemos remover todos os elementos (zerar a lista)

Exemplo 14:

lista5.clear()
print(lista5)
------------------------------------------------------------------------------------------------------------------------
- Podemos facilmente repetir elemento em uma lista

Exemplo 15:

nova = [1, 2, 3]
nova = nova * 3
print(nova)
------------------------------------------------------------------------------------------------------------------------
- Podemos facilmente converter uma string para uma lista
OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

Exemplo 16:

curso = 'Programação em Python: Essencial'
curso = curso.split()
print(curso)

Exemplo 17:

curso = 'Programação, em, Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)
------------------------------------------------------------------------------------------------------------------------
- Convertendo uma lista em uma string

Exemplo 18:

lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string

curso = ' '.join(lista6)
print(curso)

Exemplo 19:

# Abaixo estamos falando: Pega a lista6, coloca cifrão entre cada elemento e transforma em uma string

curso = '$'.join(lista6)
print(curso)
------------------------------------------------------------------------------------------------------------------------
- Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados.

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45648964564]
------------------------------------------------------------------------------------------------------------------------
- Iterando sobre listas
- Utilizando for

Exemplo 20:

for elemento in lista1:
    print(elemento)

Exemplo 21:

soma = 0
for elemento in lista1:
    print(elemento)
    soma += elemento
print(soma)

Exemplo 22:

soma = ''
for elemento in lista2:
    print(elemento)
    soma += elemento
print(soma)
------------------------------------------------------------------------------------------------------------------------
- Utilizando While

Exemplo 23:

carrinho = []
produto = ''

while produto !+ 'sair':
    print('Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
------------------------------------------------------------------------------------------------------------------------
- Utilizando variáveis em listas

Exemplo 24:

numero = [1, 2, 3, 4, 5]
print(numero)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numero = [num1, num2, num3, num4, num5]
print(numero)
------------------------------------------------------------------------------------------------------------------------
- Fazemos acesso aos elementos de forma indexada

Exemplo 25:

#           0          1        2       3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

Exemplo 26:

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense na lista como um círculo, onde o final de um elemento está ligado ao
inicio da lista

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4] # verde
print(cores[-5] # Erro, pois não existe índice 5
------------------------------------------------------------------------------------------------------------------------
Exemplo 27:

#           0          1        2       3
cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores);
    print(cores[indice])
    indice += 1
------------------------------------------------------------------------------------------------------------------------
- Gerar índice em um for

Exemplo 28:

for indice, cor in enumerate(cores):
    print(indice, cor)
------------------------------------------------------------------------------------------------------------------------
- Lista aceita valores repetidos

Exemplo 29:

lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)
------------------------------------------------------------------------------------------------------------------------
- Outros métodos não tão importantes mas também úteis
- Encontrar o índice de um elemento na lista
OBS: caso não tenha este elemento na lista, será apresentado erro ValueError

exemplo 30:

numeros = [5, 6, 7, 8, 9, 10]

- Em qual índice da lista está o valor 6?
print(numeros.index(6))

- Retorna o índice do primeiro elemento encontrado
print(numeros.index(5))

- Podemos fazer busca dentro  de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1)) - Buscando a partir do índice 1
print(numeros.index(5, 2)) - Buscando a partir do índice 2
print(numeros.index(5, 3)) - Buscando a partir do índice 3
print(numeros.index(5, 4)) - Buscando a partir do índice 4
OBS: caso não tenha este elemento na lista, será apresentado erro ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numero.index(8, 3, 6)) - Busca o índice do valor 8, entre índices 3 a 6
------------------------------------------------------------------------------------------------------------------------
- Revisão Slice
- lista[inicio:fim:passo]
- range(inicio:fim:passo)
-Trabalhando com slice de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:]) - Iniciando no índice 1 e pegando todos os elementos restantes

- Trabalhando com slice de lista com o parâmetro 'fim':

print(lista([:2]) - Começa em 0, pega até o índice 2 - 1

print(lista[1:3]) - Começa em 1, pega até o índice 3 - 1

- Trabalhando com slice de lista com o parâmetro 'passo'

print(lista[1::2]) - Começa em 1, vai até final, de 2 em 2

print(lista[::2]) - Começa em 0, vai até final, de 2 em 2
------------------------------------------------------------------------------------------------------------------------
- Invertendo Valores em uma lista

nomes = ['geek', 'University']

nome [0], nomes[1] =  nomes[1], nomes[0]
nomes.reverse() - mesma coisa
------------------------------------------------------------------------------------------------------------------------
- Soma*, Valor máximo*, Valor mínimo*, tamanho

- * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) - Soma
print(max(lista)) - máximo valor
print(min(lista)) - mínimo valor
print(len(lista)) - tamanho da lista
------------------------------------------------------------------------------------------------------------------------
- Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))
------------------------------------------------------------------------------------------------------------------------
- Desempacotamento de lista

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

- E chamado de desempacotamento de lista

OBS: se tivermos um número diferente de elementos na lista ou variáveis para receber os dados, teremos ValueError
------------------------------------------------------------------------------------------------------------------------
- Copiando uma lista para outra (Shallow Copy e Deep Copy)

Forma 1:

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

- Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas ficaram totalmente
independente, ou seja, modificando uma lista, não afeta a outra. Isso em Python é chamado de Deep copy ou
(Cópia Profunda).

- Forma 2: Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista  - Cópia

print(nova)

nova. append(4)

print(lista)
print(nova)

- Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas após realizar
modificação em uma das listas, essa modificação se refletiu em ambas as listas. Isso em Python é chamado de Shallow Copy


"""
