from random import randint

# Código original
with open('binario.txt', 'w') as bina:
    for i in range(10):
        bina.write(bin(randint(1, 1000)))

# Usei a var num só para verificação
with open('binario.txt', 'w') as bina:
    for i in range(10):
        num = randint(1, 1000)
        bina.write(bin(num) + ' - ' + str(num) + '\n')