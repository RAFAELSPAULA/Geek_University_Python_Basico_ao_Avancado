"""
Faça um programa para ler o horário (hora, minuto e segundo) de inicio e a duração, em segundos, de uma experiência
biológica. O Programa deve resultar como o novo horário (hora, minutos e segundo) do termino da mesma.
"""
print("Digite a hora os minutos e os segundos abaixo")

hor = int(input('Horas: '))
mi = int(input('Minutos: '))
seg = int(input('Segundos: '))
dur = int(input('Informe a duração em segundos: '))

hor = hor * 3600
mi = mi * 60
tSec = hor + mi + seg + dur

hFinal = int(tSec / 3600)
rest = tSec % 3600
miFinal = int(rest / 60)
rest = rest % 60

print(f"A experiência irá terminar as: {hFinal}:{miFinal}:{rest}")