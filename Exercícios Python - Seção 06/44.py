soma = 0
num_atual = 0
num_anterior = 1
sequencia = [0, 1]

numero = int(input('Digite um número para cálculo da sequência de Fibonacci: '))

while numero < 0:
    print('Você deve digitar um número positivo!')
    numero = int(input('Digite um número para cálculo da sequência de Fibonacci: '))
while True:
    soma = num_atual + num_anterior
    num_anterior = max(sequencia)
    sequencia.append(soma)
    if max(sequencia) > numero:
        break
    else:
        num_atual = soma
print(sequencia)
