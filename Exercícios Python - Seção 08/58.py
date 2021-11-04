import math
import random

n = int(input("Qual a ordem da matriz A ? "))

matrizA: [[float]] = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
    for j in range(n):
        matrizA[i][j] = random.randint(0, 2)

for i in range(n):
    for j in range(n):
        print(matrizA[i][j], end=' ')
    print()
print()

m = int(input("Qual a ordem da matriz B? "))

matrizB: [[float]] = [[0 for x in range(m)] for x in range(m)]

for i in range(m):
    for j in range(m):
        matrizB[i][j] = random.randint(0, 2)

for i in range(m):
    for j in range(m):
        print(matrizB[i][j], end=' ')
    print()
print()

matrizC: [[float]] = [[0 for x in range(n)] for x in range(n)]

for i in range(m):
    for j in range(m):
        matrizC[i][j] = matrizA[i][j] * matrizB[i][j]

for i in range(m):
    for j in range(m):
        print(matrizC[i][j], end=' ')
    print()
print()
