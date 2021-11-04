def serie(n):
    s = 0
    for i in range(1, n + 1):
        s += ((i ** 2) + 1) / (i + 3)
    return s


n = int(input('Digite um número positivo maior que 0: '))
if n > 0:
    print(f'Série: {serie(n)}')
else:
    print('Número inválido!')
