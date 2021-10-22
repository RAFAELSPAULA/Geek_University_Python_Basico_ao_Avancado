"""
Calcule as raízes da equação de 2° grau.

Lembrando que:

x = (-b±√delta) / 2a

Onde

Delta = B² - 4ac

E ax² + bx + c = 0 presenta uma equação de 2° grau.

A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Não é equação de segundo grau".

Se delta < 0, não existe real. Imprima a mensagem - Não Existe Raiz.
Se delta = 0, Existe uma raiz real. Imprima a raiz e a mensagem - Raiz única.
se delta > 0, imprima as duas raízes reais
"""
a = float(input('Digite valor de a: '))

if a == 0:
    print('Não é equação de segundo grau')
else:
    b = float(input('Digite valor de b: '))
    c = float(input('Digite valor de c: '))
    delta = (b ** 2) - (4 * a * c)
    print(delta)
    if delta < 0:
        print('Não Existe Raiz')
    elif delta == 0:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f'Raiz única: {x1} {x2}')
    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f'Raízes Reais: {x1} {x2}')

