salario = 2030
ano = 1997
aumento = 0
juros = 1.5

while True:
    if ano == 2021:
        break
    if ano != 2021:
        salario = (salario * juros) + salario
        juros = juros * 2
        print(juros)
        ano += 1

print(salario)
