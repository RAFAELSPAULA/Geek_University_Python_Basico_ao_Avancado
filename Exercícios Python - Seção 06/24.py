n = int(input("Digite um número: "))

soma = 0
print(f'A soma dos divisores do número é {n}: ', end='')

for i in range(1, n):
    if n % i == 0:
        soma += i
        print(f'{i} ', end='+ ' if soma < n else f'= {soma}')
