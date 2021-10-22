r1 = int(input('Digite valor de R1:'))
r2 = int(input('Digite valor de R2: '))

r = (r1 * r2) / (r1 + r2)

while r != 0:
    r1 = int(input('Digite valor de R1:'))
    r2 = int(input('Digite valor de R2: '))
    r = (r1 * r2) / (r1 + r2)

print(f'Valor de r : {r}')
