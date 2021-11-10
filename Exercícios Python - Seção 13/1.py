with open('arq.txt', 'w') as arquivo:
    while True:
        a = input('Digite algo ou sair: ')
        if a != 'sair':
            arquivo.write(a)
            arquivo.write('\n')
        else:
            break

