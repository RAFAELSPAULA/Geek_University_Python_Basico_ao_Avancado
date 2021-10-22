"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre
quantos degraus o usuário deverá subir para atingir seu objetivo.
"""
a = float(input('Altura do degrau: '))
m = float(input('Altura que deseja chegar: '))
t = m / a
print(f'Tera que subir: {t} degraus: ')
