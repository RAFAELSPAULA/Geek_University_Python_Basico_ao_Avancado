def pesquisa():

    sexo = []
    cor = []
    cabelo = []
    idade = []
    media = 0
    conta = 0

    while True:
        if len(idade) == 5:
            break
        a = str(input('Digite seu sexo: '))
        if a == 'M' or a == 'F':
            sexo.append(a)
        else:
            print('Somente Masculino ou Feminino')
            a = str(input('Digite seu sexo: '))

        b = str(input('Digite cor dos olhos: '))
        if b == 'A' or b == 'C':
            cor.append(b)
        else:
            print('Somente Azul ou Castanho')
            b = str(input('Digite cor dos olhos: '))

        c = str(input('Digite cor do cabelo: '))
        if c == 'L' or c == 'P' or c == 'C':
            cabelo.append(c)
        else:
            print('Somente Loiro ou Preto ou Castanho')
            c = str(input('Digite cor do cabelo: '))

        d = int(input('Digite sua idade: '))
        if d > 0:
            idade.append(d)
        else:
            print('Idade deve ser acima de 0')
            d = str(input('Digite sua idade: '))
    soma = 0
    cont = 0

    for i in range(0, 5):
        if cor[i] == 'C' and cabelo[i] == 'P':
            soma += idade[i]
            cont += 1

    media = soma / cont

    h = max(idade)

    for i in range(0, 5):
        if sexo[i] == 'F' and (18 < idade[i] <= 35) and cor[i] == 'A' and cabelo[i] == 'L':
            conta += 1

    return media, h, conta


print(pesquisa())

