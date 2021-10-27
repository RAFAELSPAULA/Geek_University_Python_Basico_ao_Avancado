vetor = []
contador = 1

while len(vetor) < 100:
    if contador % 7 == 0 or str(contador)[-1] == '7':
        vetor.append(contador)
    contador += 1

print(f'Acabei de preencher um vetor com {len(vetor)} números múltiplos de 7 ou que terminam em 7')
print(vetor)