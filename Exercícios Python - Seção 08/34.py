def fatorialDuplo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorialDuplo(n - 2)


print(fatorialDuplo(5))
