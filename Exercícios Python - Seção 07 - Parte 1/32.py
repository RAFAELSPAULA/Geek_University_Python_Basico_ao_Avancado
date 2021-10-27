x = []
y = []
soma = 0
vetor_soma = []
vetor_multiplicacao = []
vetor_diferenca = []
vetor_intersecao = []
vetor_uniao = []

for numero in range(1, 6):
    x.append(int(input(f"Informe um Numero {numero} / 5: ")))

for numero_2 in range(1, 6):
    y.append(int(input(f"Informe um Numero {numero_2} / 5: ")))

for soma_x, soma_y in zip(x, y):
    soma = soma_x + soma_y
    vetor_soma.append(soma)

for multiplicaco_x, multiplicaco_y in zip(x, y):
    multiplicao = multiplicaco_x * multiplicaco_y
    vetor_multiplicacao.append(multiplicao)

for diferenca_x, diferenca_y in zip(x, y):
    if diferenca_x != diferenca_y:
        vetor_diferenca.append(diferenca_x)

for intersecao_x, intersecao_y in zip(x, y):
    vetor_intersecao = list(set(x).intersection(y))

for uniao_x, uniao_y in zip(x, y):
    vetor_uniao = list(set().union(x, y))

print(x)
print(y)
print(f"minha soma: {vetor_soma}\n--------------------------------------------------/")
print(x)
print(y)
print(f"minha multiplicacão: {vetor_multiplicacao}\n--------------------------------------------------/")
print(x)
print(y)
print(f"minha diferença dos elementos em x que nao tem em y {vetor_diferenca}\n--------------------------------------------------/")
print(x)
print(y)
print(f"minha intersecção {vetor_intersecao}\n--------------------------------------------------/")
print(x)
print(y)
print(f"meu vetor união {vetor_uniao}")