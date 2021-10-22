valor1 = maior = 0
menor = 999999

while True:
    valor1 = int(input("Digite um número: "))
    if valor1 <= 0:
        break
    if valor1 > maior:
        maior = valor1

    if valor1 < menor:
        menor = valor1

print(f"E o maior valor é :-> {maior}")
print(f"E o menor valor é :-> {menor}")
