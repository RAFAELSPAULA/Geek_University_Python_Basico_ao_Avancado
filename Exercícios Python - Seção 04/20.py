"""
Leia um valor de massa em quilograma e apresente-o convertido em libras. A fórmula de conversão é: L = k/0.45, sendo K
a massa em quilograma e L a massa em libras.
"""
k = float(input('Digite um valor em quilograma: '))
libras = k/0.45
print(f'Valor da massa em libras: {libras}')