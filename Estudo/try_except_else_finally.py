"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!
OBS: A função do usuário é DESTRUIR seu sistema.

Else -> E executado somente se não ocorrer o erro.

num = 0

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor Incorreto')
else:
    print(f'Você digitou {num}')
# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o Finally')

# OBS: O bloco finally é Sempre executado. Independente se houve exceção ou não.
# O finally, geralmente, é utilizando para fechar ou deslocar recursos.

# Exemplo mais complexos Errado

def dividir(a, b):
    return a / b


num1 = int(input('Informe o primeiro número: '))
try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O Valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

# Exemplo mais complexo Correto.
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return a / b
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por 0'


num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(dividir(num1, num2))

# Exemplo mais complexo Generic.
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'


num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(dividir(num1, num2))

# Exemplo mais complexo semi Generic.
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(dividir(num1, num2))


"""

