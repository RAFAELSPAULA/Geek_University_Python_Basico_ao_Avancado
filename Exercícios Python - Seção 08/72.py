def vetor(x, y, z):
    lis = list()
    lis.append(float(x))
    lis.append(float(y))
    lis.append(float(z))
    return lis


def soma(v1, v2, res):
    for i, z in zip(v1, v2):
        res.append(i + z)
    return res


vet1 = vetor(2, 3, 5)
vet2 = vetor(-3, 8, 9)
print(soma(vet1, vet2, []))  # RESP-> [-1.0, 11.0, 14.0]