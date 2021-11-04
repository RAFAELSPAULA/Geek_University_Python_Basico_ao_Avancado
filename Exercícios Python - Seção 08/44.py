from random import randint


def vetores():
    lista = []
    listaP = []
    listaI = []

    for i in range(0, 5):
        lista.append(randint(0, 100))

    for i in lista:
        if i % 2 == 0:
            listaP.append(i)
        else:
            listaI.append(i)
    return print(lista), print(listaP), print(listaI)


print(vetores())
