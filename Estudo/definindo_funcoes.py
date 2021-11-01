"""
Definindo Funções

- Funções são pequenos trechos de código que realizam tarefas específicas:
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimento similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela; é bom fazer uma verificação para que a função
seja simplificada.

Já utilizamos várias funções desde que iniciamos este curso:

- print()
- len()
- max ()
- min ()
- count()
- e muitas outras;

"""

# Exemplo de utilização de funções:

cores = ['Verde', 'Amarelo', 'Azul', 'Branco']

# Utilizamos a função integrada (Built-on) do Python print()

# print(cores)

curso = 'Programação em Python: Essencial'

# print(curso)

cores.append('Roxo')

# print(cores)

# curso.append('Mais dados...') # AtributeError
# print(curso)

cores.clear()
# print(cores)

# print(help(print))

# Dry - Don't Repeat Yourself - Não repita você mesmo / Não repita o código.

# Mas então, como definir funções?

"""
Em Python, a forma geral de definir uma função é: 

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> SEMPRE -> SEMPRE, com letra minúscula, e se for composto, separado por underline (Snake case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def', informando ao Python que estamos definindo
uma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é utilizado em Python para definir 
blocos.
"""


# Definindo a primeira função

def diz_oi():
    print('oi!')


"""
OBS:

1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só  executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;
"""

# Utilizando funções

# Chamada de execução
# diz_oi()

"""
Atenção:

Nunca esqueça de utilizar o parênteses ao executar uma função.

Exemplo:

# Errado
diz_oi 

# Certo
diz_oi()

# Errado 
diz_oi ()
"""


# Exemplo 2

def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')


# for n in range(5):
#     cantar_parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável

canta = cantar_parabens

canta()