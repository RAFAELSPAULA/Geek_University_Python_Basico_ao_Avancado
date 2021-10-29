from random import uniform

prova = []
result1, result2, result3 = 0, 0, 0


for n in range(10):
    prova.append([])
    for i in range(3):
        prova[n].append(f'{(uniform(3.0, 10.0)):.1f}')  # Usando 3.0 como menor nota

for c in prova:
    if c.index(min(c)) == 0:
        result1 += 1
    elif c.index(min(c)) == 1:
        result2 += 1
    else:
        result3 += 1

print(f'{result1} Aluno(s) com pior nota na PRIMEIRA prova!')
print(f'{result2} Aluno(s) com pior nota na SEGUNDA prova!')
print(f'{result3} Aluno(s) com pior nota na TERCEIRA prova!')
