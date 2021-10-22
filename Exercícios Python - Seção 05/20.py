"""
Dados três valores, A,B,C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um triângulo
escaleno, equilátero ou isóscele, considerando os seguintes conceitos:

* O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
* Chama-se equilátero o triângulo que tem três lados iguais.
* Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
* Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""
a = float(input('Digite valor de A: '))
b = float(input('Digite valor de B: '))
c = float(input('Digite valor de C: '))

if a == b == c:
    print('Triângulo Equilátero')
elif b == c:
    print('Triângulo Isósceles')
elif a != b != c:
    print('Triângulo Escaleno')