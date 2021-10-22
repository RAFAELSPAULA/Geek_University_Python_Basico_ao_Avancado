base = int(input('Digite valor da base: '))

while base <= 0:
    print('Valor inválido')
    base = int(input('Digite valor da base: '))

altura = int(input('Digite valor da altura: '))

while altura <= 0:
    print('Valor inválido')
    altura = int(input('Digite valor da altura: '))

a = (base * altura) / 2

print(a)
