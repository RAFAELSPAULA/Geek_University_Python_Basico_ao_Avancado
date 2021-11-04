def somatorio(a):
    soma = 0
    for i in range(1, a + 1):
        soma += i
    return soma


a = int(input('Digite um número positivo maior que 0: '))
if a > 0:
    print(f'Série: {somatorio(a)}')
else:
    print('Número inválido!')
