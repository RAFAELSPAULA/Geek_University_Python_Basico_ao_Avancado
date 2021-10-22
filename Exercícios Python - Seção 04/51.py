"""
Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0,0)
"""
x1 = int(input(f'Informe x1 => '))
y1 = int(input(f'Informe y1 => '))

# Elevar à uma fracão corresponde a tirar a raiz tendo como com indices
# Número indicado no denominador

distancia = int((((0 - x1) ** 2) + ((0 - y1) ** 2)) ** (1 / 2))

print(f'A distância entre a origem (0,0) e o ponto de coordenadas ({x1},{y1}) é: {distancia}')
print(f'Distância da origem = {distancia}')
