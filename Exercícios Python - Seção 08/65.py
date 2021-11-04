def concatena(str1, str2, n):
    soma = str1 + str2[:n]
    str1 = None
    return f'{soma} {str1}'


print(concatena(input('Digite a primeira string: '), input('Digite a segunda string: '),
                int(input('Digite o valor de N: '))))
