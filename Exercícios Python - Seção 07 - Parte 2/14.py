import numpy as np
from random import sample

m = 5
n = 5
v = (m * n)

# Montando uma matriz qualquer.
if v <= 170:
    numeros = sample(range(1, 171), v)
    print(np.array([numeros[i:i+n] for i in range(0, len(numeros), n)]))
else:
    print('Erro! Quantidade de sorteios maiores que o range!')