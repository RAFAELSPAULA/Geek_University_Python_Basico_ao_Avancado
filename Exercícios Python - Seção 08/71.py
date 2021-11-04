def ponto(x, y):
    return int(x), int(y)


def dentro_ou_fora(v1=(0, 0), v2=(0, 0), p=(0, 0)):
    if v1[0] < p[0] < v2[0]:
        if v1[1] < p[1] < v2[1]:
            return 1
    return 0


v01 = ponto(3, 2)
v02 = ponto(6, 8)
p01 = ponto(4, 5)

print(dentro_ou_fora(v01, v02, p01))
if dentro_ou_fora(v01, v02, p01) == 1:
    print(f"O Ponto {p01}, Está Dentro do Retângulo de vértices {v01} e {v02} ")
else:
    print("Fora")
# 1
# O Ponto (4, 5), Está Dentro do Retângulo de vértices (3, 2) e (6, 8)
