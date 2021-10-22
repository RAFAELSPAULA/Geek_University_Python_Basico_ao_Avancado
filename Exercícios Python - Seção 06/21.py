x = int(input('Digite um número: '))
y = int(input('Digite um número: '))

par = 0
impar = 1

while y < x or x == y:
    print('O valor de y deve ser maior que o valor de x')
    x = int(input('Digite um número para X: '))
    y = int(input('Digite um número para Y: '))

for i in range(x - 1, y + 1):
    if i % 2 == 0:
        par = par + i
    elif i % 2 != 0:
        impar = impar * i

print('A soma dos números pares entre', x, 'e', y, 'é', par, '.')
print('A multiplicação dos números impares entre', x, 'e', y, 'é', impar, '.')
