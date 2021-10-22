"""
Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a tabela baixo, quando aluno tem
mais de 20 faltas ocorre uma redução de conceito.

Nota 9 a 10 = A - B
7.5 a 8.9 = B - C
5.0 a 7.4 = C - D
4.0 a 4.9 = D - E
0.0 a 3.9 = E - E
"""
n = float(input('Digite a sua nota: '))
f = int(input('Digite quantidade de faltas: '))

if (n > 0) and (n < 3.9) and (f < 20):
    print('Conceito E')
elif (n > 0) and (n < 3.9) and (f > 20):
    print('Conceito E')
elif (n > 4.0) and (n < 4.9) and (f < 20):
    print('Conceito D')
elif (n > 4.0) and (n < 4.9) and (f > 20):
    print('Conceito E')
elif (n > 5.0) and (n < 7.4) and (f < 20):
    print('Conceito C')
elif (n > 5.0) and (n < 7.4) and (f > 20):
    print('Conceito D')
elif (n > 7.5) and (n < 8.9) and (f < 20):
    print('Conceito B')
elif (n > 7.5) and (n < 8.9) and (f > 20):
    print('Conceito C')
elif (n > 9.0) and (n < 10.0) and (f < 20):
    print('Conceito A')
elif (n > 9.0) and (n < 10.0) and (f > 20):
    print('Conceito B')
