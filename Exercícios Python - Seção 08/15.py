def triangulo(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return 'Não é permitido números negativos!'

    if c < a + b and \
            a < b + c and \
            b < c + a:
        if a == b and b == c:
            return 'Triângulo equilátero!'
        if a == b and b != c or \
                b == c and c != a or \
                c == a and a != b:
            return 'Triângulo isósceles'
        if a != b and b != c:
            return 'Triângulo escaleno!'

    return 'Não é triângulo!'


a = int(input('Digite o primeiro lado do triângulo: '))
b = int(input('Digite o segundo lado do triângulo: '))
c = int(input('Digite o terceiro lado do triângulo: '))

print(triangulo(a, b, c))
