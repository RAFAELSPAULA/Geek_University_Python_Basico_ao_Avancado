"""
Reversed

OBS: Não confunda com a função reverse() que estudamos em listas.

A função reverse() só funciona em listas.

Ja á função reversed() funciona com qualquer iterável.

Sua função e inverter o iterável.

A função reversed() retorna um iterável chamado list reverse interator

"""
# Exemplo

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla ou Conjunto

# lista
print(list(reversed(lista)))

# tupla
print(tuple(reversed(lista)))

# Conjunto
# Em Conjunto, não definimos a ordem dos elementos
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

# Podemos fazer o mesmo sem o uso for
print()
print(''.join(list(reversed('Geek University'))))

# Já vimos como fazer isso mais fácil com o slice de strings
print('Geek University'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

# Apesar que também já vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)

