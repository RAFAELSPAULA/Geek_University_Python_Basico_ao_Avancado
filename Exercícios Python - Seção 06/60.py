soma = 0
soma_pares = 0
cont = 0
cont_par = 0
maior = -999999999999
menor = 99999999999

n = int(input("Informe um número: "))
while n != 0:
    soma += n
    cont += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    if n % 2 == 0:
        cont_par += 1
        soma_pares += n
    n = int(input("Informe um número: "))
    
print(f"A soma dos números digitados é igual a {soma}")
print(f"A quantidade de números digitados é igual a {cont}")
print(f"A média dos números digitados é igual a {soma / cont}")
print(f"O maior número digitado é igual a {maior}")
print(f"O menor número digitado é igual a {menor}")
print(f"A média dos números pares é igual a {soma_pares / cont_par}")
