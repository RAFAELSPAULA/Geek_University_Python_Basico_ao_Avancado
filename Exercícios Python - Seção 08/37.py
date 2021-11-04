import mpmath as mp


def hiper(n):
    return mp.hyperfac(n)


print(hiper(200))
