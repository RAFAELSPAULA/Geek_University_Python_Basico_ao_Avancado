"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes
fórmulas (onde H corresponde a altura):

* Homem (72.7 * H) - 58
* Mulheres (62.1 * H) - 44.7
"""
a = float(input('Digite a altura da pessoa: '))
s = str(input('Digite o sexo da pessoa: '))

if s == 'Homem':
    homem = (72.7 * a) - 58
    print(f'Peso ideal: {homem:.2f}')
elif s == 'Mulher':
    mulher = (62.1 * a) - 44.7
    print(f'Peso ideal: {mulher:.2f}')
else:
    print('Sexo inválido')