"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

\n serve para pular uma linha como Enter

\  e utilizado como caractere de escape

nome = "rafael \" Paula"

nome.upper() -> tudo Maiúsculo
nome.lower() -> tudo Minusculo
nome.split() -> Separa cada palavra e coloca em uma lista de string

nome = RAF
# [ 0,   1,   2 ]
# ['R', 'A', 'F']

print(nome[0:4]) -> # Slice de string
print(nome.split()[0])

[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
print(nome[::-1]  # Inversão da String Pythônico

nome.replace('e', 'i') -> troca toda letra e do nome por i.

Palíndromo e um texto que de traz para frente e a mesma coisa.

"""
# - Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""
