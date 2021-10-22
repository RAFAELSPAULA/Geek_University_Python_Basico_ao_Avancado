"""
Leia um salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário:
'Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.
"""
s = float(input('Digite valor do salário: '))
pl = s * 0.2
p = float(input('Digite valor da prestação: '))

if pl > p:
    print('Empréstimo concedido')
else:
    print('Empréstimo não concedido')
