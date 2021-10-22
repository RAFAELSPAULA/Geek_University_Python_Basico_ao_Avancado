num = 2000000

primo = []
lista = []
cont = 1

while len(primo) < num:
    for i in range(1, cont + 1):
        if cont % i == 0:
            lista.append(i)

    if len(lista) == 2:
        primo.append(cont)
        lista.clear()
    else:
        lista.clear()
    cont += 1

print(f"A soma dos {num} primeiros números primos é {' + '.join(map(str, primo))} = {sum(primo)}")
