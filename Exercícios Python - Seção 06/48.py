proximo = 0
anterior = 0
soma = 0

count = 2
termo = 0

while proximo < 4000000:
    proximo = proximo + anterior
    anterior = proximo - anterior
    if proximo == 0:
        proximo += 1
    if proximo % 2 == 0:
        soma += proximo

print(soma)