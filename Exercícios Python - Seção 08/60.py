a = str(input('Digite uma string: '))
b = list(a)
print(len(b))


def slince():
    if len(b) >= 1:
        return print(a[0])
    else:
        return print(-1)


slince()
