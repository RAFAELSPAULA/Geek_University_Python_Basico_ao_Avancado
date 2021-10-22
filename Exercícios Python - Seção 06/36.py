soma = 0
q = 0
q2 = 0

for i in range(1, 101):
    soma = soma + i ** 2

for i in range(1, 101):
    q += i
    q2 = q ** 2


resultado = q2 - soma
print(f'Diferença entre {q2} - {soma} = {resultado}')


