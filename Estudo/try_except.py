"""
O bloco try/except

Utilizamos o bloco  try/except para tratar erros que podem ocorrer no nosso código. Prevenindo assim que o programa
para de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um error genérico

try:
    geek()
except:
    print('Deu algum Problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

# Exemplo 2 - Tratando um error genérico

try:
    len(5)
except:
    print('Deu algum Problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de forma
específica.

# Exemplo 3 - Tratando um error específico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 4 - Tratando um error específico

try:
    len(5)
except TypeError:
    print('Você está utilizando uma função inexistente')

# Exemplo 5 - Tratando um error específico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    len(5)
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')


"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "Geek"}

print(pega_valor(dic, "game"))
