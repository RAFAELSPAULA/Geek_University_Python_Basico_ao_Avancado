"""
Leio um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""
Segundos = int(input('Valor em segundos: '))

Horas = Segundos // 3600 # Divisão Inteira
Resto = Segundos % 3600  # Pega Resto da Divisão Inteira

Minutos = Resto // 60 # Pega Resto do Resto e transofrma em minutos fazendo uma divisão Inteira
SegundosR = Resto % 60 # E por fim resto da divisão minutos em segundos.

# Imprimir Valores

print(Horas, ':', Minutos, ':', SegundosR)