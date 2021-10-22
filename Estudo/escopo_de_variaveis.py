"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado
    ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

numero = 42 # Exemplo Variável Global

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo
de dado dela.
Este tipo é inferido ao atribuímos  o valor à mesma.

if numero > 10:
    novo = numero +10 # A variável 'novo' está declarando localmente dentro do bloco do if. Portanto é local


"""