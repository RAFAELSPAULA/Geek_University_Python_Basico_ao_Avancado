def segundos(horas, minutos, segundo):
    segH = horas / 3600
    segM = minutos * 60
    return segH + segM + segundo


print(segundos(1, 0, 0))

