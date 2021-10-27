lista = []


while len(lista) < 5:
    n = int(input('Digite um valor: '))
    lista.append(n)

cod = int(input('Digite Comando 1 para ordem normal e 2 para inversa ou 0 para sair: '))

while True:
    if cod == 0:
        break
    if cod == 1:
        print(lista)
        break
    if cod == 2:
        lista.reverse()
        print(lista)
        break
    if cod != 0 and cod != 1 and cod != 2:
        print('Comando invalido!!!')
        cod = int(input('Digite Comando 1 para ordem normal e 2 para inversa ou 0 para sair: '))

