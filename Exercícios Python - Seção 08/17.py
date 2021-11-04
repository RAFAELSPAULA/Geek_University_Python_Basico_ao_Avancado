def numeros(a, b):
    if a > b:
        maior = b
        b = a
        a = maior
    lista = 0
    for i in range(a, b+1):
        lista += i
    return lista


print(numeros(5, 1))
