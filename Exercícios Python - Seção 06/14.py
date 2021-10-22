n = int(input('Digite Quantas Vezes Deseja repetir: '))

for i in range(n, -1, -1):
    if i % 2 == 0:
        print(i)
