import random

c = 0

while True:
    n = random.randint(1, 1000)
    a = int(input('Tente acertar o valor: '))
    if n > a:
        print('Número maior que  N')
        c += 1
    if n < a:
        print('Número menor que N')
        c += 1
    if n == a:
        break
print(f'Número de tentativas erradas {c}')
