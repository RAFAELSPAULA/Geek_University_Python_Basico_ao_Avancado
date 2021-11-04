def triangulo(n):
    matriz = []
    z = 0
    for i in range(1, n + 1):
        lista = []
        asterisco = (z + 1) * '*'
        lista.append(asterisco)
        matriz.append(lista)
        z += 2
    x = n
    for j in range(0, n):
        print(f"{x * ' '}{matriz[j][0]}")
        x -= 1


y = 6
triangulo(y)
