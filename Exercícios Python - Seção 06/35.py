x = int(input('Digite Valor Inicial: '))
y = int(input('Digite Valor Final: '))

soma = 0

while y < x or x == y:
    print('O valor inicial deve ser maior que o valor final')
    x = int(input('Digite Valor Inicial: '))
    y = int(input('Digite Valor Final: '))

for i in range(x, y):
    if i % 2 == 1:
        soma += i

print(soma)

















