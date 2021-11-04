from statistics import stdev


def desvio(a, b, c, d, e, f):
    return stdev([a, b, c, d, e, f])


print(desvio(1.5, 2.5, 2.5, 2.75, 3.25, 4.75))
