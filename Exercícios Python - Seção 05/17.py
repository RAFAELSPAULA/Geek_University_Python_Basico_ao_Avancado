"""
Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:

A = ((baseMaior + baseMenor) * Altura)/2

Lembre-se a base maior e a base menor devem ser números maiores que zero.
"""
baseMaior = float(input('Digite a base maior: '))

if baseMaior < 0:
    print('Base invalida')
else:
    baseMenor = float(input('Digite a base menor: '))
    if baseMenor < 0:
        print('Base invalida')
    else:
        altura = float(input('Digite a altura: '))
        a = ((baseMaior + baseMenor) * altura) / 2
        print(f'Area do Trapézio: {a}')


