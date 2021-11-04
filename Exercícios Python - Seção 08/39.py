def troque(a, b):
    primeira = b
    b = a
    a = primeira
    return a, b


print(troque(1, 2))
