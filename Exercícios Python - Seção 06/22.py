nota = int(input('Digite sua nota: '))
soma = 0
base = 1

while True:
    if 10 <= nota <= 20:
        nota = int(input('Digite sua nota: '))
        soma += nota
        base += 1
    else:
        break

media = soma / base
print(f'Média : {media}')

