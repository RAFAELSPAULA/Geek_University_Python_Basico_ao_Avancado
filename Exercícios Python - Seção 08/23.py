def escadinha(n):
    for i in range(1, n + 1):
        if i != n:
            print('*' * i)
        elif i == n:
            print('*' * i)
    for i in range(n, 0, -1):
        if n == i:
            pass
        else:
            print('*' * i)


escadinha(4)
