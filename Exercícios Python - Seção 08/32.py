def divisor(n):
    i = 2
    vet = []
    while n != 1:
        while int(str(n / i).split('.')[1]) > 0:
            i += 1
        n /= i
        vet.append(i)
    return vet


def simplifica(num, den):
    if len(set(divisor(num)).intersection(divisor(den))) == 0:
        return 'Fração irredutível'
    i = 1
    while len(set(divisor(num)).intersection(divisor(den))) != 0:
        if num % i == 0 and den % i == 0:
            num /= i
            den /= i
            i = 1
        i += 1
    return str(int(num)) + '/' + str(int(den))


n = int(input('Digite o númerador: '))
d = int(input('Digite o divisor: '))
if n > 0 and d > 0:
    frac = simplifica(n, d)
    if 'irredutível' not in frac:
        print('Fração simplificada: ', frac)
    else:
        print('Fração irredutível')
else:
    print('Número inválido!')