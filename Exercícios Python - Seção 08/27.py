from math import factorial, radians


def seno(x, n=7):
    x = radians(x)

    def termo_geral(x, i):
        return ((-1) ** i / factorial(2 * i + 1)) * (x ** (2 * i + 1))

    def termos(x, n):
        for i in range(n):
            yield termo_geral(x, i)

    return sum(termos(x, n))


print(seno(0.5, 7))
