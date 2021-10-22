"""
Faça um programa que receba três números e mostre-os em ordem crescente.
"""
lista = [int(input("Digite o primeiro número: ")),
         int(input("Digite o segundo número: ")),
         int(input("Digite o terceiro número: "))]

lista.sort()
print(lista)
