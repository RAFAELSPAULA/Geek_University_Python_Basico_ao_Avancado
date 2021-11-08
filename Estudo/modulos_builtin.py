"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalado no Python)
________________________
|Python|Módulos builtin|
------------------------

# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

#Podemos importar todas as funções de um módulo utilizando *

from random import *

print(random())

# Utilizando alias (apelidos) para módulos/frações

from random import randint as rdi

print(rdi(5, 89))

# Utilizando alias (apelidos) para módulos/frações

from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())


"""
# Costumamos a utilizar tuple para colocar multiples import de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)
