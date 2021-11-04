import math


def superFatorial(n, ):
    multi = 1
    for i in range(1, n + 1):
        multi *= math.factorial(i)
    return multi


print(superFatorial(4))
