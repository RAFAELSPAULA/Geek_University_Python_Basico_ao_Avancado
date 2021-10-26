"""
Módulo Collections - Named Tuple

- Recap Tupla

tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> São Tuplas, diferenciadas, onde, especificamente um nome para a mesma e também parâmetros

from collections import namedtuple

- Precisamos definir o nome e parâmetros.

- Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

- Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

- Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade, raca, nome'])

- Usando

ray = cachorro (idade=2, raca='Chow-Chow', nome='Ray')

print(ray)

- Forma 1

print(ray[0]) - Idade
print(ray[1]) - raça
print(ray[2]) - nome

- Forma 2

print(ray.idade) - idade
print(ray.raca) - raça
print(ray.nome) - nome


"""