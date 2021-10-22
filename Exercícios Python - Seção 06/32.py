import random

n = int(input('Digite um valor: '))

d1 = 0
d2 = 0

for i in range(1, n+1):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    if d1 > d2:
        print(f'{d1} > {d2}')
    elif d1 < d2:
        print(f'{d1} < {d2}')
    elif d1 == d2:
        print(f'{d1} = {d2}')





