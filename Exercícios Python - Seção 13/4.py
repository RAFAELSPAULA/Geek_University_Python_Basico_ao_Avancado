with open('arq.txt', 'r') as arquivo:
    vogais = filter(lambda x: x in 'aeiouAEIOU', arquivo.read())
    print(len(list(vogais)))

with open('arq.txt', 'r') as arquivo:
    con = filter(lambda x: x in 'bcdfghjklmnpqrstvwxz', arquivo.read())
    print(len(list(con)))
