import math


def fatorialDuplo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return math.factorial(2 * n) / math.factorial(n)


print(fatorialDuplo(2))
