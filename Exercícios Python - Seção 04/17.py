"""
Leia um valor de comprimento em centímetro e apresente-o convertido em polegadas. A fórmula de conversão é: P = C/2.54,
sendo C o comprimento em centímetro e P o comprimentos em polegadas.
"""
c = float(input('Digite um valor em centímetros: '))
p = c/2.54
print(f'Valor em polegadas: {p}')
