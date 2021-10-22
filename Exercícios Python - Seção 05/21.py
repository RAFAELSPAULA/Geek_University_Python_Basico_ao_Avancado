"""
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhidas. Escreva uma mensagem de erro
se a opção for inválida.

Escolha a opção:

1 - Soma de 2 números.
2 - Diferença entre 2 (Maior pelo menor)
3 - Produto entre 2 número
4 - Divisão entre 2 número (o dominador não pode ser zero)
"""
option = int(input('Digite a opção desejada, sendo 1 Soma, 2 Subtração, 3 Divisão e 4 Multiplicação: '))

if option == 1:
    valor1 = float(input('Digite primeiro valor: '))
    valor2 = float(input('Digite segundo valor: '))
    soma = valor1 + valor2
    print(soma)
elif option == 2:
    valor1 = float(input('Digite primeiro valor: '))
    valor2 = float(input('Digite segundo valor: '))
    sub = valor1 - valor2
    print(sub)
elif option == 3:
    valor1 = float(input('Digite primeiro valor: '))
    valor2 = float(input('Digite segundo valor: '))
    div = valor1/valor2
    print(div)
elif option == 4:
    valor1 = float(input('Digite primeiro valor: '))
    valor2 = float(input('Digite segundo valor: '))
    mult = valor1 * valor2
    print(mult)
else:
    print('Opção Inválida')
