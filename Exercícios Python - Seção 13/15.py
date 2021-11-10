from datetime import datetime

with open('data.txt', 'r') as arquivo:
    ano = datetime.today().year
    texto = list(arquivo.read().split('\n'))
    with open('data_string.txt', 'w+') as novo:
        for linha in texto:
            anotemp = abs(int(linha[-4:]))
            msg = 'menor de idade' if ano - anotemp < 18 else 'maior de idade' \
                if ano - anotemp > 18 else 'entrando na maior idade'