lista = []

while len(lista) < 15:
    nota = float(input('Digite o valor da nota: '))
    lista.append(nota)

total = sum(lista)
media = total / 15
print(media)
