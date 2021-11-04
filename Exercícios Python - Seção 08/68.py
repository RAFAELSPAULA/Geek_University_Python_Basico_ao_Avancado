def intercalar(a, b):
    res = "".join(i + j for i, j in zip(a, b))
    return res


print(intercalar('ol', 'as'))
