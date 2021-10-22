n = int(input('Digite um valor: '))
i = int(input('Digite valor de i: '))

while i <= 0:
    print('Valor não pode ser  menor que zero!')
    i = int(input('Digite valor de i: '))

j = int(input('Digite valor de j: '))

while j <= 0:
    print('Valor não pode ser  menor que zero!')
    j = int(input('Digite valor de j: '))

for k in range(0, n + 3):
    if k % i == 0 or k % j == 0:
        print(k, end=', ' if n + 1 > k else '.')
