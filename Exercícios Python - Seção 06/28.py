import math

soma = 1

numero = int(input("Digite um número: "))

while numero <= 0:
    print("Você deve digitar um número maior do que 0 (zero)!")
    numero = int(input("Digite um número: "))
for n in range(numero, 0, -1):
    soma = soma + (1 / math.factorial(n))
print(f'\nO resultado de E para N = {numero} é >>>> {soma:.5f}.')