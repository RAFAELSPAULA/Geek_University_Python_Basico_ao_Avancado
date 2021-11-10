with open('arq.txt', 'r') as arquivo:
    carac = str(input('Digite uma letra: '))
    a = filter(lambda x: x in carac, arquivo.read())

print(len(list(a)))
