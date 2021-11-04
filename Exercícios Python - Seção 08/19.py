def maior_fator_primo(n):
    i = 2
    maior_fator = 0
    while n != 1:
        while int(str(n / i).split('.')[1]) > 0:
            i += 1
        n /= i
        maior_fator = i
    return maior_fator


f = int(input('Digite um número positivo maior que 0: '))
if f > 0:
    print('Maior fator primo: ', maior_fator_primo(f))
else:
    print('Número inválido!')
