lista = []

while len(lista) < 10:
    n = int(input('Digite o número: '))
    lista.append(n)

x = int(input('Informe um valor para encontrar os múltiplos: '))
contador = 0

for i in lista:
    if i % x == 0:
        print(f'O valor {i} é múltiplo de {x}')
        contador += 1

print(contador)