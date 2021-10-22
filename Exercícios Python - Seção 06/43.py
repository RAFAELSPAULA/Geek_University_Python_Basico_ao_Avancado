idade = int(input('Digite sua idade: '))

idadet = idade
base = 0

while True:
    if idade == 0:
        break
    if idade > 0:
        idade = int(input('Digite sua idade: '))
        idadet += idade
        base += 1

media = idadet / base
print(idadet)
print(base)
print(media)